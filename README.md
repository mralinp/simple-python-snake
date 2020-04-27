# simple-python-snake
This is my first programming project, when i was a jounior studen at shiraz univesity (2015). 
I uploaded source code and some discriptions heres and, i hope this could help some people find what they need for their related school projects.

## project deffenition
Please write a simple snake game as you may seen on old Nokia phones or other old phones.
The game runs on a single page terminal and the size of the page is constant (i.e. 80*40).

A single snake moves around the game board witch is controlled by user, using arrows keys or 'W', 'A', 'S' and 'D' to move UP, LEFT, DOWN and RIGHT respectively.
by pressing 'Esc' key the game has to pause. you have to make a ability to store the highest score on the game or other arbitrary method such as storying each user score.

After a random time a single charachter food will deployed on a random spot of map and if snake eats that, its tail become longer.
Map can contain some walls or obstacles that, if snake hits them the game will finish and player loses the game. the game can end also when snake eats its own tail.

### bonuses

Any creativity to make the game looks friendly and more pleasant such as having a menu, several levels, or even it can have a story line(this must be a little hard but nothing is impossible, trust me my child).

## Colorama cheatSheet

```
Intensity:
ESC [ 0 m       # reset all (colors and brightness)
ESC [ 1 m       # bright
ESC [ 2 m       # dim (looks same as normal brightness)
ESC [ 22 m      # normal brightness

Foreground:
ESC [ 30 m      # black
ESC [ 31 m      # red
ESC [ 32 m      # green
ESC [ 33 m      # yellow
ESC [ 34 m      # blue
ESC [ 35 m      # magenta
ESC [ 36 m      # cyan
ESC [ 37 m      # white
ESC [ 39 m      # reset

Background:
ESC [ 40 m      # black
ESC [ 41 m      # red
ESC [ 42 m      # green
ESC [ 43 m      # yellow
ESC [ 44 m      # blue
ESC [ 45 m      # magenta
ESC [ 46 m      # cyan
ESC [ 47 m      # white
ESC [ 49 m      # reset

Cursor positioning:
ESC [ y;x H     # position cursor at x across, y down
ESC [ y;x f     # position cursor at x across, y down
ESC [ n A       # move cursor n lines up
ESC [ n B       # move cursor n lines down
ESC [ n C       # move cursor n characters forward
ESC [ n D       # move cursor n characters backward

Clear the screen:
ESC [ mode J    # clear the screen

Clear the line:
ESC [ mode K    # clear the line
```
