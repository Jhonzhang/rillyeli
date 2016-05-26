import re

from back import back
import soft


def fback(results):
  backs={}
  urls={}
  h_totals={}
  r_totals={}
  u_totals={}

  for row in results:
    fname = row[1].encode("utf-8")
    surl = row[2].encode("utf-8")
    url=surl.replace('\t','').replace('\n',';;')

    isGet=re.compile(r'[POST|GET](.+?);')
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
    if UAgent not in u_totals:
      u_totals[UAgent]=1
    else:
      u_totals[UAgent]=u_totals[UAgent]+1

    a=back(Get)
    if a==0:
      backs[fname]=surl
    else:
      urls[fname]=surl
  return backs,urls,h_totals,r_totals,u_totals

def fsoft(urls,hostsoft,ref):
  softs={}
  urls1={}
  h_totals={}
  r_totals={}
  u_totals={}
  #hostsoft=[]
  #ref1={}
  num=0
  for k in urls.keys():
    hsofts=hostsoft
    fname=k
    surl=urls(k)
    url=surl.replace('\t','').replace('\n',';;')

    isGet=re.compile(r'[GET|POST](.+?);')
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
    if UAgent not in u_totals:
      u_totals[UAgent]=1
    else:
      u_totals[UAgent]=u_totals[UAgent]+1

    b,hostsoft=soft(Get,Host,Ref,UAgent,hsofts)
    if b==0:
      softs[fname]=surl
    else:
      urls1[fname]=surl
  return softs,urls1,hostsoft