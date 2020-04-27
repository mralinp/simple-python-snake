#! /usr/bin/python3 

# SIMPLE-PYTHON-SNAKE
# Practical level : elementry
# Project of Computer Sience Elementrys (CSE 101) 
# Teacher: Dr.Sardaldini.
# Head Ta: Eng H.moteallah
# Shiraz Uni Fall 2015 Semester first
# This code is uploaded on github @ Apr 2020.
# This project challengs were:
#   1.getting the async key or (non_blocking input), 
#   2.building a user friendly UI from scratch (Warnning. no high level modules allowed e.g wx-python, pygame, etc)
#   3.solve lagging (i.e 'display bliking')
#   (note. using modules like colorama is allowed for printing collored chars and positioning chars)
#   Project basics:
#   1.An snake with default lenght 5 at the beginnig. The snake have to move around.
#   2.An ASCI game map with some foods in.
#   3.By eating each food the snake lenghth is grown and the players score is increses with 100.
#   4.The game has to be non-blocking, smoth and has low and limmited memory usage.
#  Bounsus: 
#      1.handling char positioning with out using colorama or stuffs like that.
#      2.Any awesome idea about ui
#      3.having some levels in game with diffrent maps and defficulties

import sys
import os
from colorama import init
init()

t_color_map = {
    'black' : '30',
    'red': '31',
    'green' : '32',
    'yellow' : '33',
    'blue' : '34', 
    'magenta' : '35', 
    'cyan' : '36', 
    'white' : '37',
    'reset': '39'
    }

b_color_map = {
    'black' : '40',
    'red': '41',
    'green' : '42',
    'yellow' : '43',
    'blue' : '44', 
    'magenta' : '45', 
    'cyan' : '46', 
    'white' : '47',
    'reset': '49'
    }

intensity_map = {
    'reset' : '0', 
    'bright' : '1', 
    'dim':'2', 
    'normal':'22'
    }

board_size = (40 ,17)

snake = []
food = []
walls = []


# a function to print a text on an arbitrary possition
def print_XY(msg, x=1, y=1, t_color='reset' , b_color='reset', intensity='reset'):
    
    # possition the cursare on (x, y) porisstion
    s = '\033[' + str(x) + ';' + str(y) + 'H' 
    
    # set text color
    s = s +'\033[' + t_color_map[t_color] + 'm'
    
    # set background color
    s = s + '\033[' + b_color_map[b_color] + 'm'
    
    # set intensity
    s = s + '\033[' + intensity_map[intensity] + 'm'
    
    print(s+msg)

def clear_screan():
    os.system('clear')
    for i in range(1, board_size[0]):
        for j in range(1, board_size[1]):
            print_XY(' ', j, i, 'red', 'blue', 'bright')

def draw_window(width, height, color):
    for i in range(int(board_size[0]/2)-1, int(board_size[0]/2)+width):
        for j in range(int(board_size[1]/2)-1, int(board_size[1]/2) + height):
            print_XY(' ', j, i, 'reset', color, 'bright')



lose = False
direction = (0, 0)

# game loops
while (lose == False):
    for i in 
clear_screan()
draw_window(5,5, 'green')
a = input()

