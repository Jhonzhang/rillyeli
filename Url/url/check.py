from ClassPart4 import hof
#from operator import mul
from ClassPart4 import *
import mysql.connector
from back import back
from pickurl import pick
from user import add
from soft import soft
# from checksql import checkd
def checkd(get): # check out which get's refrere is get11(get)
    getf={}
    conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                   use_unicode=True)


    cursor = conn.cursor()
    sql="select * from url10 where url like '%"+get+"%'"
    #print get,type(get)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname=row[1].encode("utf-8")
        surl=row[2].encode("utf-8")
        #print fname
        Get, Host, Ref, UAgent, Cookie = rexurl(surl)
        Get=Get.strip()
        if Get==get:#get11 same with ref11 , when get is Get checkout get's referer
            #print fname,Ref
            getf[fname]=Ref
        else:
            continue

    cursor.close()
    conn.close()
    return getf

def checkua(get):
    getf={}
    uakind={}
    conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                   use_unicode=True)

    cursor = conn.cursor()
    sql="select * from url10 where url like '%"+get+"%'"
    #print get,type(get)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname=row[1].encode("utf-8")
        surl=row[2].encode("utf-8")
        #print fname
        Get, Host, Ref, UAgent, Cookie = rexurl(surl)
        Get=Get.strip()
        if Get==get:#get11 same with ref11 , when get is Get checkout get's referer
            #print fname,Ref
            getf[fname]=UAgent
            if UAgent not in uakind:
                uakind[UAgent]=1
            else:
                uakind[UAgent]=uakind[UAgent]+1
        else:
            continue

    cursor.close()
    conn.close()
    return getf,uakind


def cheua(sames1):
    uas={}
    conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                   use_unicode=True)
    cursor = conn.cursor()
    checkrefurl = {}
    #a=0
    # print get01.keys()
    # s="http://www.sunland.org.cn/ "
    # if s in get01.keys():
    #     print s
    for c1 in sames1.keys():
            # print c1,type(c1)
        c1 = c1.strip()
        sql = "select * from url11 where url like '%" + c1 + "%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            fname=row[1].encode("utf-8")
            surl=row[2].encode("utf-8")

            Get,Host,Ref,UAgent,Cookie=rexurl(surl)
            Get=Get.strip()
            if len(Get)!=0 and Get==c1:
                if UAgent not in uas:
                    uas[UAgent]=1
                else:
                    uas[UAgent]=uas[UAgent]+1

    cursor.close()
    conn.close()
    return uas

def UaHost(ua):
    #hosts={}
    conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                   use_unicode=True)
    cursor = conn.cursor()

    sql = "select * from url11 where url like '%" + ua + "%'"
    cursor.execute(sql)
    results = cursor.fetchall()
    #all=cursor.rowcount
    als=0
    num=0
    sof=0
    for row in results:
        fname=row[1].encode("utf-8")
        surl=row[2].encode("utf-8")
        #print type(surl)
        cha="CONNECT"
        if cha in surl:
            num=num+1
            #print fname
        Get,Host,Ref,UAgent,Cookie=rexurl(surl)
        Get=Get.strip()
        ch="https:"
        if len(Get)!=0 and UAgent==ua:
            if back==0:
                sof=sof+1
            if ch in Get:
                als=als+1


    cursor.close()
    conn.close()
    if als!=0:
        res=float(num)/als
        if res<=0.5 and sof!=0:
            return 0  # has https but soft and https nums too smal
        else:
            return 1
    else:  # no https UA
        return 0


def UaHost1(urls,ua):
    hosts={}
    ua=ua.strip()
    for row in urls.values():
        url=row.encode("utf-8")
        Get,Host,Ref,UAgent,Cookie=rexurl(url)
        Get=Get.strip()
        #UAgent=UAgent.strip()
        if len(Get)!=0 and UAgent==ua:
            if Ref not in hosts:
                hosts[Ref]=1
            else:
                hosts[Ref]=hosts[Ref]+1
    print "kinds of hosts:",len(hosts)
    return hosts
# def uaref(urls,ref):
#
#     for fname in urls.keys():
#         row=urls[fname]
#         url=row.encode("utf-8")
#         try:
#             Get, Host, Ref, UAgent, Cookie = rexurl(url)
#             Gets = Get.strip()
#             Ref = Ref.strip()
#             if



