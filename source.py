#! /usr/bin/python3 

import keyboard_manager
import display
import db

kb = keyboard_manager.KBHit()

if __name__ == '__main__':
    display.init()
    while(True):
        if(kb.kbhit()):
            print(ord(kb.getch()))