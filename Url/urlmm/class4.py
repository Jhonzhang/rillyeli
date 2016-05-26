# coding:utf-8
import re
from tld import get_tld
from soft import soft
def rexurll(url0):
    isGet = re.compile(r'(.+?HTTP/1.[0|1];;)')
    Get = re.findall(isGet, url0)
    Get = "".join(Get)
    #Get=Get.encode("utf-8")
    #print Get
    # Get=Get[1:]
    isHost = re.compile(r'(Host:.+?;;)')
    Host = re.findall(isHost, url0)
    Host = "".join(Host)
    # Host0=Host[1:]
    #print Host
    isReferer = re.compile(r'(Referer:.+?;;)')
    Ref = re.findall(isReferer, url0)
    Ref = "".join(Ref)
    # print Ref
    isUser = re.compile(r'(User-Agent:.+?;;)')
    UAgent = re.findall(isUser, url0)
    UAgent = "".join(UAgent)

    isCookie = re.compile(r'(Cookie:.+?;;)')
    Cookie = re.findall(isCookie, url0)
    Cookie = "".join(Cookie)

    return Get, Host, Ref, UAgent, Cookie
def rexurl(url0):
    isGet = re.compile(r'[GE|POS]T(.+?)HTTP/1.[0|1];;')
    Get = re.findall(isGet, url0)
    Get = "".join(Get)[1:]
    #print Get
    #Get=Get[1:]
    isHost = re.compile(r'Host:(.+?);;')
    Host = re.findall(isHost, url0)
    Host = "".join(Host)[1:]
    #Host0=Host[1:]
    #print Host
    isReferer = re.compile(r'Referer:(.+?);;')
    Ref = re.findall(isReferer, url0)
    Ref = "".join(Ref)[1:]
    #print Ref
    isUser = re.compile(r'User-Agent:(.+?);;')
    UAgent = re.findall(isUser, url0)
    UAgent = "".join(UAgent)[1:]

    isCookie =re.compile(r'Cookie:(.+?);;')
    Cookie= re.findall(isCookie,url0)
    Cookie= "".join(Cookie)[1:]

    return Get, Host, Ref, UAgent,Cookie


def rexua(UAgent):
    li = ['chrome', 'Mozilla', 'AppleWebKit', 'Safari', 'Linux']
    uach = []
    for ch in li:
        ch = ch.lower()
        uag = UAgent.lower()
        if ch in uag:
            uach.append(ch)
        else:
            continue
    if len(uach) != 0:
        return 1
    else:
        return 0

def host(Host, h_totals):
    if Host not in h_totals:
        h_totals[Host] = 1
    else:
        h_totals[Host] = h_totals[Host] + 1
    return h_totals

def get(Get,g_totals):
    if Get not in g_totals:
        g_totals[Get]=1
    else:
        g_totals[Get]=g_totals[Get]+1
    return g_totals

def ref(Ref, r_totals):
    if Ref not in r_totals:
        r_totals[Ref] = 1
    else:
        r_totals[Ref] = r_totals[Ref] + 1
    return r_totals

def uaf(UAgent, u_totals):
    if UAgent not in u_totals:
        u_totals[UAgent] = 1
    else:
        u_totals[UAgent] = u_totals[UAgent] + 1
    return u_totals

def cook(Cookie,c_totals):
    if Cookie not in c_totals:
        c_totals[Cookie]=1
    else:
        c_totals[Cookie]=c_totals[Cookie]+1
    return c_totals

def classf(urls):
    host00={}
    host01={}
    host10={}
    host11={}
    get00={}
    get01={}
    get10={}
    get11={}
    ua00={}
    ua01={}
    ua10={}
    ua11={}
    #u_totals={}
    urls00={}
    urls01={}
    urls10={}
    urls11={}
    ref10={}
    ref11={}
    cookie00={}
    cookie01={}
    cookie10={}
    cookie11={}
    #urls0=urls
    #ua=0
    for fname1 in urls.keys():


        surl1 = urls[fname1]
        url0 = surl1.replace('\t', '').replace('\n', ';;')

        #print fname0,surl0
        Get, Host, Ref, UAgent,Cookie= rexurl(url0)

        #print Ref,'\n',UAgent

        #global ua
        ua=rexua(UAgent)
        #print ua
        if len(Ref)!=0:
            if ua==0:
                urls10[fname1]=surl1
                host10=host(Host,host10)
                ref10=ref(Ref,ref10)
                ua10=uaf(UAgent,ua10)
                get10=get(Get,get10)
                cookie10=cook(Cookie,cookie10)
            else:
                urls11[fname1]=surl1
                host11=host(Host,host11)
                ref11=ref(Ref,ref11)
                ua11 = uaf(UAgent, ua11)
                get11= get(Get, get11)
                cookie11= cook(Cookie, cookie11)

        else:
            if ua==0:
                urls00[fname1]=surl1
                host00=host(Host,host00)
                ua00 = uaf(UAgent, ua00)
                get00= get(Get, get00)
                cookie00 = cook(Cookie, cookie00)
            else:
                urls01[fname1]=surl1
                host01=host(Host,host01)
                ua01=uaf(UAgent, ua01)
                get01 = get(Get, get01)
                cookie01 = cook(Cookie, cookie01)

    return urls00,urls01,urls10,urls11,host00,host01,host10,host11,ref10,ref11,ua00,ua01,ua10,ua11,get00,get01,get10,get11,cookie00,cookie01,cookie10,cookie11

