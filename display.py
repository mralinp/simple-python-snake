from colorama import init
from os import system


# text color map
color_map = {
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
# back ground map
bg_color_map = {
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

# intensity map
intensity_map = {
    'reset' : '0', 
    'bright' : '1', 
    'dim':'2', 
    'normal':'22'
    }

# print a char on arbitrary possition with arbitrary color, bg_color and intensity
def print_XY(msg, x=1, y=1, color='reset' , bg_color='reset', intensity='reset'):
    
    # possition the cursare on (x, y) porisstion
    s = '\033[' + str(y) + ';' + str(x) + 'H' 
    
    # set text color
    s = s +'\033[' + color_map[color] + 'm'
    
    # set background color
    s = s + '\033[' + bg_color_map[bg_color] + 'm'
    
    # set intensity
    s = s + '\033[' + intensity_map[intensity] + 'm'
    
    print(s+msg)
# clear whole the screan
def clear_screan():
    system('clear')
    
# prints a rectangle with given two corner diameter points a and b
#  a-----
#  |     | 
#  |_____b
def draw_rectangular(a, b, color='reset', bg_color='reset', intensity="reset"):
    for i in range(a[0], b[0]):
        for j in range(a[1], b[1]):
            print_XY(' ', i, j, color, bg_color, intensity)


if __name__ == "__main__" :
    init()
    clear_screan()
    draw_rectangular((1,1), (40, 15), 'red', 'blue', 'bright')