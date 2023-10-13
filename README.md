# song-color-selector
Python script which changes the color of your led lights to match the vibe of the song playing on your spotify.

Uses a KNN algorithmn and a dataset of spotify audio features from about 500 songs which I have classified as either red, blue, green, cyan, magenta, yellow, teal, orange, purple, sky blue, yellow-green, or pink.
The algorithmn finds the top k similar songs in the database and averages the hue of those songs. The result is then sent by serial connection to the Arduino controlling the LED strip.

How to use:
- aqquire a spotify API key
- edit config.py to fit your needs
- upload arduino script to arduino
- install dependancies (pytorch, csv, numpy)
- run main.py, ensuring that dataset.csv is in the same directory
- follow instructions to connect your spotify account
- play a song, and the leds should update to match the energy of the song.

This project was requested by a friend of mine. 