def UaHost2(urls,ua):
    refs={}
    ref={}
    ua=ua.strip()
    for fname in urls.keys():
        row=urls[fname]
        url=row.encode("utf-8")
        try:

            Get,Host,Ref,UAgent,Cookie=rexurl(url)
            Gets=Get.strip()
            https=http(Gets)
            Ref=Ref.strip()
            back=soft(Get,Host,Ref,UAgent)

            if https==1 and UAgent==ua:
                if back == 0:
                    print https,fname
                    if Ref not in refs:
                        refs[Ref]=1
                    else:
                        refs[Ref]=refs[Ref]+1
                else:
                    if Ref not in ref:
                        ref[Ref]=1
                    else:
                        ref[Ref]=ref[Ref] + 1
        except:
            print "Error:",fname

    return refs,ref

def http(get):  # pick out which get with more than 2 http
    res=re.compile(r'(http)')
    https=re.findall(res,get)
    #print https
    if len(https)!=0:
        if len(https)>=2:
            return 0
        else:
            return 1
    else:
        pass
# get="http://googlead"
# a=http(get)
# print a

def CharinD(cha,D):
    cha=cha.strip()
    # if cha in D.keys():
    for dch in D.keys():
        dch=dch.strip()
        if dch==cha:
            print cha

def check(d):
    # print str(d.__class__)
    for dk in d.keys():
        print dk,":",d[dk]

def checkT(d):
    account=0
    a=[]
    for dk in d.keys():
        num=d[dk]
        if num>=10:
            account=account+1
            print dk,":",num
        else:
            a.append(num)
    print "number of Over Threshold:",account
    print "length of low Threshold:",len(a)
    print a

def check2kk(d):
    # print str(d.__class__)
    for dk in d.keys():
        print dk,":",d[dk]

def Tref(d):
    a=0
    aurl=[]
    # print str(d.__class__)
    for dk in d.keys():
        if len(dk)!=0 and d[dk]>=15:
            dk=dk.encode("utf-8")
            aurl.append(dk)
            a=a+1
            #print dk," : ",d[dk]
    print "countnum of checkout:",a
    return aurl

def checklist(l):
    for li in l:
        print li

def check2(d1,d2):
    sames=[]
    nosame1=[]
    nosame2=[]
    for c1 in d1.keys():
        if c1 in d2.keys():
            sames.append(c1)
        else:
            nosame1.append(c1)
            #nosame2.append(c2)
            continue
    return sames,nosame1

def check2d(d1,d2):
    sames1={}
    sames2={}
    nosame1={}
    #nosame2={}
    #print type(d2.keys())
    for c1 in d1.keys():
        c1url=d1[c1]
        c1=c1.strip()
        #print type(c1)
        if c1 in d2.keys():
            sames1[c1]=c1url
            sames2[c1] =d2[c1]
        else:
            nosame1[c1]=c1url

    return sames1,nosame1,sames2

def check2get(d1, d2):
    sames1 = {}
    sames2 = {}
    nosame1 = {}
    for c1 in d1.keys():
        c1url = d1[c1]
        #c1 = c1.strip()
            # print type(c1)
        if c1 in d2.keys():
            sames1[c1] = c1url
            sames2[c1] = d2[c1]
        else:
            nosame1[c1] = c1url

    return sames1, nosame1, sames2

def cheget(sames1,get01):
    checkrefurl=[]
    for c1 in sames1.keys():
        #print c1,type(c1)
        c1=c1.strip()
        c1s=checkd(c1)# check out in mysql which sames is get11&ref11
        #print c1s
        if len(c1s)!=1:
            for c2 in c1s.values():
                c2 = c2.strip()
                #print c1s[c2]
                if c2 in get01.keys():
                    checkrefurl.append(c2)
                else:
                    continue
    return checkrefurl


def checkdref(get,results):
    getf = {}
    for row in results:
        fname=row[1].encode("utf-8")
        surl=row[2].encode("utf-8")
        #print fname
        Get, Host, Ref, UAgent, Cookie = rexurl(surl)
        Get=Get.strip()
        if Get==get:
            #print fname,Ref
            getf[fname]=Ref
        else:
            continue

    return getf

