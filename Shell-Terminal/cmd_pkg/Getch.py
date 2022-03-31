"""
Getch will capture characters when typed from the keyboard.
It will also utilize the print command function below to print each character being captured from Getch.
"""

import os
import sys
from time import sleep

class Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): 
        return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def print_cmd(cmd):
    """ This function "cleans" off the command line, then prints
        whatever cmd that is passed to it to the bottom of the terminal.
    """
    padding = " " * 80
    sys.stdout.write("\r"+padding)
    sys.stdout.write("\r"+prompt+cmd)
    sys.stdout.flush()


if __name__ == '__main__':
  getch = Getch()                             # create instance of our getch class
  
  prompt = "%:"                               # set default prompt

  cmd = ""                                # empty cmd variable

  print_cmd(cmd)                          # print to terminal
  
  while True:                             # loop forever

      char = getch()                      # read a character (but don't print)

      if char == '\x03' or cmd == 'exit': # ctrl-c
          raise SystemExit("Bye.")
      
      elif char == '\x7f':                # back space pressed
          cmd = cmd[:-1]
          print_cmd(cmd)
          
      elif char in '\x1b':                # arrow key pressed
          null = getch()                  # waste a character
          direction = getch()             # grab the direction
          

      elif char in '\r':                 # return pressed 
                         
              
          cmd = ""                        # reset command to nothing (since we just executed it)

          print_cmd(cmd)                  # now print empty cmd prompt
      else:
          cmd += char                     # add typed character to our "cmd"
          print_cmd(cmd) 