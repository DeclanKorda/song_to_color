# Song To Color
Python script which changes the color of your led lights to match the vibe of the song playing on your spotify.

Uses a KNN algorithmn and a dataset of spotify audio features from about 500 songs which I have classified as either red, blue, green, cyan, magenta, yellow, teal, orange, purple, sky blue, yellow-green, or pink.
The algorithmn finds the top k similar songs in the database and averages the hue of those songs. The result is then sent by serial connection to the Arduino controlling the LED strip.

# Setup
```bash
# Create conda environment
conda create --name test-env
# Activate conda environment
conda activate test-env
# Clone repo
git clone https://github.com/DeclanKorda/song_to_color
# Install required python dependencies
pip3 install -r requirements.txt
```
# Run:
- Get a spotify API key
- Edit config.py to fit your needs
- Upload arduino script to arduino
- Run main.py
- Follow instructions to connect your spotify account
  NOTE: after logging into spotify, you will be redirected to a broken URL. The terminal will prompt you to copy/paste this URL.
- Play a song, and the leds should update to match the energy of the song.
# Updating Dataset:
- Run 'data gatherer.py'
- play a song on spotify
- the program will prompt you to select a color which matches the energy of the song. Upon selection the next track will play.

This project was requested by a friend of mine. 
