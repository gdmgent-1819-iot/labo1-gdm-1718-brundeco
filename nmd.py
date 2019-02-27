from sense_hat import SenseHat
import time
import numpy as np
sense = SenseHat()

r = 0
g = 0
b = 0

for i in range(5):
    
    color = list(np.random.choice(range(256), size=3))
    sense.show_letter('N', text_colour=color)
    time.sleep(1)
    
    color = list(np.random.choice(range(256), size=3))
    sense.show_letter('M', text_colour=color)
    time.sleep(1)

    color = list(np.random.choice(range(256), size=3))
    sense.show_letter('D', text_colour=color)
    time.sleep(1)
    
    sense.clear((r,g,b))
    time.sleep(2)
