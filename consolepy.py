from os import system
from math import sqrt

class consolepy_error(Exception):
    """ Base class for all errors """
    pass

class NeedToInit(consolepy_error):
    """ Raised when the user has not initialised the module """
    pass

def color(xterm, char):
    """ Formats the color to allow easier changes """
    return f'\u001b[48;5;{xterm}m' + str(char) + '\u001b[0m'

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

class consolepy():
    #### SETUP FUNCTIONS
    def init(self):
        """ Initialises the module """
        system('color')
        self.fill = color(0, ' ')
        self.to_render = {}

    def size(self, width, height):
        """ sets the size for the screen """
        self.width = width
        self.height = height

    def set_fill(self, char, xterm):
        """ chooses the color and char to fill background with """
        self.fill = color(xterm, char)

    #### CONTROLL FUNCTIONS
    def update(self):
        """ updates the screen and draws it to the console """
        screen = ''
        
        for i in range(self.height):
            screen += '\n'
            for j in range(self.width):
                if f'{j}:{i}' in self.to_render:
                    screen += self.to_render[f"{j}:{i}"]
                else:
                    screen += self.fill

        print(screen)
        self.to_render = {}

    def clear(self):
        system('cls || clear')

    #### DRAWING FUNCTIONS
    def draw_point(self, x, y, char, xterm):
        """ Draws a single character to screen """
        self.to_render[f"{int(x)}:{int(y)}"] = color(xterm, char)

    def draw_line(self, x1, y1, x2, y2, char, xterm):
        """ draws a line from a to b """
        # changes in x and y
        dx = x2 - x1
        dy = y2 - y1

        # magnitude
        mag = sqrt(dx**2 + dy**2)

        # normalise magnitude
        if mag == 0:
            return
        
        dx /= mag
        dy /= mag

        ttl = 100

        while dist(x1, y1, x2, y2) > 1:#int(x1) != x2 and int(y1) != y2:
            x1 += dx
            y1 += dy
            
            self.to_render[f"{int(x1)}:{int(y1)}"] = color(xterm, char)

            ttl -= 1
            if ttl <= 0:
                break
















