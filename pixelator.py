from sense_hat import SenseHat
import numpy as np
import time

s = SenseHat()
s.clear()

counter = 0
x = 0
y =0

while x < 8:
    for x in range(0,8):
        for y in range(0,8):
            ran_col = list(np.random.choice(range(256), size=3))
            s.set_pixel(y, x, ran_col)
            time.sleep(0.2)
            s.clear()
