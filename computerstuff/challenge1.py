from adafruit_circuitplayground import cp
import time

while True:
     if cp.button_a:
           leds = [0, 1, 2, 3, 4, 5, 6, 7, 9,]
           for led in leds:
                 cp.pixels[led] = (0, 0, 1)
                 time.sleep(0.1)
                 cp.pixels[led] = 0.