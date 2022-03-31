"""
The history command will print out the entire 
history to the output stream. We are still 
currently working on being able to output 
it to another inputted file.
"""

import os


def history(**kwargs):
  redirects = kwargs.get('redirects')
  # base path for directory
  #base = os.path.dirname(__file__)
  base = os.getcwd()
  #print(base)
  # the path to our history file
  file_path = os.path.abspath(os.path.join(base, ".", "history.log"))
  #print(file_path)
  count = 1
  hist_dict = {}

  with open(file_path, 'r') as f:
    for line in f.readlines():
      hist_dict[count] = line
      
      if not redirects:      
        print(f"{count}   {line}", end = '')
      count+=1

  if redirects:
    mode = redirects[0]
    write_file = redirects[1]
    with open(write_file, mode) as wf:
      for key in hist_dict:
        wf.write(f"{key}    {hist_dict[key]}")



if __name__ == '__main__':
  #history("", "", ['w', "f1.txt"])
  #history("", "", "")
  #history() ##--> print to the screen
  history(redirects = ['w','f3.txt']) ##--> writes to f3.txt