#! /usr/bin/python3 

import keyboard_manager
import display
import db
from time import sleep
from random import choice, randint
# screen_size
screen_size = (40, 16)

# main menu options
main_menu = [
    "   Start   ",
    "Score Board",
    "   Exit    "
]
# a key map to say what key is deffining which direction
key_direction_map = {0x01 : (0, -1), 0x02: (0, 1), 0x03 : (-1, 0), 0x04 : (1, 0)}

# This function Draws an empty frame, with give color,
# frame could be centered or sticked top left corner by sellecting pos
# pos:1 is centered , and otherwise sticks at top left corner
def draw_frame(w, h, pos=1, bg='blue'):
    
    a = (1,1)
    b = (w+1,h+1)
    
    if(pos == 1):
        s_w = int(screen_size[0]/2)
        s_h = int(screen_size[1]/2)
        w = int(w/2)
        h = int(h/2)
        a = (s_w - w, s_h - h)
        b = (s_w + w + 1, s_h + h + 1) 
    
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

def draw_ingame_score(score):
    s ="Score: " + str(score)
    s = " " * (screen_size[0] - len(s)) + s
    display.print_XY(s, 1,screen_size[1]+1,"green", "reset", "bright")
    
# Keypad mapper
# I could make it better and have a variable keys that can be setup my user,
# just like control settings in other games, but its fine for now 
def get_key(key):
    # key_map = {0x01 : "UP", 0x02 : "DOWN", 0x03 : "LEFT", 0x04 : "RIGHT", 0x05 : "RET", 0x06 : "PAU", 0x07 : "QUI", 0x00 : "NOU"}
    ret = 0x00
    if(key == "A" or key == "w"):
        ret = 0x01
    elif(key == "B" or key == "s"):
        ret = 0x02
    elif(key == "D" or key == "a"):
        ret = 0x03
    elif(key == "C" or key == "d"):
        ret = 0x04
    elif(key == "\n"):
        ret = 0x05
    elif (key == 'p'):
        ret = 0x06
    elif (key == "q"):
        ret = 0x07
    else:
        ret = 0x00
    return ret

def init_game():
    display.clear_screen()
    draw_frame(screen_size[0], screen_size[1])
    draw_menu(0)

def start_game():
    display.print_XY("", 1, 1)
    display.clear_screen()
    draw_frame(screen_size[0], screen_size[1])
    for p in snake:
        display.print_XY("O", p[0], p[1], "red", "blue", "bright")
    for p in walls:
        display.print_XY("#", p[0], p[1], "red", "blue", "bright")
    for p in food:
        display.print_XY("A", p[0], p[1], "red", "blue", "bright")
    draw_ingame_score(score)


def printObj(c, pts, color = "reset", bg_color="reset"):
    for p in pts:
        display.print_XY(c, p[0], p[1], color, bg_color, "bright")

def show_score_board():
    print ("1")
    
def loser_check(snake, walls):
    if(snake[0] in snake[1:]):
        return True
    if(snake[0] in walls):
        return True
    
def gen_food(snake, wall, food):
    board = []
    for i in range(1, screen_size[0] + 1):
        for j in range(1, screen_size[1] + 1):
            board += [(i,j)]
    for i in snake:
        if(i in board):
            board.remove(i)
    for i in food:
        if(i in board):
            board.remove(i)
    for i in wall:
        if(i in board):
            board.remove(i)
    return choice(board)

def print_food(food):
    for f in food:
        display.print_XY("A", f[0], f[1], "yellow", "blue", "bright")
