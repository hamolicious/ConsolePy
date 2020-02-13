# ConsolePy
A game and graphics development module for the console [WORK IN PROGRESS]

Main code (will look roughly the same every time)
```python3
# boiler plate code
screen = consolepy()
screen.init()

# setup a screen
w, h = 42, 40
screen.size(w, h)

# preset the background fill params
screen.set_fill('  ', 97)
while True:

  """ main code goes in this loop """

  # clears the current frame in the console
  screen.clear()
  # draws the new frame
  screen.update()
```

<h3>Quick Docs</h3>

If exact colors are needed, <a href="https://github.com/jonasjacek">jonasjacek</a> has an awesome resource over <a href="https://jonasjacek.github.io/colors/">here</a> providing you with the XTerm codes for all the possible colors

Controll Methods:
<li>init()</li>
sets up the module to be used
<li>size(frameWidth, frameHeight)</li>
defines the size for the frame to be rendered with
<li>set_fill(characterToFillWith, XTermColorCode)</li>
sets the background color and character fill when clearing the frame
<li>update()</li>
draws the next frame to screen
<li>clear()</li>
clears the previous frame from the screen
<li>draw_point(x, y, char, xterm)</li>
draws a single character "char" to the screen at x, y coordinates
<li>draw_line(x1, y1, x2, y2, char, xterm)</li>
draws a line from x1, y1 to x2, y2 using the "char" character
<li>draw_rect(x, y, w, h, char, xterm, fill=False)</li>
draws rectange at x, y with a size of w and h, optional parameter "fill" to choose if to fill the shape
<li>draw_circle(x, y, r, char, xterm, fill=False)</li>
draws a circle at x, y with a radius of r, optional parameter "fill" to choose if to fill the shape

