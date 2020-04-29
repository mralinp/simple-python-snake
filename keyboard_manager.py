# !!! we have an issue with ESC key itself that must be solved first!

import os

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select


class KBHit:

    def __init__(self):
        if os.name == 'nt':
            pass
        else:
            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)


    def set_normal_term(self):
        # Resets to normal terminal.  On Windows this is a no-op.
        if os.name == 'nt':
            pass
        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        # Returns a keyboard character after kbhit() has been called.
        if os.name == 'nt':
            return msvcrt.getch().decode('utf-8')
        else:
            # read 1 byte, if this it's not a char key read 2 more bytes, otherwise return that char.
            # !!! there is an isssue here, ESC code is \x1b and arrow and Function keys start with ESC and 2 more bytes.
            # if i read 1 byte and it is a \x1b then it might be ESC key or an arrow key, What we can do now?
            # in debugging lets assume we dont have ESC for now.
            c = sys.stdin.read(1)
            if( c == '\x1b'):
                return sys.stdin.read(2)[1]
            return c

    def kbhit(self):
        # Returns True if keyboard character was hit, False otherwise.
        if os.name == 'nt':
            return msvcrt.kbhit()

        else:
            dr,dw,de = select([sys.stdin], [], [], 0)
            return dr != []
        
# Test    
if __name__ == "__main__":

    kb = KBHit()

    print('Hit any key, or ESC to exit')

    while True:

        if kb.kbhit():
            c = kb.getch()
            print(ord(c))

    kb.set_normal_term()