def classurlphone(results):
    host00={}
    host01={}
    host10={}
    host11={}
    get00={}
    get01={}
    get10={}
    get11={}
    ua00={}
    ua01={}
    ua10={}
    ua11={}
    #u_totals={}
    urls00={}
    urls01={}
    urls10={}
    urls11={}
    ref10={}
    ref11={}
    cookie00={}
    cookie01={}
    cookie10={}
    cookie11={}
    #urls0=urls
    #ua=0
    for row in results:
        # fname1 = row[1].encode("utf-8")
        # surl1 = row[2].encode("utf-8")
        # #surl1 = urls[fname1]
        # url0 = surl1.replace('\t', '').replace('\n', ';;')
        #print fname0,surl0
        fname1 = row[1]
        surl1 = row[3].encode("utf-8")
        surl1 = surl1.replace('\t', '').replace('\n', ';;')
        Get, Host, Ref, UAgent,Cookie= rexurl(surl1)
        # print fname1
        # print "Get:",Get
        # print "Ref:",Ref

        # if len(Get)==0:
        #     print fname1
        #print Ref,'\n',UAgent
        #global ua
        ua=rexua(UAgent)
        if len(Get)==0:
            continue
        else:
            if len(Ref)!=0:
                if ua==0:
                    urls10[fname1]=surl1
                    host10=host(Host,host10)
                    ref10=ref(Ref,ref10)
                    ua10=uaf(UAgent,ua10)
                    get10=get(Get,get10)
                    cookie10=cook(Cookie,cookie10)
                else:
                    urls11[fname1]=surl1
                    host11=host(Host,host11)
                    ref11=ref(Ref,ref11)
                    ua11 = uaf(UAgent, ua11)
                    get11= get(Get, get11)
                    cookie11= cook(Cookie, cookie11)

            else:
                if ua==0:
                    urls00[fname1]=surl1
                    host00=host(Host,host00)
                    ua00 = uaf(UAgent, ua00)
                    get00= get(Get, get00)
                    cookie00 = cook(Cookie, cookie00)
                else:
                    urls01[fname1]=surl1
                    host01=host(Host,host01)
                    ua01=uaf(UAgent, ua01)
                    get01 = get(Get, get01)
                    cookie01 = cook(Cookie, cookie01)

    return urls00,urls01,urls10,urls11,host00,host01,host10,host11,ref10,ref11,ua00,ua01,ua10,ua11,get00,get01,get10,get11,cookie00,cookie01,cookie10,cookie11




def hof(Host):
    rehost = 'http://' + Host
    rehost = get_tld(rehost)
    return rehost


def fsoft(urls00, urls10):
    softs = {}
    others = {}
    for k00 in urls00.keys():
        fname00 = k00
        surl00 = urls00[k00]
        url00 = surl00.replace('\t', '').replace('\n', ';;')
        Get00, Host00, Ref00, UAgent00,Cookie00 = rexurl(url00)
        print Get00
        f00 = soft(Get00, Host00, Ref00, UAgent00)
        for k10 in urls10.keys():
            # global fname10
            # global surl10
            fname10 = k10
            surl10 = urls00[k10]
            url10 = surl10.replace('\t', '').replace('\n', ';;')
            Get10, Host10, Ref10, UAgent10 ,Cookie10= rexurl(url10)
            Hos00 = hof(Host00)
            Hos10 = hof(Host10)
            f10 = soft(Get10, Host10, Ref10, UAgent10)
            if Host00 == Host10:
                softs[fname10] = surl10
            elif Host00 == Ref10:
                softs[fname10] = surl10
            elif Hos00 == Hos10:
                softs[fname10] = surl10
            elif f10 == 0:
                softs[fname10] = surl10
            else:
                continue
        if len(softs) != 0:
            softs[fname00] = surl00
        elif f00 == 0:
            softs[fname00] = surl00
        else:
            others[fname00] = surl00
            others[fname10] = surl10
    return softs, others


# def user(urls01,urls11,host10,host11,ref10,ref11):
