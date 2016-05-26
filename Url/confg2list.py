def conf(filepath):
  a=[]
  with open(filepath) as f:
    data=f.readlines()
    for line in data:
      if len(line)!=1:
        line=line.strip('\n')
        a.append(line)
      else:
        break
  return a