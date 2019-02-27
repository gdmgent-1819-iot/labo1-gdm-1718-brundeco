from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

r = 0
g = 0
b = 0

def thisNum(int):
    return random.randint(0,int)

for i in range(10):
    for x in range(4):
        for y in range(8):
            z = thisNum(1)
            if z == 0:
                sense.set_pixel(x, y, (50,50,50))
                sense.set_pixel((7-x), y, (50,50,50))
            if z == 1:
                sense.set_pixel(x, y, (220,80,250))
                sense.set_pixel((7-x), y, (220,80,250))
    sleep(1)
sense.clear((r, g, b))