def cherefget(ref,results):
    getref = {}
    for row in results:
        fname=row[1].encode("utf-8")
        surl=row[2].encode("utf-8")
        #print fname
        Get, Host, Ref, UAgent, Cookie = rexurl(surl)
        Get=Get.strip()
        if Get==ref:
            #print fname,Ref
            getref[fname]=Ref
        else:
            continue

    return getref
def cheuaget(ua,results):
    getref = {}
    for row in results:
        fname=row[1].encode("utf-8")
        surl=row[2].encode("utf-8")
        #print fname
        Get, Host, Ref, UAgent, Cookie = rexurl(surl)
        Get=Get.strip()
        if Get==ua:
            #print fname,Ref
            getref[fname]=Ref
        else:
            continue

    return getref
def cheget2(sames1, get01):
    conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                   use_unicode=True)
    cursor = conn.cursor()
    checkrefurl = {}
    a=0
    # print get01.keys()
    # s="http://www.sunland.org.cn/ "
    # if s in get01.keys():
    #     print s
    for c1 in sames1.keys():
            # print c1,type(c1)
        c1 = c1.strip()
        sql = "select * from url10 where url like '%" + c1 + "%'"
        cursor.execute(sql)
        results = cursor.fetchall()
        c1s = checkdref(c1,results)
        #print c1s
        if len(c1s) != 0:
            for c2 in c1s.values():
                #print type(c2)
                c22 = c2+" "

                if c22 in get01.keys():
                    a=a+1
                    if c2 not in checkrefurl:
                        checkrefurl[c2]=1
                    else:
                        checkrefurl[c2]=checkrefurl[c2]+1
                    #checkrefurl.append(c2)
                    #print c2
                else:
                    continue
        else:
            continue
    print a
    cursor.close()
    conn.close()
    return checkrefurl

def get11ref(urls):
    cheurl={}
    b=0
    for u in urls.keys():
        a=back(u)
        if a==0:
            b = b + 1
            cheurl[u] = urls[u]
            # continue
        else:
            continue
            # b=b+1
            # cheurl[u]=urls[u]
    return cheurl,b

def chehost(sames1):
    samehost={}
    for ke in sames1.keys():
        ke1=pick(ke)
        ke22="".join(ke1)
        ke2=ke22.replace(' ', '')
        if ke2 not in samehost:
            #print ke2
            samehost[ke2]=1
        else:
            samehost[ke2]=samehost[ke2]+1
            #print ke2
    return samehost

def getrefsame(sames1,sam1):
    #num=len(sames1)
    use={}
    a=1
    for c1 in sames1.keys():
        #c11 = c1.strip()
        #print c1
        if c1 in sam1.keys():
            print a,":",c1
            #print c1
            print "getnum:",sames1[c1]
            print "refnum:",sam1[c1]
            a = a + 1
            if sam1[c1]>=50:
                use[c1]=sam1[c1]

        else:
            continue
    print use


def classua(urls,ua):
    #url={}
    for fname in urls.keys():
        row=urls[fname]
        row=row.encode("utf-8")
        Get, Host, Ref, UAgent, Cookie = rexurl(row)
        if UAgent==ua:
            print "fname:",fname
            print Get
            print Host
            #print Ref
            print UAgent
            #print Cookie

def uaT(u_totals):
    uas={}
    ua1=[]
    sums=reduce(add,u_totals.values())
    for ua in u_totals.keys():
        back=rexua(ua)
        num=u_totals[ua]
        if back!=0:
            acc=float(num)/sums
            uas[ua]=acc
            if acc>=0.1:
                print ua,":",acc
                ua1.append(ua)
    return uas,ua1

def uaUser(urls):# select from msyql  results to deel with urls
    softnum=0
    softfname=[]
    allnum=len(urls)
    for row in urls:
        fname1 = row[1]
        surl1 = row[2].encode("utf-8")
        Get,Host,Ref,UAgent,Cookie=rexurl(surl1)

        #soft(get, host, ref, uagent)
        a=soft(Get,Host,Ref,UAgent)
        if len(Get) == 0:
            continue
        else:
            if a==0:
                softnum=softnum+1
                # print fname1
                # print UAgent
                softfname.append(fname1)
                # print "-" * 80
                # print fname1
                # return 0
            #break

            else:
                continue
    softacc=float(softnum)/allnum
    return softacc,softfname





