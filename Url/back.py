
from confg2list import conf
pathofback=r"D:/confg/back.txt"
charback=conf(pathofback)
#print charback
def back(url):
  #a=0
  for c in charback:
    if c in url and ".jsp" not in url:
      return 0
      #break
      #print url
    else:
      continue

