from __future__ import print_function
import spotipy
import spotipy.util as util
import csv
import time

scope = 'user-read-currently-playing user-modify-playback-state'

username = 'mvdyjz4ogwn3b3pyuh6r30ufy'

r = "\x1B[38;5;196m"
b = "\x1B[38;5;4m"
g = "\x1B[38;5;2m"
c = "\x1B[38;5;51m"
m = "\x1B[38;5;200m"
y = "\x1B[38;5;226m"
p = "\x1B[38;5;129m"
o = "\x1B[38;5;202m"
t = "\x1B[38;5;42m"
n = "\x1B[38;5;190m"
w = "\x1B[38;5;15m"
s = "\x1B[38;5;32m"
ff = "\x1B[38;5;204m"

SCOPE = 'user-read-currently-playing user-modify-playback-state'
CLIENT_ID = 'd66ba13f375a46879267cb812a06724f'
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
    print("Can't get token for", username)

with open("dataset.csv", "a") as f:
    writer = csv.writer(f)
    input("please open spotify and play a song. once a song is playing press enter.")

    while True:

        time.sleep(0.5)
        results = sp.currently_playing()
        if results != None:
            item = results['item']
            track = sp.audio_features(item["id"])[0]
            color = input("Select a color for {0}. enter -1 to exit."
                          "\n color options: "
                          "\n{1}R {2}G {3}B "
                          "\n{4}C {5}M {6}Y"
                          "\n{7}P {8}O {9}T"
                          "\n{10}F {11}S {12}N"
                          "\n{13} W\n".format(item["name"], r, g, b, c, m, y, p, o, t, ff, s, n, w))

            if color == "-1":
                break
            print(track)
            writer.writerow([
                track["acousticness"],
                track["danceability"],
                track["energy"],
                track["instrumentalness"],
                track["liveness"],
                track["loudness"],
                track["mode"],
                track["speechiness"],
                track["tempo"],
                track["valence"],
                color])

        input("press enter for the next track")
        sp.next_track()
