import mysql.connector
from user import soted
from check import get11ref,check,checklist,check2d,check2get,cherefget,chehost,getrefsame
from ClassPart4 import *
from pickurl import *
from Realuser import Realurl
from Fillter import *
 # dict type fname->Ref is get11

def maxUA(u_totals): # maxnum in dict return list maxchar
    maxua = max(u_totals.values())
    print "maxua:",maxua
    for c in u_totals.keys():
        if u_totals[c]==maxua:
            return c
def maxua(u_totals):
    # a=u_totals.keys()
    # print a
    # a=max(a)
    a=soted(u_totals)#maxnum in dict return list maxchar top0,1
    a=a[0]# max  top0
    #a=maxUA(u_totals)
    print a
    #getf = {}
    conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                   use_unicode=True)

    cursor = conn.cursor()
    sql = "select * from url1 where url like '%" + a + "%'"
    # print get,type(get)
    cursor.execute(sql)
    results = cursor.fetchall()

    urls00, urls01, urls10, urls11, host00, host01, host10, \
    host11, ref10, ref11, ua00, ua01, ua10, ua11, get00, get01, \
    get10, get11, cookie00, cookie01, cookie10, cookie11 = classurl(results)

    print "-" * 80
    print "Testxx:", "urls, host, get, ua, cookie,ref"
    print "Test00:", len(urls00), len(host00), len(get00), len(ua00), len(cookie00)
    print "Test01:", len(urls01), len(host01), len(get01), len(ua01), len(cookie01)
    print "Test10:", len(urls10), len(host10), len(get10), len(ua10), len(cookie10), len(ref10)
    print "Test11:", len(urls11), len(host11), len(get11), len(ua11), len(cookie11), len(ref11)
    print "-" * 80
    g_totals, h_totals, r_totals, u_totals, c_totals, num = fck(results)
    print "number of totalurls:", num
    print "-" * 80
    print "g_totals, h_totals, r_totals, u_totals, c_totals"
    print len(g_totals), len(h_totals), len(r_totals), len(u_totals), len(c_totals)
    print "-" * 80
    sames0, nosames0, sam0 = check2d(get01, ref11)
    sames1, nosames1, sam1 = check2d(get11, ref11)
    # same=dict(sames0,**sames1)
    same= dict(sames0.items() + sames1.items())
    #print len(same)
    sames2, nosames2, sam2 = check2d(ref11,same)
    sames3, nosames3, sam3 = check2get(host01, host11)
    print "-" * 80
    #sames4, nosames4, sam4 = check2d(sames0, get11)
    print "number of possible urls:",len(sames0)
    # print len(nosames1)
    #check(sames1)
    #F1, R, P, realurl = Realhost(sames0)
    F1, R, P, realurl=Realurl(sames0)
    print "F1:",F1
    print "Recall:",R
    print "Precise:",P
    print "userurl:",len(realurl)
    #
    #
    # # urlss=Tref(sam1)
    # # print get01.keys()
    # # print sam1
    # getrefsame(sames1, sam1)
    #refget={}
    # cheurl,num=get11ref(sam1)   # deal back
    # print "num of sameso without back:",num
    # check(cheurl)
    #a=0
    # for che in cheurl.keys():
    #     #print "che",che
    #     sqlche = "select * from url10 where url like '%" + che + "%'"
    #     # print get,type(get)
    #     #print sqlche
    #     cursor.execute(sqlche)
    #     resultss = cursor.fetchall()
    #     #print resultss
    #     getref=cherefget(che,resultss)
    #     #print getref
    #     for ccc in getref.keys():
    #         cg=getref[ccc]
    #         if cg not in refget:
    #             #print ccc
    #             refget[cg]=1
    #         else:
    #             refget[cg]=refget[cg]+1
    #
    #             # if len(cg)!=0:
    #             #     print cg
    #             #     refget.append(cg)
    #         # else:
    #         #     continue
    # print "len:",len(refget)
    #print refget
    #check(refget)
    #refhost=[]
    # refhost={}
    # for chost in refget.keys():
    #     #print chost
    #     chost1=pick(chost)
    #
    #     chost1= "".join(chost1)
    #     chost1 = chost1.replace(' ','')
    #     #print chost1
    #     if chost1 not in refhost:
    #         refhost[chost1]=1
    #     else:
    #         refhost[chost1]=refhost[chost1]+1


            # refhost.append(chost1)

    #check(refhost)
    #Realhost(refhost)
    # cheHost=chehost(sames0)
    # cheHost=cheHost.keys()
    # #print cheHost
    # #cheHost.extend(refhost)
    # exhost=list(set(cheHost+refhost))
    # exhost.remove('')
    # #exhost=cheHost.sort()
    # print "dd",exhost
    # print "-" * 80
    # F1, R, P, realurl=Realhost(exhost)
    # print "F1:",F1
    # print "Recall:",R
    # print "Precise:",P
    # print "userurl:",len(realurl)
    #checklist(cheurl.values())

    # for row in results:
    #     fname = row[1].encode("utf-8")
    #     surl = row[2].encode("utf-8")
    #     # print fname
    #     Get, Host, Ref, UAgent, Cookie = rexurl(surl)
    #     Get = Get.strip()
    #     if Get == get:
    #         # print fname,Ref
    #         getf[fname] = Ref
    #     else:
    #         continue
    cursor.close()
    conn.close()
    #return getf









#     url=surl.replace('\t', '').replace('\n', '')
#     #print url
#     ch="Host: soft.360.cn"
#     if ch in url:
#         print fname
# red="http://www.lofter.com/recommendblog?email=yang_jianli@163.com"
# redd=checkd(red)
# print redd
# c="zz"
# z="zz"
# if c==z:
#     print "OK"
