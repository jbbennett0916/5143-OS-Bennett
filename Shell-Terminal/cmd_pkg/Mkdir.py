import os
import rich

# when we type in mkdir (something) we want to create a new directory named (something)

##########  What I'm thinking  #########
#   if statement for: if cmd == mkdir
#   Use the os.path.abspath() method
#   Use the os.path.join() method
############################################


#########  What I think we will Need  #########
#   statement for if the file exists already
#   statement for if the file is invalid
#   statement for making valid file
#   
###################################################

path = '.'
# getting path
def absPath(path):
  the_path = os.path.abspath(path)
  return the_path
  
# making a new directory
"""
mkdir with abs path: /home/runner/blah
mkdir with relative path:
    temp == ./temp
    ../temp
    ../../temp
"""
# def MKDIR(dirName):
#     if not os.path.isdir(dirName):
#       # creates a new directroy of input name
#       os.mkdir(dirName)
#       # prints out the absolute path with new folder
#     print(os.path.abspath(dirName))
#     parts = dirName.split("/")
#     print(type(parts))
#     print(parts)
#     myBasePath = "/".os.path.join(parts[:-1])
#     print(type(myBasePath))
#     print(myBasePath)
  
    # return None

# def Mkdir(dirName):
#   if not os.path.isdir(dirName):
#     #os.mkdir(dirName)
#     new_path = os.mkdir(dirName)
#     return new_path
#   parts = new_path.split("/")
#   print(parts)
  

def mkdir(**kwargs):
  params = kwargs.get("params", None)
  dirName = params[0:]
  for dir_params in dirName:
    if not os.path.isdir(dir_params): #[dir_params]
      #os.mkdir(dirName) 
      new_path = os.mkdir(dir_params)
      #return new_path
    # parts = new_path.split("/")
    # print(parts)

# # making a new directory
# def MKDIR_with_statements():
#   new_cmd = {}
#   cmd = input("% ")
#   cmd = cmd.split()
#   # new_cmd['cmd'] = cmd[0]
#   # new_cmd['params'] = cmd[1]
#   # print(new_cmd)
#   if cmd[0] == 'mkdir':
#     new_path = os.mkdir(cmd[1])
#     if new_path == os.path.exists(os.path.join(os.getcwd(), 'new_path'))
#     print("File already exists")

#     else
#     return new_path

# print(absPath(path))
# MKDIR()

if __name__=='__main__':
  # print("what")
  # cmd = input("% ")
  # cmd = cmd.split()
  # if cmd[0] == 'mkdir':
  #   Mkdir(cmd[1])

  mkdir(params = 'newdirectory')