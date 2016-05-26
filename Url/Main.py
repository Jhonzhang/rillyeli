import mysql.connector
from url.check import *
from Realuser import Realurl
from url.pickurl import Realhost
from url.check import *
from Fillter import *
from ClassPart4 import *
# filepath=r"E:\testdata\test1\raw"
# excep,account,fnamenum=putMysql(filepath)
# print excep,account,fnamenum
conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                 use_unicode=True)
cursor = conn.cursor()
sql = "select * from url6"
try:
  cursor.execute(sql)
  results = cursor.fetchall()
  #results=results.encode("utf-8")

  backs,urls,h_totals,r_totals,u_totals,get=fback(results)

  print "-" * 80
  print "h_totals, r_totals, u_totals"
  print len(h_totals), len(r_totals), len(u_totals)
  print "-" * 80
  #check(u_totals)

  #print urls
  #print type(backs),h_totals,'\n',r_totals
  #print backs.keys(),'\n',type(urls),urls.keys()
  # for k1 in backs.keys():
  #   cursor.execute("insert into back (fname,url) values (%s,%s)",[k1,backs[k1]])
    #cursor.execute("delete from url where fname='%s'" %k1)

  #print len(urls),len(get),len(urls.keys()),urls
  print "total results:", len(results)
  print "total backs:", len(backs)
  print "total urls:",len(urls)
  #hostsoft=[]
  #classf(urls)
  urls00, urls01, urls10, urls11, host00,\
  host01, host10, host11, ref10, ref11, ua00, ua01, ua10, ua11, \
  get00, get01, get10, get11, cookie00, cookie01, cookie10, cookie11=classf(urls)
  #softs, others=fsoft(urls00, urls10)
  #print "softsnum00:",len(urls00),len(urls01),len(urls10),ref11

    # backitems.sort()
    # return [backitems[i][1] for i in range(0,len(backtitems))]
  print "-"*80
  print "Testxx:", "urls, host, get, ua, cookie,ref"
  print "Test00:",len(urls00),len(host00),len(get00),len(ua00),len(cookie00)
  print "Test01:",len(urls01),len(host01),len(get01),len(ua01),len(cookie01)
  print "Test10:",len(urls10),len(host10),len(get10),len(ua10),len(cookie10),len(ref10)
  print "Test11:",len(urls11),len(host11),len(get11),len(ua11),len(cookie11),len(ref11)
  # print "-" * 80
  # check(ua00)
  # print "-" * 80
  # check(ua01)
  # print "-" * 80
  # check(ua10)
  # print "-" * 80
  # check(ua11)
  #print get01.keys()
  # print "-" * 70
  # #check(host01)
  # sames,nosame1=check2(host01,host11)
  # print len(sames)
  # print len(nosame1)
  # #print len(r_totals)
  # #print host01

  # print "-" * 70
  # sames, nosame1=check2(host01,host11)
  # F1, R, P, realurl = Realhost(sames)
  # print "F1:", F1
  # print "Recall:", R
  # print "Precise:", P
  # print "realurl:",realurl
  #check1ist(sames)

  # print "-" * 70
  # userurl, userother, av = soteuser(ref11)
  # print userurl
  # print len(userurl)
  # # print "row of userurl:",len(userurl)


  # print "-" * 70
  # userurl, otherurl = userurls(ref11)
  # print len(userurl)
  # F1, R, P, realurl=Realurl(userurl)
  # print "F1:",F1
  # print "Recall:",R
  # print "Precise:",P
  # print "userurl:",userurl

  #print len(a),a
  # a=sorted(ref11.items(),lambda x,y:cmp(x[1],y[1]))
  # b=a[-1:-4:-1]
  # print type(a)
  # #print a
  # print b[0][0]
  #for k2 in softs.keys():
    #cursor.execute("insert into soft (fname,url) values (%s,%s)",[k2,softs[k2]])
    #cursor.execute("delete from url where fname='%s'" %k2)


  #softs,others=fsoft(urls00,urls10)
  #print len(urls11)
  #usergets0,others=userf2(urls01, urls11,userurl)
  #print len(usergets0)




except:
  print 'Error! check !!!'
conn.commit()
cursor.close()
conn.close()