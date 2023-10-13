// I won't lie I generated this file with chatGPT. What good is technology if we dont use it right?

#include <FastLED.h>

// Define the number of LEDs in your strip
#define NUM_LEDS 6

// Define the data pin to which the LED strip is connected
#define LED_DATA_PIN 6

// Create an array to store the LED colors
CRGB leds[NUM_LEDS];

void setup() {
  // Initialize the LED strip
  FastLED.addLeds<WS2812B, LED_DATA_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(128); // Adjust the brightness (0-255)

  // Uncomment this line if you want to clear the strip at startup
  // FastLED.clear();
  
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  // Check if there is serial data available
  if (Serial.available() >= 3) {
    // Read the incoming RGB values from Python
    
    int r = Serial.read();
    int g = Serial.read();
    int b = Serial.read();
    Serial.println("RGB:");
    Serial.println(r);
    Serial.println(g);
    Serial.println(b);
    // Update the LED strip with the received RGB values
    colorWipe(CRGB(r, g, b), 50);
  }
}

// Function to fill the entire strip with a single color
void fill_solid(CRGB color) {
  fill_solid(leds, NUM_LEDS, color);
  FastLED.show();
}
// Function to create a color wipe effect
void colorWipe(CRGB color, int wait) {
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = color;
    FastLED.show();
    delay(wait);
  }
}
