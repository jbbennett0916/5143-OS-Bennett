"""
The cd command will change the current working directory that you are in. However there is a bug if you cd .. from the start. We cannot move forward back to our home directory.
"""


import os
from os.path import expanduser

def cd(**kwargs):
  params = kwargs.get("params", " ")
  # if ..  go back one directory
  if '..' in params:
    os.chdir(os.path.dirname(os.getcwd()))


  # if params
  elif params:
    # cast our params[0] to a string
    str_params = str(params[0])
    # check to see if the path exists
    if os.path.exists(str_params):
      # check to see if it is a directory
      if os.path.isdir(str_params):
        # change to the directory
        os.chdir(str_params) 
    else:
      #
      return("Path does not exist")
  print(os.getcwd())