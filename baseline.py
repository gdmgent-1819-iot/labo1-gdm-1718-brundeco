from sense_hat import SenseHat
import time
import numpy as np

sense = SenseHat()

r = 0
g = 0
b = 0

baseline = "Hello! We are New Media Development :)"

for i in range(3):
    
    rand_vals_tc = list(np.random.choice(range(110,255), size=3))
    rand_vals_bg = list(np.random.choice(range(80), size=3))

    sense.show_message(baseline, text_colour=rand_vals_tc, back_colour=rand_vals_bg)
    sense.clear((r,g,b))




