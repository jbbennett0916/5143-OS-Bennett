import os
import shutil
import glob



# def rmdir(flags=[], params=[], redirects=None):
#   files = glob.glob('*.txt')
#   print(files)
#   print(os.getcwd())
#   delpath = os.path.join(os.getcwd(), params[0])
#   print(delpath)
#   print(os.path.isdir(delpath))
#   print(os.path.isfile(delpath))
#   #os.removedirs(params[0])

def rmdir(**kwargs):
  params = kwargs.get("params", None)
  files = glob.glob('*.txt')
  print(files)
  print(os.getcwd())
  delpath = os.path.join(os.getcwd(), params[0])
  print(delpath)
  print(os.path.isdir(delpath))
  print(os.path.isfile(delpath))
  #os.removedirs(params[0])

  

  # # will remove a file
  # os.remove(params[0])
  # # will remove an empty folder
  # os.removedirs(params[0])
  # # will remove a folder with files inside of it
  # shutil.rmtree(params[0])
  '''
    3 if statements to check if it is a file, folder, or a folder with files  
  '''
  
  #os.chdir(cwd)
  
# def rm2(flags, params, redirects):
#   # if the -r flag is given
#   if flags:
#     if flags[0] == '-r':
#       # delete recursively
#       shutil.rmtree(params[0])
#       print(params[0], "was deleted")

#   else:
#     # give an error if no file is given
#     if not params:
#       print("Error: Please enter a file name after rm.")

#     else:
#       # file name will be the first index in the list
#       filename = params[0]
#       # get the current working directory of the file
#       base = os.getcwd()

#       # check to see if it is a wildcard
#       if "*" in filename:
#         substring = filename [1:]
#         for file in os.listdir(base):
#           if file.endswith(substring):
#             # join the basename and file together then remove
#             os.remove(os.path.join(base, file))
#             print(file, "was deleted")


#       else:
#         index = 0
#         for p in params:
#           # check for all the paths in params and remove them
#           if os.path.exists(params[index]):
#             os.remove(params[index])
#           else:
#             print("Error The file does not exist.")
#         index+=1
#   return



if __name__ == '__main__':
  

  #rm("", "", "") # no parameter given
  #rm("", ["file1.txt"], "") # incorrect filename given
  #rm("-r", path, "")
  #rm("", ["file1.txt"], "") ##--> works
  #rm(["-r"], ['folderWfiles'], "") ##--> works
  #rm("", ["*file.txt"], "") ##--> works

  rmdir("", ["folderWOfiles"], "") ##--> works
