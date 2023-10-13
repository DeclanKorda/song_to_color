from __future__ import print_function
import warnings
import serial.tools.list_ports
import time
import spotipy
import csv
import torch
import numpy as np
import colorsys
from config import *


class KNN:
    included_features = included_features

    colors = {"R": [0, 1],
              "B": [np.pi * (4 / 3), 1],
              "G": [np.pi * 2 / 3, 1],
              "C": [np.pi, 1],
              "M": [np.pi * 5 / 3, 1],
              "Y": [np.pi / 3, 1],
              "P": [np.pi * 3 / 2, 1],
              "O": [np.pi / 6, 1],
              "T": [np.pi * 5 / 6, 1],
              "F": [np.pi * 11/6, 1],
              "S": [np.pi * 7/6, 1],
              "N": [np.pi / 2, 1],
              "W": [0, 0.5]}

    def __init__(self, file):
        self.k = k
        self.labels = []
        dataset = []
        with open(file, "r") as data:
            reader = csv.reader(data)
            for line in reader:
                x = [float(line[KNN.included_features[i]]) for i in KNN.included_features]
                dataset.append(x)
                self.labels.append(line[-1])
        self.dataset = torch.Tensor(dataset)

    def eval(self, feature_data):

        dist = torch.norm(self.dataset - feature_data, dim=1, p=None)
        # returns a list of the k most similar tracks
        knn = dist.topk(self.k, largest=False)
        print('kNN dist: {}, index: {}'.format(knn.values, knn.indices))

        results = []
        total_weight = float(0)
        total_value = float(0)
        for x, y in zip(knn.values, knn.indices):
            if x == 0:
                weight = k*10
            else:
                weight = 1 - 1 / (1 + np.exp(-(10 * float(x)-4)))
            print(str(int(y)) + ": " + self.labels[y])
            hv = KNN.colors[self.labels[y]]
            hue = hv[0]
            total_value += hv[1] * weight
            total_weight += weight
            results.append([weight, hue])
        # compute weighted-average hue

        points = list(map(lambda i: [i[0] * np.cos(i[1]), i[0] * np.sin(i[1])], results)) # converts hue into coordinates on color wheel
        point_sum = [sum(x) for x in zip(*points)]
        average_point = [
            point_sum[0] / k,
            point_sum[1] / k
        ]
        average_hue = (np.arctan2(average_point[1], average_point[0]) * 180 / np.pi)
        if average_hue < 0:
            average_hue = 360 + average_hue
        average_value = total_value / total_weight
        print("hue: {0}, value {1}".format(average_hue, average_value))
        return list(map(lambda x: x * 255, colorsys.hsv_to_rgb(average_hue / 360, average_value, 1)))


model = KNN(dataset)

device_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if p.manufacturer is not None
    if device_name in p.manufacturer
]
print(device_ports)
if not device_ports:
    raise IOError("No {0} found".format(device_name))
if len(device_ports) > 1:
    warnings.warn('Multiple {0}, using first'.format(device_name))
connection = serial.Serial(device_ports[0])

SCOPE = 'user-read-currently-playing user-modify-playback-state'
CLIENT_ID = client_id
REDIRECT_URI = 'https://localhost/'

auth = spotipy.oauth2.SpotifyPKCE(client_id=CLIENT_ID, redirect_uri=REDIRECT_URI, scope=SCOPE)

token = auth.get_access_token()

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.currently_playing()
    if results != None:
        item = results['item']
        print(item['name'] + ' - ' + item['artists'][0]['name'])
else:
    print("Can't get token")
current_song = ""
while True:
    result = sp.currently_playing()
    if result:
        item = result["item"]
        if item != None and item["name"] != current_song:
            current_song = item["name"]
            track = sp.audio_features(item["id"])[0]
            feature_data = np.array([float(track[i]) for i in KNN.included_features])
            feature_data = torch.Tensor(feature_data).view(1, len(KNN.included_features))

            final_color = model.eval(feature_data)
            print(item["name"])
            print("RGB value:")
            print(final_color, "\n")
            connection.write(bytes([int(final_color[0]), int(final_color[1]), int(final_color[2])]))
        time.sleep(1)
