from sense_hat import SenseHat
import time
sense = SenseHat()

wht = (250, 250, 250)
zero = (0, 0, 0)
red = (250, 20, 20)
skin = (232, 107, 75)
blue = (30, 70, 255)
black = (50, 15, 3)

pos1 = [
    zero, zero, red, red, red, red, zero, zero,
    zero, zero, red, red, red, wht, red, zero,
    zero, zero, skin, skin, skin, blue, zero, zero,
    zero, zero, skin, skin, skin, skin, zero, zero,
    zero, red, blue, red, red, blue, red, zero,
    zero, skin, blue, blue, blue, blue, skin, zero,
    zero, zero, blue, blue, blue, blue, zero, zero,
    zero, zero, skin, zero, zero, skin, zero, zero,
    ]

pos2 = [
    zero, zero, skin, skin, skin, blue, zero, zero,
    zero, zero, skin, skin, skin, skin, zero, zero,
    skin, red, blue, red, red, blue, red, skin,
    zero, zero, blue, blue, blue, blue, zero, zero,
    zero, zero, blue, blue, blue, blue, zero, zero,
    zero, skin, zero, zero, zero, zero, skin, zero,
    zero, zero, zero, zero, zero, zero, zero, zero,
    zero, zero, zero, zero, zero, zero, zero, zero
    ]


while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "down":
                sense.set_pixels(pos1)
            elif event.direction == "up":
                sense.set_pixels(pos2)
    


    

