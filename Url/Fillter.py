import re
from ClassPart4 import *
from back import back
#from test.soft import soft
#from soft import soft


def fback(results):
  backs={}
  urls={}
  h_totals={}
  r_totals={}
  u_totals={}
  get=[]
  for row in results:
    fname = row[1].encode("utf-8")
    surl = row[2].encode("utf-8")
    url=surl.replace('\t','').replace('\n',';;')

    isGet=re.compile(r'[POS|GE]T(.+?)HTTP/1.[0|1];;')
    Gets=re.findall(isGet,url)
    Get="".join(Gets)[1:]
    #Get=Get[1:]
    if len(Get)==0:
        continue
    else:
        get.append(Get)
        isHost=re.compile(r'Host:(.+?);;')
        Host=re.findall(isHost,url)
        Host="".join(Host)[1:]
        if Host not in h_totals:
            h_totals[Host]=1
        else:
            h_totals[Host]=h_totals[Host]+1

        isReferer=re.compile(r'Referer:(.+?);;')
        Ref=re.findall(isReferer,url)
        Ref="".join(Ref)[1:]
        if Ref not in r_totals:
            r_totals[Ref]=1
        else:
            r_totals[Ref]=r_totals[Ref]+1

        isUser=re.compile(r'User-Agent:(.+?);;')
        UAgent=re.findall(isUser,url)
        UAgent="".join(UAgent)[1:]
        if UAgent not in u_totals:
            u_totals[UAgent]=1
        else:
            u_totals[UAgent]=u_totals[UAgent]+1

        a=back(Get)
        if a==0:
            backs[fname]=surl
        else:
            urls[fname]=surl
  return backs,urls,h_totals,r_totals,u_totals,get

#def fclass(urls):

    #urls00,urls01,urls10,urls11,host00,host01,host10,host11,ref10,ref11,ua00=classf(urls)
    #return urls00,urls01,urls10,urls11,host00,host01,host10,host11,ref10,ref11,ua00


    #softs={}
    #others={}

  # b,hostsoft=soft(,ref1ua0)
  # if b==0:
  #     softs[fname]=surl
  # else:
  #     urls1[fname]=surl
 #return softs,urls1,hostsoft

def fck(results):
  #backs={}
  #urls={}
  g_totals={}
  h_totals={}
  r_totals={}
  u_totals={}
  c_totals={}
  #get=[]
  num=0
  for row in results:
    fname = row[1].encode("utf-8")
    surl = row[2].encode("utf-8")
    #url=surl.replace('\t','').replace('\n',';;')
    Get, Host, Ref, UAgent, Cookie=rexurl(surl)

    if len(Get)==0:
        continue
    else:
        num=num+1
        if Get not in g_totals:
            g_totals[Get] = 1
        else:
            g_totals[Get] = g_totals[Get] + 1

        if Host not in h_totals:
            h_totals[Host]=1
        else:
            h_totals[Host]=h_totals[Host]+1


        if Ref not in r_totals:
            r_totals[Ref]=1
        else:
            r_totals[Ref]=r_totals[Ref]+1


        if UAgent not in u_totals:
            u_totals[UAgent]=1
        else:
            u_totals[UAgent]=u_totals[UAgent]+1

        if Cookie not in c_totals:
            c_totals[Cookie] = 1
        else:
            c_totals[Cookie] = c_totals[Cookie] + 1


  return g_totals,h_totals,r_totals,u_totals,c_totals,num

def fckphone(results):
  #backs={}
  #urls={}
  g_totals={}
  h_totals={}
  r_totals={}
  u_totals={}
  c_totals={}
  #get=[]
  num=0
  for row in results:
    fname = row[1].encode("utf-8")
    surl = row[3].encode("utf-8")
    surl=surl.replace('\t','').replace('\n',';;')
    Get, Host, Ref, UAgent, Cookie=rexurl(surl)

    if len(Get)==0:
        continue
    else:
        num=num+1
        if Get not in g_totals:
            g_totals[Get] = 1
        else:
            g_totals[Get] = g_totals[Get] + 1

        if Host not in h_totals:
            h_totals[Host]=1
        else:
            h_totals[Host]=h_totals[Host]+1


        if Ref not in r_totals:
            r_totals[Ref]=1
        else:
            r_totals[Ref]=r_totals[Ref]+1


        if UAgent not in u_totals:
            u_totals[UAgent]=1
        else:
            u_totals[UAgent]=u_totals[UAgent]+1

        if Cookie not in c_totals:
            c_totals[Cookie] = 1
        else:
            c_totals[Cookie] = c_totals[Cookie] + 1


  return g_totals,h_totals,r_totals,u_totals,c_totals,num