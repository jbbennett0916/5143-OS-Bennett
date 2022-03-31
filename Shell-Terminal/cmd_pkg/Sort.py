import os


def sort(**kwargs):
  params = kwargs.get("params", None)
  with open(params[0], "r") as f:
    file = f.read().splitlines()
  file = sorted(file)

  for lines in file:
      print (lines)

  





if __name__ == '__main__':
  sort(params = ['output.txt'])