"""
If the ! x command is given, x being an integer 
number associated to the integer in the 
history.log, will print that whole command. 
IMPORTANT there has to be a space between the ! and the integer. 
example: ! 21 ... will print out cd

"""

def hist_num(**kwargs):
  params = kwargs.get("params", None)

  # if the '!x' command is given
  if params:
    # set the number value equal to params[1]
    num = params[0]
    num = int(num)
    num-=1
    # for line in range(num):
    with open("history.log", 'r') as f:
      params = f.readlines()
      # print out the appropriate line number
    print(params[num])
    return(params[num])
  else:
    print("error")


    
  


if __name__ == "__main__":
  hist_num(params= ['!', 20])