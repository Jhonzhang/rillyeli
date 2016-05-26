from ClassPart4 import *
from fclient import  fiphone,specile,fget
from back import back
from confg2list import *
from fclient import *
import chardet
def normalurl(Get):
    filepath = "D:/confg/normalurls.txt"
    with open(filepath) as f:
        for line in f.readlines():
            if len(line) != 1:
                try:
                    if line==Get:
                        return 0
                except:
                    continue
            else:
                break
def commonUA(UserAgent):
    account=0
    charpc1=['Chrome', 'Mozilla', 'AppleWebKit', 'KHTML', 'Safari', 'Gecko']
    for chs1 in charpc1:
        if chs1 in UserAgent:
            account=account+1
    if account==6:
        return 0
def favf(Gets):
    favs=['favicon.','icon','logo.']
    for f in favs:
        if f in Gets:
            return 0

def ie(ies,UAgent):
    a1=0
    lenies=len(ies)
    for ch1 in ies:
        if ch1 in UAgent:
            a1 = a1 + 1
    if a1==lenies:
        return 0
def ieUA(UAgent):

    ie1=['Mozilla','compatible','MSIE','Windows','NT','Trident/']
    ie2=['Mozilla','compatible','MSIE','Windows','NT']
    ie3=['Mozilla','compatible','MSIE','Windows','NT','Trident/','.NET4','.NET CLR','Tablet PC']
    ie4=['Mozilla','rv:','Windows','NT','like Gecko']
    if ie(ie1,UAgent)==0:
        return 0
    elif ie(ie2,UAgent)==0:
        return 0
    elif ie(ie3, UAgent)==0:
        return 0
    elif ie(ie4, UAgent)==0:
        return 0

filepath = "D:/confg/normalUAs.txt"
uacha=conf(filepath)
#print uacha
def specileUA(UAgent):
    for charua in uacha:
        if charua in UAgent:
            if commonUA(UAgent)==0:
                #print UAgent
                return 0
            elif 'Mozilla/' in UAgent:
                #print UAgent
                 # specile ua char in UA
                return 0
        else:
            continue


def RealUAMobile(urls):
    # urll={}
    ua=[]
    relua={}
    for fname in urls.keys():
        row=urls[fname]
        url=row.encode("utf-8")
        try:
            Get,Host, Ref, UAgent, Cookie = rexurl(url)
            Gets=Get.strip()
            #print UAgent
            if UAgent not in ua and UAgent.startswith("Mozilla/"):
                if fiphone(UAgent)==0:
                    ua.append(UAgent)
                elif specile(UAgent)==0:
                    ua.append(UAgent)
                elif favf(Gets)==0:
                    ua.append(UAgent)
                elif fget(Get,UAgent)==0:
                    ua.append(UAgent)
                else:
                    continue

            else:
                continue

        except:
            continue

    return ua

def RealUAPC(urls):
    ua=[]
    for fname in urls.keys():
        row = urls[fname]
        url = row.encode("utf-8")
        try:
            Get, Host, Ref, UAgent, Cookie = rexurl(url)
            Gets = Get.strip()
            if UAgent not in ua and UAgent.startswith("Mozilla/"):
                if specileUA(UAgent) == 0:
                    ua.append(UAgent)
                elif favf(Gets)==0:
                    ua.append(UAgent)
                elif normalurl(Gets)==0:
                    ua.append(UAgent)
                else:
                    continue
            else:
                continue
        except:
            continue
    return ua

def uap(ua,UAgent):
    if UAgent not in ua:
        ua[UAgent]=1
    else:
        ua[UAgent] = ua[UAgent] + 1
    return ua

def UAMbPc(results):
    a=0
    ua={}
    uano={}
    for row in results:
        try:
            fnames = row[0].encode("utf-8")
            fd = fnames.split("|")
            times = fd[0].strip()
            url = row[1].encode("utf-8")
            surl = url.replace('\t', '').replace('\n', ';;')
            # print surl1
            Get, Host, Ref, UAgent, Cookie=rexurlg(surl)

            if len(Get)==0 or "Mozilla/" not in UAgent:
                continue
            else:
                a=a+1
                Gets=Get.strip()
                UAgent=UAgent.strip()
                #UAgents=UAgent+"|"+times
                #uaurl[times]=UAgent
                if UAgent in ua:
                    ua[UAgent]=ua[UAgent]+1

                else:
                    if mobile(UAgent,Gets)==0:
                        ua=uap(ua,UAgent)
                    elif specileUA(UAgent)==0:
                        ua=uap(ua,UAgent)
                    elif favf(Gets)==0 and ieUA(UAgent)==0:
                        ua=uap(ua,UAgent)
                    elif favf(Gets)==0 and 'Mozilla/' in UAgent:
                        ua=uap(ua,UAgent)
                    else:
                        uano=uap(uano,UAgent)

        except:
            continue

    for keyua in ua.keys():
        if keyua in uano.keys():
            v1=ua[keyua]
            v2=uano[keyua]
            v=v1+v2
            #print v2
            ua[keyua]=v

    print "*"*80
    print "number  of row:",a
    #print uano
    return ua
