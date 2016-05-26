import os
import re
def fnameList(filename):
  a=[]
  files=os.listdir(filename)
  for fname  in files:
    isName=re.compile('^\d+_c.txt')
    result=re.findall(isName,fname)
    if result:
      a.extend(result)
  return a


