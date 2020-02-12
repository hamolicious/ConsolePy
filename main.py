from consolepy import *
from time import sleep

screen = consolepy()
screen.init()

w, h = 100, 40
screen.size(w, h)

screen.set_fill('_', 22)

x = w/2
y = h/2

xvel = 1.2
yvel = 1.5


while True:
    screen.draw_line(w/2, h/2, x, y, '+', 60)
    screen.draw_point(x, y, '0', 5)

    x += xvel
    y += yvel

    if x <= 0:
        xvel *= -1
    if y <= 0:
        yvel *= -1
    if x >= w-1:
        xvel *= -1
    if y >= h-1:
        yvel *= -1

    screen.clear()
    screen.update()
    sleep(0.3)

















