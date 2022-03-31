from cmd_pkg import Getch
import os
#import keyboard


def less(**kwargs):
  params = kwargs.get('params', [])
  head = 0
  tail = 44
  # set back to 44
  for file in params:
    with open(params[0], "r") as f:
      lines = f.read().splitlines()

      # getch func
      #   if up arrow pressed head-- && tail--
      #   if down arrow pressed tail++ && head++
  for line in lines[head:tail]:
    print(line)

  getch = Getch()
  while True:
      char = getch() 
      if char == 'q':
        break
      if char in '\x1b':                # arrow key pressed
        null = getch()                  # waste a character
        direction = getch()             # grab the direction

        # one line up with up arrow
        if direction in 'A': # up arrow 
            if head > 0:
              os.system('clear')
              head-=1
              tail-=1
              for line in lines[head:tail]:
                print(line)

###########################################################################
           # One page up ASK DR. GRIFFIN
        # if direction in 'SPACEBAR': # up arrow 
        #     if head > 0:
        #       os.system('clear')
        #       head-=1
        #       tail-=1
        #       for line in lines[head:tail]:
        #         print(line)
        

            # print the previous line
        # one line down with down arrow
        elif direction in 'B':
          #file_eof = lines.read()
          if tail < len(lines):
            os.system('clear')
            head+=1
            tail+=1
            for line in lines[head:tail]:
              print(line)
          else: 
            head = head
            tail = tail
          # print the next line


      # elif keyboard.is_pressed(' '):
      #   #file_eof = lines.read()
      #   if tail < len(lines):
      #     os.system('clear')
      #     head+=10
      #     tail+=10
      #     for line in lines[head:tail]:
      #       print(line)
      #   else: 
      #     head = head
      #     tail = tail
        

if __name__=='__main__':
  less(params = ['Moby_Dick.txt'])





