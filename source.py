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
print('\033[31m' + 'Ali')

# sample print code
print('\033[10;25H\033[33m\033[40m' + 'some red text')
# reset defaults
print('\033[39m') 
# # A dict to define the change made on snakes possition while moving around.
# direction = {'UP':(0, +1), 'DOWN':(0, -1), 'LEFT':(-1, 0), 'RIGHT':(+1, 0)}

# GREEN = 0xff
# GRAY = 0x55
# RED = 0x33


# def print_XY(x, y, color=GRAY, h_color=GRAY):
#     print("")

# board_size = (80 ,40)

# snake = []
# food = []
# walls = []

# for i in walls:
#     print_XY(i, '#')

# for i in food:
#     print_XY(i, 'F')

# for i in snake:
#     print_XY(i, 'O', GREEN, RED)



