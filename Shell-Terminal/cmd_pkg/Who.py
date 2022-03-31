import getpass



def who(**kwargs):
    directions = kwargs['params']
    # empty string to pass the current users logged in
    user = ""
    # getpass.getuser() displays the login name of the user
    user = getpass.getuser()
    # if no directions
    if(len(directions) == 0):
      print(user)
      return user
    # if there is a mode to redirect it to another file
    elif(len(directions) == 2):
      # the mode
        direct = directions[0]
        # the file name to direct it to
        file = directions[1]
        # open the file in directions[1] with the mode in directions[0]
        f = open(file, direct)
        # writes the text in user to a file
        f.write(user)
        f.close()

if __name__ == "__main__":
  print(who(directions = [])) ## --> works
  print(who(directions = ['w','file.txt'])) ## --> works