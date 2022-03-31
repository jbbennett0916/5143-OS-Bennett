"""
cp should copy an entire file or group of files
and should put all of the source content in another file
or create another file with all of the source content
"""

import os
import shutil


def cp(**kwargs):
  params = kwargs.get('params', None)
  source_file = params[0]
  destin_file = params[1]
  ###   If both files exist
  if os.path.exists(source_file):
    if os.path.exists(destin_file):
      dir_path = os.path.dirname(__file__)
      source_path = os.path.abspath(os.path.join(dir_path, source_file))
      destin_path = os.path.abspath(os.path.join(dir_path, destin_file))
      ###   print(source_path)      WORKS UP TO HERE
      ###   print(destin_path)      WORKDS UP TO HERE
      shutil.copyfile(source_file, destin_file)

    ###   If the destination file does not exist yet
    else:
      with open(destin_file,'a') as f:
        pass
      dir_path = os.path.dirname(__file__)
      source_path = os.path.abspath(os.path.join(dir_path, source_file))
      destin_path = os.path.abspath(os.path.join(dir_path, destin_file))
      # print(source_path)      #WORKS UP TO HERE
      # print(destin_path)      #WORKDS UP TO HERE
      shutil.copyfile(source_file, destin_file)
  else:
    print("Error {} does not exist.".format(source_file))


if __name__ == "__main__":
  # cp("f1.txt","f2.txt")  #--> Copies f1 content to f2
  # cp("f1.txt","f3.txt")  #--> Copies f1 to unmade f3
  # cp("DNE.txt", "DNE2.txt")  #--> Shows DNE because it does not exist

  #cp(source_file = 'f1.txt', destin_file = 'f2.txt')
  #cp(source_file ="f1.txt",destin_file = "f3.txt")  #--> Copies f1 to unmade f3
  #cp(source_file ="output1.txt", destin_file = "DNE2.txt")  #--> Shows DNE because it does not exist

  cp(params =['1.txt', '2.txt'])