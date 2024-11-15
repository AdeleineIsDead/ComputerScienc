from adafruit_circuitplayground import cp
import time

while True:
      x, y, z = cp.acceleration
      if x > 5:
            cp.pixels.fill((0, 0, 0))
            for i in range(1, 4):
                  cp.pixels[i] = ((0, 1, 0))
      elif x < -5:
            cp.pixels.fill((0, 0, 0))
            for i in range(6, 9):
                  cp.pixels[i] = ((0, 1, 0))     
                  

      

