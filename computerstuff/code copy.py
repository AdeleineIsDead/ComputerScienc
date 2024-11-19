from adafruit_circuitplayground import cp
import time
while True:
    if cp.button.a:
        import random
        diceroll = random.randint(0, 10)
        if diceroll == 0:
            cp.pixels[0] = (0, 0, 1)
            cp.pixels[2] = (0, 0, 0)
            cp.pixels[3] = (0, 0, 0)
            cp.pixels[4] = (0, 0, 0)
            cp.pixels[5] = (0, 0, 0)
            cp.pixels[6] = (0, 0, 0)
            cp.pixels[7] = (0, 0, 0)
            cp.pixels[8] = (0, 0, 0)
            cp.pixels[9] = (0, 0, 0)
            cp.pixels[1] = (0, 0, 0)


    

         
