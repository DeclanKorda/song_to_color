
# comment out any features that you do not want to use for calculating song color.
included_features = {
        "acousticness": 0,
        "danceability": 1,
        "energy": 2,
        "instrumentalness": 3,
        #"liveness": 4,
        # "loudness": 5,
        # "mode": 6,
        "speechiness": 7,
        "tempo": 8,
        "valence": 9
    }
# how many of the nearest neighbors are used in calculating color
# (eg. if k = 3, the top 3 most similar songs in the dataset determine color)
k = 4
# if you have an off brand arduino, you will need to figure out what it shows up as when you plug it into your computer.
device_name = "Arduino"
# pathway to dataset
dataset = "dataset.csv"

client_id = # your client id here!
