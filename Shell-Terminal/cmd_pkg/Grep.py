"""
The grep command searches a file or files for a string. When it finds a pattern that matches more than one file it will print the names of the files. 
"""

import re
import sys


def grep(**kwargs):

  params = kwargs.get("params", None)
  flags = kwargs.get("flags", None)   
  #params = kwargs.get('params')
  pattern = params[0]
  dirs = params[1:]
  for word in dirs:
    with open(word, 'r') as file:
        for params in file:
          if re.search(pattern,params):
            if not flags:      
              print(params)
            else:
              if len(dirs) >= 1 and dirs == dirs:
                dir_list = ""
                dir_list = " ".join(dirs)
                print(dir_list)
              
                break


if __name__ == '__main__':
  #print(grep(params = [['pwd'],["file3.txt"], ["Dick.txt"]]))
  #print(grep(**commands))
  # grep(params = [['donations'], ['Dick.txt']])
  # grep(params = [['donations'], ['Dick.txt']])
  grep(params = ['cat', 'f2.txt'])
  