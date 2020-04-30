#! /usr/bin/python3 

import keyboard_manager
import display
import db

# Initial a keyboard manager
kb = keyboard_manager.KBHit()

#Initial display
display.init()

# screen_size
screen_size = (40, 16)

# main menu options
main_menu = [
    "   Start   ",
    "Score Board",
    "   Exit    "
]

# This function Draws an empty frame, with give color,
# frame could be centered or sticked top left corner by sellecting pos
# pos:1 is centered , and otherwise sticks at top left corner
def draw_frame(w, h, pos=1, bg='blue'):
    
    a = (1,1)
    b = (w,h)
    
    if(pos == 1):
        s_w = int(screen_size[0]/2)
        s_h = int(screen_size[1]/2)
        w = int(w/2)
        h = int(h/2)
        a = (s_w - w, s_h - h)
        b = (s_w + w, s_h + h) 
    
    display.draw_rectangular(a, b, color='red', bg_color=bg, intensity='bright')

# Main menu drawer
# If user changes the selected menue, the ">" char, changes and shows the selected menu
def draw_menu(select=0):
    w = 0
    for i in main_menu:
        w = max (w, len(i))
    w = w + 2
    w = int(w/2)
    h = int(len(main_menu)/2)
    s_w = int(screen_size[0]/2)
    s_h = int(screen_size[1]/2)
    
    x = s_w - w
    y = s_h - h
    
    for i in range(len(main_menu)):
        msg = ' ' + main_menu[i] + ' '
        if(select==i):
            msg = ">" + msg[1:]   
        display.print_XY(msg,x,y+i,bg_color='red',color='yellow', intensity="bright")

# Keypad mapper
# I could make it better and have a variable keys that can be setup my user,
# just like control settings in other games, but its fine for now 
def get_key(key):
    
    if(key == "W" or key == "w"):
        return 0x01
    elif(key == "S" or key == "s"):
        return 0x02
    elif(key == "A" or key == "a"):
        return 0x03
    elif(key == "D" or key == "d"):
        return 0x04
    elif(key == "\n" or key == "\n"):
        return 0x05
    elif (key == 'p' or key == 'P'):
        return 0x06
    elif (key == "q" or key == "Q"):
        return 0x07
    return 0x00

# to be continued
def action(state, key):
    pass

# Main function
if __name__ == '__main__':
    display.clear_screan()
    draw_frame(screen_size[0], screen_size[1])
    # Currnet state, i defined it here to protect it against other methods that could not make any changes to it. 
    state = 0
    
    #menu state
    menue_state = 0
    
    # other privte methods the we only want nobody could access them
    # like : snake possition, spawned foods, walls
    snake = []
    food = []
    walls = []
    
    draw_menu(menue_state)
    
    # Main game loop, it will quit only when you select quit on any stage
    while(True):    
        # delay(200);
        # if user pressed a key
        if(kb.kbhit()):
            # read that input
            c = kb.getch()
            # see what key is this
            key = get_key(c)
            # what to do, what not do? this is the problem.
            act = action(state, key)
            
    # the game is ended, set terminal settings to normal
    kb.set_normal_term()
    
    # close any oppend files
    #db.close()
    
    # now safely exit
    #exit(0)
    
    