import re
import codecs
from ClassPart4 import *
import mysql.connector
from lxml import etree
#path=r"D:\testdata\test7\raw"
path=r"D:\Browsers\2345s\raw"
path=path.replace('\\','/')
#html=r"D:\testdata\test5\_index.htm"
html=r"D:\Browsers\2345s\_index.htm"
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
        data0=f1.read()
        data1=data0.decode("ISO-8859-2")
        data=data1.encode("utf-8")

        #data=data.replace('\t','')
        #print type(data)
    #fnames=tr_nodes1[tim]+"|"+filename
    usercount="2345"
    fnames = tr_nodes1[tim] + "|" + filename
    fname = fnames.encode("utf-8")
    surl =data[:]
    #urls = surl.replace('\t', '').replace('\n', ';;')
    # Get, Host, Ref, UAgent, Cookie = rexurll(urls)
    # url=Get+Host+Ref+UAgent+Cookie
    #print fname,url
    #print type(url)
    #url=url.encode("utf-8")

    try:
        #pass
        cursor.execute("insert into 2345ss (usercount,fname,url) values(%s,%s,%s)", [usercount,fname, surl])

    except:

        excep.append(fname)
        #print
        #continue
        #
    else:
       account = account + 1


conn.commit()
cursor.close()
conn.close()
f.close()

print excep,"\n","num of except:",len(excep),"\n",account

