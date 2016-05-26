import mysql.connector
#from url.check import *
from user import *
from Realuser import Realurl
from pickurl import Realhost
from checksql import maxua
from UserMT import usermt
from UA import RealUA
from Fillter import *
from check import *
from ClassPart4 import *
# filepath=r"E:\testdata\test1\raw"
# excep,account,fnamenum=putMysql(filepath)
# print excep,account,fnamenum
conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                 use_unicode=True)
cursor = conn.cursor()
sql = "select * from url4s"
try:
  cursor.execute(sql)
  results = cursor.fetchall()

  urls00, urls01, urls10, urls11, host00, host01, host10,\
  host11, ref10, ref11, ua00, ua01, ua10, ua11, get00, get01,\
  get10, get11, cookie00, cookie01, cookie10, cookie11=classurl(results)

  print "-" * 80
  print "Testxx:", "urls, host, get, ua, cookie,ref"
  print "Test00:", len(urls00), len(host00), len(get00), len(ua00), len(cookie00)
  print "Test01:", len(urls01), len(host01), len(get01), len(ua01), len(cookie01)
  print "Test10:", len(urls10), len(host10), len(get10), len(ua10), len(cookie10), len(ref10)
  print "Test11:", len(urls11), len(host11), len(get11), len(ua11), len(cookie11), len(ref11)
  print "-" * 80
  g_totals, h_totals, r_totals, u_totals, c_totals,num=fck(results)
  print "number of totalurls:",num
  print "-"*80
  print "g_totals, h_totals, r_totals, u_totals, c_totals"
  print len(g_totals),len(h_totals),len(r_totals),len(u_totals),len(c_totals)
  #check(ref11)
  print "-"*80
  # check(get01)
  print "-" * 80
  #check(get01)
  # print ref01
  # print "-" * 80
  # check(ref11)
  print "-" * 80
  check(ua11)
  print "-"*80
  realua,uanum=RealUA(urls11,ua11)
  print realua
  if len(realua)!=0:
    print realua
    print uanum
    realurl = usermt(urls01, urls11, realua)
    print realurl
    print "number of possible urls:", len(realurl)
    F1, R, P, realurls = Realurl(realurl)
    print "F1:", F1
    print "Recall:", R
    print "Precise:", P
    print "userurl:", len(realurls)
  # else:
  #   print "not click url"

  # refs=usermt(urls01, urls11, realua)
  # print len(refs)
  # checklist(refs)
  # print url
  # check(relref)
  # # print "-"*80
  # # # print ua
  # # checklist(ua)
  # print "number of possible urls:", len(url)

  # uas0="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.26 Safari/537.36"
  # uas1="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
  # uas2="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat"
  #refsback,ref=UaHost12(urls11,uas0)
  # print "-" * 80
  # print len(refsback),len(ref)
  # print "-" * 80
  # ref=UaHost1(urls11, uas0)
  # ref1=UaHost1(urls11, uas1)
  #check(ref1)
  # samef, nosamef, samf= check2d(ref, ref1)
  # print "-" * 80
  # check(samef)
  # print len(sames0)
  # print len(nosames0)
  #softacc, softfname=uaUser(urls11)
  #print u_totals
  # a,ua1=uaT(u_totals)
  # print "-" * 80
  # check(a)

  # print "-" * 80
  # bac = UaHost(uas0)
  # if bac==0:
  #   print "pass"
  # else:
  #   print "OK!"


  # for ua in ua1:
  #   sqlss = "select * from url10 where url like '%" + ua + "%'"
  #   cursor.execute(sqlss)
  #   resultss = cursor.fetchall()
  #   softnum, softfname=uaUser(resultss)
  #   if softnum>=0.1:
  #     print "ua of soft:", ua
  #     print softnum
  #     #checklist(softfname)
  #   # if uaUser(resultss)==0:
  #   #   print "ua of soft:",ua
  #   #
  #   else:
  #     print "-" * 80
  #     print ua

  # check(u_totals)
  #maxua(u_totals)
  # # check(get00)
  # # print "-" * 80
  # print "-" * 80
  # check(ua01)
  # print "-" * 80
  # check(ua11)
  # print "-" * 80

  #classua(urls01,"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36")
  #check(get01)
  #print urls01
  #check(u_totals)
  #checklist(ref11.keys())
  # aurl=Tref(r_totals)
  # F1, R, P, realurl=Realurl(aurl)
  # print "F1:",F1
  # print "Recall:",R
  # print "Precise:",P
  # print "userurl:",len(realurl)
  # sames, nosame1 = check2(host01, host11)
  # print len(sames)
  # print len(nosame1)
  #print sames
  # a="http://music.baidu.com/"
  # if a in ref11.keys():
  #   print a
  #print ref11
  #check(get01)
  # print get01.keys()
  # print ref11.keys()
  sames0, nosames0, sam0=check2d(get01,ref11)
  sames1, nosames1, sam1 = check2d(get11, ref11)
  #same=dict(sames0,**sames1)
  same=dict(sames0.items()+sames1.items())
  # print "sames1:",len(sames1)
  # check(sames0)
  #sames2, nosames2, sam2 = check2d(ref11,same)
  sames3, nosames3, sam3=check2get(get01,get11)
  sames4, nosames4, sam4 = check2d(host00,host11)
  # print "-" * 80
  # F1, R, P, realurl = Realurl(sames0)
  # print "number of possible urls:", len(sam1)
  #check(sam1)
  # print "F1:", F1
  # print "Recall:", R
  # print "Precise:", P
  # print "userurl:", len(realurl)
  # check(sames0)
  # print len(sames0)
  # print len(sames1)
  # uas=cheua(sames0)
  # check(uas)
  # uaks={}
  # for get2 in sames1.keys():
  #   uas,uakind=checkua(get2)
  #   for ua1 in uakind.keys():
  #     if ua1 not in uaks:
  #       uaks[ua1]=1
  #     else:
  #       uaks[ua1]=uaks[ua1]+1
  #
  #
  # print "-" * 80
  #check(uaks)
  # checkT(sam1)
  #urlss=Tref(sam1)
  #print get01.keys()
  #print sam1
  # cheurl,num=get11ref(sam1)
  # print "num of sameso without back:",num
  # check(cheurl)
  #checklist(cheurl.values())
  #print "-" * 80
  #print sames1
  #checkrefurl=cheget(sames1, get01)
  #checkrefurl = cheget2(sames1, get01)
  #check(checkrefurl)
  #print "checkrefurl:",checkrefurl
  #checklist(checkrefurl)
  #print type(sames1)
  #print "-" * 80
  #checkrefurl=cheget(sames1,get01)
  # F1, R, P, realurl=Realurl(checkrefurl.keys())
  # print "F1:",F1
  # print "Recall:",R
  # print "Precise:",P
  # print "userurl:",len(realurl)
  # ch="http://www.cnqiang.com/"
  # CharinD(ch,get00)
  #check(sames3)
  # F1, R, P, realurl = Realhost(sames3)
  # print "F1:",F1
  # print "Recall:",R
  # print "Precise:",P
  # print "userurl:",len(realurl)





except:
  print 'Error! check !!!'
conn.commit()
cursor.close()
conn.close()