import re

def pick(url):
    res=re.compile(r'^http[s]?://(.+?)[/]+?')
    pik=re.findall(res,url)
    #print pik
    return pik

# url0="http://www.cnqiang.com/360ts/xwtt/201604/01273580.html"
# print pick(url0)

def Realhost(userurl):
    #filepath = "E:/confg/urls.txt
    #print userurl
    a=0
    click=0
    #F1=0
    row = len(userurl)
    #print"row of Clickurl:",row
    realurl=[]
    f1=open("D:/confg/ClickUrl1.txt",'r')
    #f2=open("E:/confg/RealUrl.txt","a")
    for line in f1.readlines():
        sfp = line.replace('\n','')
        if len(line)!= 1:
            click=click+1
            sfp0=pick(sfp)
            #print type(sfp0)
            sfp0="".join(sfp0)
            #print sfp0
            if sfp0 in userurl:
                #print sfp0
                a=a+1
                realurl.append(sfp0)
            else:
                continue
        else:
            break
    print "-" * 80
    print "click:",click
    Recall = float(a) / click
    R= round(Recall, 3)
    Precise = float(a) /row
    P=round(Precise, 3)
    F1=float(2*P*R)/(P+R)
    F1= round(F1, 2)
    return F1,R,P,realurl