import os
import stat
import pwd
import math
# from pwd import getpwuid
import grp
from pathlib import Path

# gets the username for the -l flag
def get_user_name(filename):
  return pwd.getpwuid((os.stat(filename).st_uid)).pw_name

# gets the group name for the -l flag
def get_group_name(filename):
  return grp.getgrgid((os.stat(filename).st_gid)).gr_name


# convert the size of the bytes into kilo / megabytes
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 B"
    size_name = ("B", "KB", "MB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    # 1024 to the power of i
    p = math.pow(1024, i)
    # returns a floating point number to 2 decimal places
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def ls (**kwargs):
  
  # # get the current path
  direct_in = kwargs.get('params', [])
  if isinstance(direct_in,list) and len(direct_in) == 0:
    direct_in = '.'
  else:
    direct_in = direct_in[0]
    if not os.path.isdir(direct_in):
      #print("wtf?!?!")
      return None

    
  # get the flags
  flags = kwargs.get('flags', None)

  # check for valid path
  if os.path.isdir(direct_in):
    file_list = os.listdir(direct_in)
    #print("Valid directory")
  # checks for invvalid path
  else:
    print("Invalid direcory error")
    return "Invalid direcory error"

  file_list.sort()
  # if -a is not in flags
  if flags and 'a' not in flags:
    newfile = []
    for files in file_list:
      #print(files)
      if not files.startswith('.'):
        newfile.append(files)
    file_list = newfile
   #print(file_list)

  # if only the -a flag is given
  if len(flags) == 2 and 'a' in flags:
    for files in file_list:
      print(files)

    else:
      for files in file_list:
        pass

  # if no flags are given   
  if not flags:
    newfile = []
    for files in file_list:
      #print(files)
      if not files.startswith('.'):
        newfile.append(files)
    file_list = newfile
    #print(file_list)
    for file_name in file_list: 
      print(file_name)


  # for -l flag
  # if l_flag:
  if flags and 'l' in flags:
    # create a list for each of the columns
      # list for file permissions
    permission=[]
    # list for file amount of links
    links = []
    # list for file users
    users=[]
    # list for file groups
    group=[]
    # list for file sizes
    size=[]
    # list for file names
    name = []

    # make it in range of the lenght of the list, 
    for files in range (len(file_list)):
      #owner,group = groupOwner(files)
      # list of each files permissions
      permission.append(stat.filemode(os.stat(file_list[files]).st_mode))
      # list of each files links
      links.append(str(os.stat(file_list[files]).st_nlink))
      # list of each files user
      users.append(get_user_name(file_list[files]))
      # list of each files group 
      group.append(get_group_name(file_list[files]))

      # only if the -h flag is given to make it human readable
      if 'h' in flags:
        size.append(convert_size(os.stat(file_list[files]).st_size))
        #print(size)
      else:
        size.append(os.stat(file_list[files]).st_size)
        #print(size)

      name.append(file_list[files])
      #print(name)

    # because we want to return a string we will need to add each individual files index (ex) permission, name, g-name, u-name, size, etc..)

    for files in range(len(file_list)):
      # add permission to the file information string
      file_info = permission[files]
      # add permission to the file information string
      # cast to a str to concat to the string file info
      file_info = file_info + "  " + str(links[files]) 
      # add the users name to the string
      file_info = file_info + "  " + users[files]
      # add the group name to the string
      file_info = file_info + "  " + group[files]
      # add the size to the string need to cast it to string to add to file_info
      file_info = file_info + "  " + str(size[files]).rjust(8)


      #########################
      ### THE DATE SHOULD BE ADDED HERE IF TIME
      #########################

      # add the file name to the string
      file_info = file_info + "  " + name[files]
      print(file_info)






if __name__=='__main__':
  #print(ls(direct_in = '.', flags = ''))## if no flags are given #--> works
  #print(ls(direct_in = '.', flags = 'l'))## if l flag given, #--> works
  #print(ls(direct_in = '.', flags = 'a'))## if a flag given, #--> works
  #print(ls(direct_in = '.', flags = 'lh'))## if lh flags given, #--> works
  print(ls(direct_in = '.', flags = 'a'))## if lah flags given, #--> works

