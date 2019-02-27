from sense_hat import SenseHat
import time
import numpy as np
sense = SenseHat()

off = (0,0,0)
on = (20, 175, 255)

tiny = [
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, on, on, off, off, off,
        off, off, off, on, on, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
    ]

small = [
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
        off, off, on, on, on, on, off, off,
        off, off, on, off, off, on, off, off,
        off, off, on, off, off, on, off, off,
        off, off, on, on, on, on, off, off,
        off, off, off, off, off, off, off, off,
        off, off, off, off, off, off, off, off,
    ]

medium = [
        off, off, off, off, off, off, off, off,
        off, on, on, on, on, on, on, off,
        off, on, off, off, off, off, on, off,
        off, on, off, off, off, off, on, off,
        off, on, off, off, off, off, on, off,
        off, on, off, off, off, off, on, off,
        off, on, on, on, on, on, on, off,
        off, off, off, off, off, off, off, off,
    ]

large = [
        on, on, on, on, on, on, on, on,
        on, off, off, off, off, off, off, on,
        on, off, off, off, off, off, off, on,
        on, off, off, off, off, off, off, on,
        on, off, off, off, off, off, off, on,
        on, off, off, off, off, off, off, on,
        on, off, off, off, off, off, off, on,
        on, on, on, on, on, on, on, on,
    ]


for i in range(5):
    sense.set_pixels(tiny)
    time.sleep(0.3)
    sense.set_pixels(small)
    time.sleep(0.3)
    sense.set_pixels(medium)
    time.sleep(0.3)
    sense.set_pixels(large)
    time.sleep(0.3)
    sense.set_pixels(medium)
    time.sleep(0.3)
    sense.set_pixels(small)
    time.sleep(0.3)
    sense.set_pixels(tiny)
    time.sleep(0.3)
    sense.clear()
    time.sleep(0.2)
