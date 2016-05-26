import re

h_totals={}
r_totals={}
users={}
def fsoft(results):
  for row in results:
    fname = row[1]
    url = row[2]
    url = url.encode("utf-8")
    url=url.replace('\t','').replace('\n',';;')

    isGet=re.compile(r'GET(.+?);')
    Get=re.findall(isGet,url)
    Get="".join(Get)

    isHost=re.compile(r'Host:(.+?);')
    Host=re.findall(isHost,url)
    Host="".join(Host)
    if Host not in h_totals:
      h_totals[Host]=1
    else:
      h_totals[Host]=h_totals[Host]+1

    isReferer=re.compile(r'Referer:(.+?);')
    Ref=re.findall(isReferer,url)
    Ref="".join(Ref)
    if Ref not in r_totals:
      r_totals[Ref]=1
    else:
      r_totals[Ref]=r_totals[Ref]+1

    isUser=re.compile(r'User-Agent:(.+?)\);')
    UAgent=re.findall(isUser,url)
    UAgent="".join(UAgent)

     #aa=aa+1
      #backs.append(surl)

      #backs[fname]=surl
      #cursor.execute("insert into backurl (fname,url) values (%s,%s)",[fname,Get])

      #print fname, Get
      #cursor.execute("delete from gethttp where fname='%s'" %fname)
      #conn.commit()

     #for c in charback:
      #if c in Get:
        #cursor.execute("insert into back (fname,url) values (%s,%s)",[fname,Get])

    # for line in url.readline():
    # if line.stratswith("GET"):
    # print line
    # if c in line:
    # a.append(c)
    # print a

    # if a:
    # cursor.execute("insert into back (fname,url,back) values (%s,%s,%s)",[fname,url,a])

    # print url


