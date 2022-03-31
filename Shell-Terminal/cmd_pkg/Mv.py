import os
import shutil


def mv(**kwargs):
  file_name_params = kwargs.get('params', None)
  original_file = file_name_params[0]
  new_file = file_name_params[1]
  if os.path.exists(original_file):
    dir_path = os.getcwd()
    #dir_path = os.path.dirname(__file__)
    original_path = os.path.abspath(os.path.join(dir_path, original_file))
    new_path = os.path.abspath(os.path.join(dir_path, new_file))

    shutil.move(original_path, new_path)
  elif not os.path.exists(original_file):
    print("File does not exist.")
    return


  
if __name__ == '__main__':
  mv(file_name_params = ['1.txt', 'bananas'])