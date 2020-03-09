# ConsolePy
A game and graphics development module for the console [WORK IN PROGRESS]
You don't have to install anything, just download the consolepy.py file and import it into your project!


<h3>Docs</h3>

<hr>
<strong>consolepy.update()</strong><br>
Renders the screen, clears the console and draws the new frame.
<br>

<hr>
<strong>consolepy.dist()</strong><br>
<p>Arguments:</p>
<p> - dist(x1, y1, x2, y2)</p>
<p> - dist(x1, y1, z1, x2, y2, z2)</p>
Returns the distance between 2 points
<br>

<hr>
<strong>consolepy.set_fill()</strong><br>
<p>Arguments:</p>
<p> - set_fill(r, g, b)</p>
<p> - set_fill(col)</p>
Sets the color of the background, takes either a RGB value or a single value to be used as rgb, e.g set_fill(51) == set_fill(51, 51, 51)
<br>
<br>

<hr>
<strong>consolepy.draw_point()</strong><br>
<p>Arguments:</p>
<p> - draw_point(x, y, r, g, b)</p>
<p> - draw_point(vec)</p>
draws a single point at coordinate x, y or at the Vector pos
<br>
<br>

<hr>
<strong>consolepy.draw_line()</strong><br>
<p>Arguments:</p>
<p> - draw_line(x1, y1, x2, y2, r, g, b)</p>
<p> - draw_line(vec1, vec2, r, g, b)</p>
draws a line from either x1, y1 to x2, y2 or Vector pos1 to Vector pos2
<br>
<br>

<hr>
<strong>consolepy.Vector()</strong><br>
<p>Arguments:</p>
<p> - Vector(x, y)</p>
<p> - Vector.random2D()</p>
A data structure that holds an X and Y position
<br>
<br>
