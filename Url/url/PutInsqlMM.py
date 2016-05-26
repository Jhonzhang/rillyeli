import re
import codecs
from ClassPart4 import *
from ClassPartMM import rexurlmm
import mysql.connector
from lxml import etree
# path=r"D:\Browsers\test001\raw"
# html=r"D:\Browsers\test001\_index.htm"
path=r"D:\confg\test\test01\raw"
html=r"D:\confg\test\test01\_index.htm"
path=path.replace('\\','/')
html=html.replace('\\','/')

conn=mysql.connector.connect(host='127.0.0.1',user='rootztf',password='rootztf',port='3306',database='browsers',use_unicode=True)
cursor=conn.cursor()
excep=[]
account=0
f=codecs.open(html,"r")
content=f.read()
tree=etree.HTML(content)
tr_nodes0=tree.xpath(u'//tbody/tr/td/a[1]/@href')
tr_nodes1=tree.xpath(u'//tbody/tr/td[last()]/text()')
num=len(tr_nodes1)
res = re.compile(r'\d+_c.txt')
for tim in range(num):
    filename = re.findall(res, tr_nodes0[tim])
    filename = "".join(filename)
    with open(path + '/' + filename) as f1:
        data0= f1.read()
        data1=data0.decode("ISO-8859-2")
        data=data1.encode("utf-8")
    fnames=tr_nodes1[tim]+"|"+filename
    fname = fnames.encode("utf-8")
    surl =data[:]
    urls = surl.replace('\t', '').replace('\n', ';;')
    a=urls.count(';;')
    urlsnum,Action, Gett, Host, Ref, UAgent, Cookie,Connection, Accept, AcceptCharset, AcceptEncoding, \
    ContentLength,AcceptLanguage, AccetpRanges, Authorization, CacheControl, ContentType, \
    Date, Expect,Froms, IfMatch,IfModifiedSince, IfNoneMatch, IfRange, IfUnmodifiedSince, MaxForwards, \
    Pragma, ProxyAuthorization, Ranges, TE, Upgrade, Via, Warning=rexurlmm(urls)
    usercount="test01"
    if len(urlsnum)!=a:
        alls='1'
    else:
        alls='0'
    try:
        cursor.execute("insert into test01 (usercount,fname,url,alls,Action, Gett, Host, Referer,"
                       "UserAgent, Cookie, Connection,Accept, AcceptCharset,"
                       "AcceptEncoding,ContentLength ,AcceptLanguage, AccetpRanges,"
                       "Authorization, CacheControl, ContentType,Date,Expect, Froms, "
                       "IfMatch,IfModifiedSince, IfNoneMatch, IfRange, IfUnmodifiedSince,"
                       "MaxForwards, Pragma, ProxyAuthorization, Ranges, TE, Upgrade, Via,"
                       "Warning) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                       "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                       "%s,%s,%s,%s,%s,%s,%s,%s,%s)",[usercount,fname,data,alls,Action,Gett,Host,
                                                      Ref, UAgent,Cookie,Connection, Accept,
                                                      AcceptCharset,AcceptEncoding,ContentLength,
                                                      AcceptLanguage,AccetpRanges,Authorization, CacheControl,
                                                      ContentType,Date, Expect,Froms, IfMatch,IfModifiedSince,
                                                      IfNoneMatch, IfRange, IfUnmodifiedSince, MaxForwards,Pragma,
                                                      ProxyAuthorization, Ranges, TE, Upgrade, Via, Warning])

    except:

        excep.append(filename)

    else:
       account = account + 1

conn.commit()
cursor.close()
conn.close()
f.close()

print excep,"\n","number of bad:",len(excep),"\n","OK:",account

