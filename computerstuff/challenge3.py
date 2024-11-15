from adafruit_circuitplayground import cp
import time

while True:
      if cp.switch:
            cp.pixels.fill((0, 0, 0))
            for i in range(0, 5):
                  cp.pixels[i] = ((0, 1, 0))
      else:
            cp.pixels.fill((0, 0, 0))
            for i in range(6, 10):
                  cp.pixels[i] = ((0, 1, 0))     
                  

      

