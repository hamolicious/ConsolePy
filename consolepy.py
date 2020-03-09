
from os import system
from math import sqrt, pi, sin, cos
from random import randint

## INITIALISATION FUNCTIONS
def get_colors():
    """ loads the colors """
    with open('colors.txt', 'r') as file:
        return file.readlines()

## CONTROLL FUNCTIONS
def update():
    global SCREEN, SCREEN_W, SCREEN_H
    """ clears and draws the screen """
    
    to_draw = ''
    for y in range(SCREEN_H):
        to_draw += '\n'
        for x in range(SCREEN_W):
            try:
                to_draw += SCREEN[f'{x}:{y}']
            except KeyError:
                to_draw += rgb_to_xterm(FILL)

    system('cls')
    print(to_draw)
    SCREEN = {}

## ASSISTIVE FUNCTIONS
def rgb_to_xterm(rgb):
    global COLORS
    """ return closest xterm version of rgb """
    r1, g1, b1 = rgb
    xterm = 0

    lowest = 100**10

    for i in range(len(COLORS)):
        xterm_check = int(COLORS[i].split(' ')[0])
        r2 = int(COLORS[i].split(' ')[1])
        g2 = int(COLORS[i].split(' ')[2])
        b2 = int(COLORS[i].split(' ')[3])

        if (dist := dist(r1, g1, b1, r2, g2, b2)) < lowest:
            lowest = dist
            xterm = xterm_check
        
    return f'\u001b[48;5;{xterm}m  \u001b[0m'

def dist(*args):
    if len(args) == 4:
        x1, y1, x2, y2 = args
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)
    elif len(args) == 6:
        x1, y1, z1, x2, y2, z2 = args
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        
## SETTINGS FUNCTIONS
def set_fill(*args):
    global FILL
    """ sets the background fill """

    if len(args) == 3:
        r, g, b = args
        FILL = (r, g, b)
    elif len(args) == 1:
        col = args
        FILL = (col, col, col)

## DRAWING FUNCTIONS
def draw_point(*args):
    global SCREEN
    """ draws a single point at xy """

    if len(args) == 5:
        x, y, r, g, b = args
    elif len(args) == 4:
        x, y = args[0].get_xy()
        r, g, b = args[1 : 4]
    
    col = rgb_to_xterm((r, g, b))

    SCREEN[f"{x}:{y}"] = col

def draw_line(*args):
    global SCREEN
    """ draws a line between x1y1 and x2y2 """

    if len(args) == 7:
        x1, y1, x2, y2, r, g, b = args
    elif len(args) == 5:
        x1, y1 = args[0].get_xy()
        x2, y2 = args[1].get_xy()
        r, g, b = args[2 : 5]

    point_to_point_dist = lambda : dist(x1, y1, x2, y2)

    col = rgb_to_xterm((r, g, b))

    dx = x2 - x1
    dy = y2 - y1

    dist = point_to_point_dist()

    dx /= dist
    dy /= dist

    while point_to_point_dist() > 1:
        SCREEN[f"{int(x1)}:{int(y1)}"] = col

        x1 += dx
        y1 += dy

## DATA STRUCTURES

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def random2D():
        xdir = randint(-100, 100)
        ydir = randint(-100, 100)

        dist = dist(0, 0, xdir, ydir)

        xdir /= dist
        ydir /= dist

        return Vector(xdir, ydir)

    def __str__(self):
        return f'X: {self.x}  |  Y: {self.y}'

    def get_xy(self):
        return (int(self.x), int(self.y))

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

    def sub(self, vec)
        self.x -= vec.x
        self.y -= vec.y

# initialise module
system('color')

global FILL, SCREEN, SCREEN_W, SCREEN_H, COLORS
COLORS = get_colors()
FILL = (0, 0, 0)
SCREEN = {}
SCREEN_W, SCREEN_H = 30, 30




















