# Main function
if __name__ == '__main__':
    
    # Initial a keyboard manager
    # it changes the terminal settings
    kb = keyboard_manager.KBHit()
    
    #Initial display
    display.init()
    
    # Global state, i defined it here to protect it against other methods that could not make any changes to it.
    # {0 : init, 1 : start a game, 2 : scoreboard, 3: exit, 4 : running game...}
    g_state = 0x00
    
    # Main menu state
    m_state = 0x00
    
    # other privte methods we only want that nobody could access them
    # for example : snake possition, spawned foods, walls, ...
    snake = [(int(screen_size[0]/2) - i, int(screen_size[1]/2)) for i in range(4)]
    max_foods = 5
    food = []
    walls = []
    m_dir = (0, 0)
    score = 0
    
    # initialing game environment
    init_game()
    speed_counter = 0
    speed_counter_limit = 50
    food_gen_timer = 0
    # Main game loop
    while(True):
        # delay to save some cpu and could be playable
        sleep(0.001);
        # Some flags to detect actions
        # det is for input detection
        det = False
        # r_menu, refresh menu due to a change in state
        r_menu = False
        # n_state, we are in a new state so change the currnet state
        n_state = False
        # pressed key holder
        key = 0x00
        # if user pressed a key
        if(kb.kbhit()):
            # read that input
            c = kb.getch()
            # what was that key?
            key = get_key(c)
            # detected a command from user
            det = True
            
        if(det):
            # we are in the main menu
            if(g_state == 0):
                # UP
                if(key == 0x01):
                    m_state = (m_state - 1) % len(main_menu)
                    r_menu = True
                # DOWN
                elif(key == 0x02):
                    m_state = (m_state + 1) % len(main_menu)
                    r_menu = True
                # RET
                elif(key == 0x05):
                    g_state = m_state + 1
                    # we have a new globale state
                    n_state = True
                    
            # game has just started and by pressing a key snake starts to moving
            elif(g_state == 4):
                food_gen_timer = randint(500, 2000)
                if(key >= 0x01 and key <= 0x04):
                    g_state = 5
                    n_state = True
                # elif(key == 0x06):
                #     g_state = 6
                #     n_state = True
                # elif(key == 0x7):
                #     g_state = 7
                
            elif(g_state == 5):
                n_dir = key_direction_map[key]
                tmp = m_dir[0] + n_dir[0], m_dir[1] + n_dir[1]
                if(tmp[1] != tmp[0] or tmp[0] != 0):
                    m_dir = n_dir
                
            # elif(key == 0x06):
            #     g_state = 6
            #     n_state = True
            # elif(key == 0x7):
            #     g_state = 7
            #     n_state = True
                    
        if(r_menu):
            draw_menu(m_state)
            
        if(n_state):
            # start a new game
            if(g_state == 1):
                start_game()
                g_state = 4
            # show score board
            elif(g_state == 2):
                show_score_board()
            # exit selected
            elif (g_state == 3):
                break
            elif (g_state == 5):
                m_dir = key_direction_map[key]
                
        # if game is running move the snake
        # only move @ every 50 cycle 
        if(g_state == 5):
            if(speed_counter > speed_counter_limit):
                speed_counter = 0
                s = snake[0]
                s = s[0] + m_dir[0], s[1] + m_dir[1]
                if(s[0] > screen_size[0]):
                    s = 1, s[1]
                if(s[0] < 1):
                    s = screen_size[0]-1, s[1]
                if(s[1] > screen_size[1]):
                    s = s[0], 1
                if(s[1] < 1):
                    s = s[0], screen_size[1]-1
                p = snake[-1]
                snake = [s] + snake[:-1]
                # move head and remove tail
                display.swap('O', p, s, "red", "blue", "bright")
                draw_ingame_score(score)
            else:
                speed_counter = speed_counter + 1
            # if ate your tail you are a loser :)
            if(loser_check(snake, walls)):
                g_state = 6
            # if ate food then increase the tail long
            if(snake[0] in food):
                food.remove(snake[0])
                snake = snake + [snake[-1]]
                score = score + 50
            # generate a food if needed
            if(len(food) < 3):
                if(food_gen_timer < 0):
                    food += [gen_food(snake, walls, food)]
                    food_gen_timer = randint(500, 2000)
                    print_food(food)
                else:
                    food_gen_timer = food_gen_timer - 1
        # we are here now!
        if(g_state == 6):
            break
    # reset display settings
    display.print_XY("", 1, 1)
    display.clear_screen()
    
    # finally, set terminal settings to normal
    kb.set_normal_term()
    
    # close any oppend files
    #db.close()
    
    # now safely exit
    exit(0)
    
    