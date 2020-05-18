simple-python-snake
======
This is my first programming project, when i was a jounior studen at shiraz univesity (2015). 
I uploaded source code and some discriptions here and, i hope this could help some people find what they need for their related school projects.

Maybe there exists some bugs in this project but, because this is just an example for begginers and its onle for educational porpuses. In our case here it doesn't matter having some bugs for experiencing a smooth gameplay, confortable UI or etc. The only thing that matters in here, is you can see how to get things working for elementary school projects. Anyway if you've seen any issues, you can tell me to fix them.

![menu image](https://github.com/mralinp/simple-python-snake/blob/master/img1.png)
![game environment](https://github.com/mralinp/simple-python-snake/blob/master/img2.png)
## project deffenition
Please write a simple snake game as you may seen on old Nokia phones or other old phones.
The game runs on a single page terminal and the size of the page is constant (i.e. 80*40).

A single snake moves around the game board witch is controlled by user, using arrows keys or 'W', 'A', 'S' and 'D' to move UP, LEFT, DOWN and RIGHT respectively.

by pressing 'Esc' key the game has to pause. you have to make a ability to store the highest score on the game or other arbitrary method such as storying each user score.


> note: Due to some reasons, currently in this version of project default keys binds are not exactly those tolled us to be, for now the keys are as follows:
`Arrow keys` and `w a s d` for moving around, `q` to quit, `p` to pause and return for `select`. I'll fix the key binds and keyboard manager soon in addition key maps will be standardized as well.

After a random time a single charachter food will deployed on a random spot of map and if snake eats that, its tail become longer.
Map can contain some walls or obstacles that, if snake hits them the game will finish and player loses the game. the game can end also when snake eats its own tail.

### bonuses

Any creativity to make the game looks friendly and more pleasant such as having a menu, several levels, or even it can have a story line(this must be a little hard but nothing is impossible, trust me my child).

## How to run this?

first you have to install python3 and pip3 on your computer.

for example on ubuntu open a terminal and type:

```console
foo@bar:~$ sudo apt update
foo@bar:~$ sudo apt install git python3 python3-pip
```


After that install colorama library using pip3:

```console
foo@bar:~$ sudo pip3 install colorama
```

Now all of pre-requirements are installed, and you are ready to run the code.

if you are on linux type:

```console
foo@bar:~$ cd ~
foo@bar:~$ git clone https://github.com/mralinp/simple-python-snake.git
foo@bar:~$ cd simple-python-snake
foo@bar:~$ sudo chmod +x source.py
foo@bar:~$ ./source
```

Or just simply type:(on any platform)

```console
foo@bar:~$ python3 source.py
```

## Colorama
Colorama is responsible of positioning the charchters on the screen and change their color.
The example bellow showes how easily we can use it.

```python
from colorama import init
init()

# possition the cursor on column 12 and row 5 (\033[12;5H)
# set text color to red (\033[32m)
# set background color to blue (\033[44m)
# and with the intensity of bright (\033[1m)
# then print 'Some Text'.
print("\033[12;5H" + "\033[32m" + "\033[44m" + "Some text")
```
For more informations you can look at the [colorama cheatsheet](#colorama-cheatsheet) to find other stuffs and see the meaning of each ascii code.
And also this link could be helpful too: [PyPi Colorama](https://pypi.org/project/colorama/)


### Colorama CheatSheet

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

## Non-Blocking input
This project had another embeded challenge and that was getting async or Non-Blocking input from the terminal. here i used some advices from stack overflow, and changed some things myself and finaly wrote a new module to handel the inputs from the user. It's wasn't easy to undrestand what is going on there, at least for those days but now i see that was too easy, let me explain:

Any machine has a mechanism to handel the I\O devices, on our computers operating system is responsible of this so, when you want to use an I\O device like keyboard monitor, printer, hard disk, etc. you have to ask your OS to comunicate with the device for you. So you don't have to get inputs from keyboard directly , OS is your partner and you ask any thing from him. And also user cant get his inputs directly to you, he gives the inputs to the OS.

Any language has a system to charachter inputs from the OS, for example function `input()` in python. it gets the input from user and returns it as a string. the input method is implimented by using standard input output system library that is working with the operating system, in our case `python` when you want to get input from the OS the python developers defined that any character you type by the keyboard has to be echoed and the getting input task is finished just when you pressed the `return` on your keyboard, this is how function `input()` defined in python.

Now here we have an other senario, the user can press a key at any time he wants and we dont need to wait for him to press a key, so the code must keeps working and at any cycle or at any 5, 10, etc cycle, depends on code, it can check that if there is a new input or not, if there is a new one, do the appropriate job for it.

In this project `keyboard_manager.py` is my input method, it changes the terminal settings and makes it appropriate for our goal.
