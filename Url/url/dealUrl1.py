import re

import mysql.connector

from back import back
from confg2list import conf
from test.real import soft

pathofback = r"B:/confg/back.conf"
pathofsoft = r"B:/confg/soft.conf"
charback = conf(pathofback)
charsoft = conf(pathofsoft)
backlist = []
softlist = []
aa=0
bb=0
b2=0
b3=0
def getconn():
  conn = mysql.connector.connect(host='127.0.0.1', user='root', password='rootztf', port='3307', database='url',
                                 use_unicode=True)
  return conn


conn = getconn()
cursor = conn.cursor()
sql = "select * from gethttp"
try:
  cursor.execute(sql)
  results = cursor.fetchall()
  for row in results:
    fname = row[1]
    url = row[2]
    url = url.encode("utf-8")
    # print type(url)
    url=url.replace('\t','').replace('\n',';;')
    #print type(url)
    #break
    isGet=re.compile(r'GET(.+?);')
    Get=re.findall(isGet,url)
    Get="".join(Get)
    #print Get
    #print fname,type(Get)
    #break
    isHost=re.compile(r'Host:(.+?);')
    Host=re.findall(isHost,url)
    #print Host
    isReferer=re.compile(r'Referer:(.+?);')
    Referer=re.findall(isReferer,url)
    #print Referer
    isUser=re.compile(r'User-Agent:(.+?)\);')
    UserAgent=re.findall(isUser,url)
    #print UserAgent
    a=back(Get)
    #print a
    #break
    if a==0:
      bb=bb+1
      #cursor.execute("insert into backurl (fname,url) values (%s,%s)",[fname,Get])

      #print fname, Get
      #cursor.execute("delete from gethttp where fname='%s'" %fname)
      #conn.commit()
    else:
      aa=aa+1
      b=soft(Get)
      if b==0:
        b2=b2+1
        print fname,Get
      else:
        b3=b3+1
        continue

      #print fname,Get
      #continue
  print aa,b2,b3

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








except:
  print 'Error unable to fetch data!'
conn.commit()
cursor.close()
conn.close()
