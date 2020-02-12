from consolepy import *
from time import sleep
from random import randint

screen = consolepy()
screen.init()

w, h = 80, 40
screen.size(w, h)

screen.set_fill('  ', 0)
while True:

    screen.draw_circle(w/2, h/2, 10, '  ', 7, True)

    screen.clear()
    screen.update()
    sleep(0.3)
    quit()

















