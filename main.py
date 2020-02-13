from consolepy import *
from time import sleep
from random import randint, choice

# boiler plate code
screen = consolepy()
screen.init()

# setup a screen
w, h = 42, 40
screen.size(w, h)

# preset the background fill params
screen.set_fill('  ', 97)

""" cookie creater """

screen.draw_circle(w/2, h/2, 15, '  ', 136, True)
screen.draw_circle(w/2, h/2, 16, '  ', 135)

for i in range(h):
    for j in range(w):
        try:
            if screen.to_render[f"{j}:{i}"] == color(136, '  ') and randint(0, 10) == 1:
                screen.draw_point(j, i, '  ', randint(1, 200))
        except KeyError:
            pass

screen.clear()
screen.update()
















