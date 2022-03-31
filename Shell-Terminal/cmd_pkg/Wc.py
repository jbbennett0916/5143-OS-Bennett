
def wc(**kwargs):
  params = kwargs.get("params", None)
  flags = kwargs.get("flags", None)
  #redirects = kwargs.get("redirects", None)
  lines = 0
  words = 0
  chars = 0

  result = {
    "lines":None,
    "words":None,
    "chars":None
  }
  
#   flag_dict ={
#     '-w' : words,
#     '-m' : chars,
#     '-l' : lines
  #    -lm
# } 
  for index in params:
    with open(index) as f:
      data = f.read()

  lineArray = data.split("\n")

  lines = len(lineArray)
  for line in lineArray:
    chars += len(line)
    words += len(line.split())



  
    #if no flags are passed
  if not flags:
    print (lines,words,chars)
    lines = str(lines)
    words = str(words)
    chars = str(chars)
    return (lines,words,chars)


    
  #for flag in flags:
  if 'l' in flags:
    result['lines']=lines
  if 'm' in flags:
    result['chars']=chars
  if 'w' in flags:
    result['words']=words
      
  ret = ""
  if result['lines']:
    ret += str(result['lines'])+ " "
  if result['words']:
    ret += str(result['words'])+ " "
  if result['chars']:
    ret += str(result['chars'])+" "
  print(ret)
  #return ret

  
if __name__=='__main__':
  with open("newfile.txt") as f:
    data = f.read()

  print(wc("", data)) # no flags
  print("Lines: ",wc(["-l"], data)) # lines
  print("Words: ", wc(["-w"], data))# words
  print("Chars: ", wc(["-m"], data)) #chars
 


  print(wc(["-w", "-l"], data))# words and lines
  print(wc(["-l", "-m"], data)) #lines and chars
  print(wc(["-w", "-m"], data)) # words and chars
  #print(wc(["-z", "-m"], data)) # should print invalid
