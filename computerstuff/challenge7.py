from adafruit_circuitplayground import cp
import time

while True:
    x, y, z, = cp.acceleration
    import random#i know theres much better ways to do this but i dont care
    random1 = random.randint(0, 255)
    random2 = random.randint(0, 255)
    random3 = random.randint(0, 255)
    random4 = random.randint(0, 255)
    random5 = random.randint(0, 255)
    random6 = random.randint(0, 255)
    random7 = random.randint(0, 255)
    random8 = random.randint(0, 255)
    random9 = random.randint(0, 255)
    random10 = random.randint(0, 255)
    random11 = random.randint(0, 255)
    random12 = random.randint(0, 255)
    random13 = random.randint(0, 255)
    random14 = random.randint(0, 255)
    random15 = random.randint(0, 255)
    random16 = random.randint(0, 255)
    random17 = random.randint(0, 255)
    random18= random.randint(0, 255)
    random19= random.randint(0, 255)
    random20= random.randint(0, 255)
    random21= random.randint(0, 255)
    random22= random.randint(0, 255)
    random23= random.randint(0, 255)
    random24= random.randint(0, 255)
    random25= random.randint(0, 255)
    random26= random.randint(0, 255)
    random27= random.randint(0, 255)
    random28= random.randint(0, 255)
    random29= random.randint(0, 255)
    random30= random.randint(0, 255)



    shake_threshold = 15.0
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        cp.pixels[0] = [random1, random2, random3]
        cp.pixels[1] = [random4, random5, random6]
        cp.pixels[2] = [random7, random8, random9]
        cp.pixels[3] = [random10, random11, random12]
        cp.pixels[4] = [random13, random14, random15]
        cp.pixels[5] = [random16, random17, random18]
        cp.pixels[6] = [random19, random20, random21]
        cp.pixels[7] = [random22, random23, random24]
        cp.pixels[8] = [random25, random26, random27]
        cp.pixels[9] = [random28, random29, random30]

         
