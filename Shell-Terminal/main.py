from cmd_pkg import cat
from cmd_pkg import chmod
from cmd_pkg import cp
from cmd_pkg import cd
from cmd_pkg import Getch
from cmd_pkg import grep
from cmd_pkg import head
from cmd_pkg import history
from cmd_pkg import hist_num
from cmd_pkg import less
from cmd_pkg import ls
from cmd_pkg import mkdir
from cmd_pkg import mv
from cmd_pkg import pwd
from cmd_pkg import rm
from cmd_pkg import rmdir
from cmd_pkg import sort
from cmd_pkg import tail
from cmd_pkg import wc
from cmd_pkg import who
from cmd_pkg import parseRawCmd

# from Cat import cat
# from Chmod import chmod
# from Cp import cp
# from Grep import grep
# from Head import head
# from History import history
# from Less import less
# from Ls import ls
# from Mkdir import Mkdir
# from Pwd import Pwd
# from Rm import rm
# from Rmdir import rmdir
# from WordCount import wc
import os,sys
from colorama import Fore, Style
from time import sleep


prompt = "%:"                               # set default 

def executeCommand(**kwargs):
  """Gets command flags and params and decides which function to call
  Returns:
      string: result of command
  """
  cmdsList = kwargs.get("cmdsList",None)

  for command in cmdsList:
    cmd = command["cmd"]
    params = command.get("params", [])
    flags = command.get("flags", [])

    #print(cmd)

  
  commands = {}
  commands['!'] = hist_num
  commands['ls'] = ls
  commands['cat'] = cat
  commands['pwd'] = pwd
  commands['less'] = less
  commands['history'] = history
  commands['wc'] = wc
  commands['grep'] = grep
  commands['cp'] = cp
  commands['cd'] = cd
  commands['head'] = head
  commands['chmod'] = chmod
  commands['mkdir'] = mkdir
  commands['rm'] = rm
  commands['rmdir'] = rmdir
  commands['tail'] = tail
  commands['mv'] = mv
  commands['sort'] = sort
  commands['who'] = who
  
  
  
  result = commands[cmd](params=params, flags=flags)

  return result


def print_cmd(cmd):
  """ This function "cleans" off the command line, then prints
      whatever cmd that is passed to it to the bottom of the terminal.
  """

  size = os.get_terminal_size()
  #print(size)
  padding = " " * 40
  sys.stdout.write(Fore.RED +"\r"+padding + Style.RESET_ALL)
  sys.stdout.write(Fore.GREEN + "\r"+prompt+cmd + Style.RESET_ALL)
  sys.stdout.flush()

  
getch = Getch() 

if __name__ == '__main__':
  
  # create instance of our getch class
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
          
          if direction in 'A':            # up arrow pressed
              # get the PREVIOUS command from your history (if there is one)
              # prints out '↑' then erases it (just to show something)
              # you should show last command in history
              cmd += '↑'
              #print_cmd(cmd)
              
          if direction in 'B':            # down arrow pressed
              # get the NEXT command from history (if there is one)
              # prints out '↓' then erases it (just to show something)
              # if i'm already up in history, then show next command otherwise
              # if I'm not in history do nothing
              cmd += '↓'
              #print_cmd(cmd)
          
          if direction in 'C':            # left arrow pressed    
              # move the cursor to the LEFT on your command prompt line
              # prints out '←' then erases it (just to show something)
              cmd += '←'
              cmd = cmd[:-1]
              #print_cmd(cmd)

          if direction in 'D':            # right arrow pressed
              # moves the cursor to the RIGHT on your command prompt line
              # prints out '→' then erases it (just to show something)
              cmd += '→'
              #print_cmd(cmd)
          
          print_cmd(cmd)                  # print the command (again)

      elif char in '\r':                  # return pressed 
          
          # This 'elif' simulates something "happening" after pressing return
          #cmd = "Executing command...."   # 
          # you call the correct function after you parse the command
         # parse me here 
        #"history.log"
          print_cmd(cmd) 
          
          file_path = os.path.abspath(os.path.join("/Users/jordanbennett/desktop/Shell-Terminal", ".", "history.log"))
          with open(file_path, 'a+') as g:
            g.write(cmd)
            g.write('\n')
          parsed = parseRawCmd(cmd)
          print()
          #print(parsed)
          executeCommand(**parsed)

            
        
          cmd = ""                        # reset command to nothing (since we just executed it)

          print_cmd(cmd)                  # now print empty cmd prompt
      else:
          cmd += char                     # add typed character to our "cmd"
          print_cmd(cmd)                  # print the cmd out

