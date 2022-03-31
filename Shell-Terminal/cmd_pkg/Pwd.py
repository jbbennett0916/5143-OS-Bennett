import os


#####################################################
###     pwd will print tthe current working directory
###
#####################################################



# def Pwd(flags, params, redirects):
#   working_dir = os.getcwd()
#   if redirects:
#     mode = redirects[0]
#     write_file_name = redirects[1]
#     with open(write_file_name, mode) as wf:
#       wf.write(working_dir)

#   else:
#     return print(working_dir)

def pwd(**kwargs):
  params = kwargs.get('params', None)
  redirects = kwargs.get("redirects", None)
  working_dir = os.getcwd()
  if redirects:
    mode = redirects[0]
    write_file_name = params[0]
    with open(write_file_name, mode) as wf:
      wf.write(working_dir)

  else:
    return print(working_dir)



if __name__ == '__main__':    
  pwd(redirects = 'w', params = ['output1.txt'])
