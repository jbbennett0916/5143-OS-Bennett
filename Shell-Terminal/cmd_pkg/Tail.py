import os

#Tail will display the last 10 lines of a given file 
#If the -n flag is given, the number that the user provides 
#will determine how many lines are displayed


# def tail(flags, params, redirects):
#   # if there are no flags
#   if not flags:
#     with open(params[0], "r") as f:
#       lines = f.read().splitlines()
#     #set default amount of lines to be the last 10 lines
#     amount_lines = 10  

#   elif '-n' in flags:
#     # set amount_lines equal to the first parameter in our list params
#     amount_lines = params[0]
#     # cast the amount to an integer
#     amount_lines = int(amount_lines)
    

#     with open(params[1], 'r') as f:
#       lines = f.read().splitlines()


#   # print each line in lines starting at 10 lines from the end. to the end
#   # or if -n is used, len(lines) - the number the user input, so like n = 25
#   # So 100-25 = 75, so print out lines 75-100
#   count = len(lines)
#   for line in lines[count-amount_lines:]:
#     print(line)












def tail(**kwargs):
  # params = kwargs['params']
  # flags = kwargs['flags']
  params = kwargs.get("params", None)
  flags = kwargs.get("flags", None)

  # if there are no flags
  if not flags:
    with open(params[0], "r") as f:
      lines = f.read().splitlines()
    #set default amount of lines to be the last 10 lines
    amount_lines = 10  

  elif '-n' in flags:
    # set amount_lines equal to the first parameter in our list params
    amount_lines = params[0]
    # cast the amount to an integer
    amount_lines = int(amount_lines)
    

    with open(params[1], 'r') as f:
      lines = f.read().splitlines()


  # print each line in lines starting at 10 lines from the end. to the end
  # or if -n is used, len(lines) - the number the user input, so like n = 25
  # So 100-25 = 75, so print out lines 75-100
  count = len(lines)
  for line in lines[count-amount_lines:]:
    print(line)




if __name__ =='__main__':
  


  tail(params = [25,'Moby_Dick.txt'], flags = ['-n'])