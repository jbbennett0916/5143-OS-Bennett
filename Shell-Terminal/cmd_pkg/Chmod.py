"""
The chmod command will change the permissions for a given
file/directory. To use it type the command chmod then 
three integers. Each integer is a binary number taking in 
three bits for the integer from 0 to 7
example: chmod 077 bananas
"""

import os, sys, stat

def chmod(**kwargs):
  params = kwargs.get('params', None)

  value = params[0]

  # This program first checks if the user wants to change a file using a number or
  # letter values. The letter values are chekced first, and then chmod by a number
  # is employed.
  
  # Allows changes for user
  if value[0] == "u":

    if value[1] == "+":

      if value[2] == "r":
        os.chmod(params[1], stat.S_IREAD)
        print("User can read file now.")

      elif value[2] == "w":
        os.chmod(params[1], stat.S_IWRITE)
        print("User can write to file now.")

      elif value[2] == "x":
        os.chmod(params[1], stat.S_IEXEC)
        print("User can execute file now.")

      elif value[2] == "a":
        os.chmod(params[1], stat.S_IRWXU)
        print("User can do everything now.")

      else:
        print("Incorrect Input.")
  
  # Allows changes for groups
  elif value[0] == "g":

    if value[1] == "+":
           
      if value[2] == "r":
        os.chmod(params[1], stat.S_IRGRP)
        print("Group can read file now.")

      elif value[2] == "w":
        os.chmod(params[1], stat.S_IWGRP)
        print("Groups can write to file now.")

      elif value[2] == "x":
        os.chmod(params[1], stat.S_IXGRP)
        print("Group can execute file now.")

      elif value[2] == "a":
        os.chmod(params[1], stat.S_IRWXG)
        print("Groups can do everything now.")

  # Allows changes for others
  elif value[0] == "o":

    if value[1] == '+':

      if value[2] == "r":
        os.chmod(params[1], stat.S_IROTH)
        print("Others can read file now.")

      elif value[2] == "w":
        os.chmod(params[1], stat.S_IWOTH)
        print("Others can write to file now.")

      elif value[2] == "x":
        os.chmod(params[1], stat.S_IXOTH)
        print("Group can execute file now.")

      elif value[2] == "a":
        os.chmod(params[1], stat.S_IRWXO)
        print("Others can do everything now.")      
      
  else:
    # os.chmod takes in octal values, so to use Linux format
    # we have to change our decimal value to octal.
    num = params[0]
    num = str(num)
    num = int(num, 8)
  
    os.chmod(params[1], num)

    # Tell the user the file permissions were changed.
    #print("File permissions for", params[1], " were changed!")

  return


if __name__=='__main__':

  # chmod(" ", ["777", "test.txt"], " ")
  # chmod(" ", ["777", "folder"], " ")

  chmod(params = ['077', 'random.txt'])