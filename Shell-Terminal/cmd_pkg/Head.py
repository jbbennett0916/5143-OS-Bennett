"""
The head command will print the first 10 lines of a given file by default without flags. 
If the -n flag is given with an integer(n) then that amount (n) number of lines is printed. 
"""

import os


def head(**kwargs):
  params = kwargs.get("params", None)
  flags = kwargs.get("flags", None)
  # if there are no flags
  if not flags:
    # set default amount to 10
    amount_lines = 10
    with open(params[0], "r") as f:
      lines = f.read().splitlines()

  
  elif '-n' in flags:
    # set amount_lines equal to the first parameter in our list params
    amount_lines = params[0]
    # cast the amount to an integer
    amount_lines = int(amount_lines)
    with open(params[1], 'r') as f:
      lines = f.read().splitlines()

  # else:
  #   print("Invalid input")

  # print each line in lines from the start to whatever amount_lines is equal to
  for line in lines[:amount_lines]:
    print(line)

if __name__ =='__main__':
  


  head(params = [25,'Moby_Dick.txt'], flags = ['-n'])
  head(params = ['Moby_Dick.txt'], flags = None)
  #head(params = ['vick.txt'], flags = None)