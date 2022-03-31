from rich import print


def parseCmd(cmd):
  """ Used by parseRawCmd
  """
  newCmd = {}

  cmd = cmd.split()

  newCmd["cmd"] = cmd[0]
  
  if len(cmd)  > 1 and "-" in cmd[1]:
    newCmd["flags"] = cmd[1]
    
  if not "flags" in newCmd and len(cmd) > 1:
    newCmd["params"] = cmd[1:]
  elif "flags" in newCmd and len(cmd) > 2:
    newCmd["params"] = cmd[2:]

  if "flags" in newCmd and not "-" in newCmd["flags"]:
    newCmd['params'].insert(0,newCmd["flags"])
    del newCmd['flags']
  
  return newCmd


def parseRawCmd(cmd):
  """
      cmd
      flags
      params
      redirect 
    Returns:
      Dictionary with each component
    Example:
      {
        "cmd":"cat",
        "flags":"-fax"
        "params":['main.py','lib1.py',...]
        "redirectType":(">",">>")
        "target":"output"
      }
    """
  newCmd = {}
  redirFlag = False
  cmds = None

  # Check for redirect and split on that
  if ">>" in cmd:
    redirFlag = True
    redirectType = "concat"
    # a+ will append
    cmd,target = cmd.split('>>')
    # print(cmd)
    # print(target)
    # str_res = ""
    # for param1 in cmd:
    #   str_res += param1
    # str_res= str_res.split()
      # with open(cmd, 'r') as f:
      #   with open(target, 'a+') as g:
      #     for line in f:
      #       g.write(line)
    

      
  elif ">" in cmd:
    redirFlag = True
    redirectType = "new"
    # w+ will rewrite the file
    cmd,target = cmd.split('>')


  if "|" in cmd:
    cmds = cmd.split("|")
  else:
    cmd = parseCmd(cmd)
    
  # if we split on a pipe do this 
  if not cmds == None:
    for i in range(len(cmds)):
        cmds[i] = parseCmd(cmds[i])
  else:
    cmds = [cmd]


  # thing that i plan on returning
  retCmd = {
    'cmdsList':cmds,
  }

  if redirFlag:
    retCmd['redirectType'] = redirectType
    retCmd['target'] = target
    if redirectType == '>>':
      with open(target, 'a+') as g:
        g.write(cmds)
  return retCmd


if __name__=='__main__':
  #cmdString = "cat file1 file2 file3 | grep moby | wc -m > output"
  cmdString = "ls -lah | grep .txt >> concatFile.out"
  #cmdString = "ls -lah | cat file1 file2 > sendtooutfile"
  cmdParsed = parseRawCmd(cmdString)
  print(cmdParsed)

  # for cmd in cmdParsed['cmdsList']:
  #   commands[cmd['cmd']](**cmd)
