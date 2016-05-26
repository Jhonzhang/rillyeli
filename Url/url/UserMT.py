from ClassPart4 import *
from back import back
import chardet
from check import check
def getu(get,refs,userurl1):
    get=get.strip()
    if back(get)!=0:
        if get in refs.keys() and refs[get]>=10:
            if len(userurl1)!=0:
                if get in userurl1:
                    return 0
def fitref(refs):
    frefs={}
    for re in refs.keys():
        numref=refs[re]
        if numref>=10 and back(re)!=0:
            frefs[re]=numref
    return frefs
def usermtpc(urls01,urls11,Realua):
    refs={}
    userurl0=[]
    userurl1=[]
    realurl=[]
    get01s={}
    getref={}
    #check()
    urls= dict(urls01.items() + urls11.items())
    # print urls
    for fname in urls:
        url=urls[fname]
        url=url.encode("utf-8")
        Get, Host, Ref, UAgent, Cookie = rexurl(url)
        if len(Get)!=0 and UAgent==Realua:
            if len(Ref)==0:
                if Get not in get01s:
                    get01s[Get]=1
                else:
                    get01s[Get]=get01s[Get]+1
            else:
                # if UAgent==Realua:
                    #print fname
                getref[Get]=Ref
                if Ref not in refs:
                    refs[Ref]=1
                else:
                    refs[Ref]=refs[Ref]+1

    refss=fitref(refs)  #simpile fittler T>=10
    for get0 in get01s.keys():
        # print "get0:",get0
        get0 = get0.strip()
        if get0 in refs.keys() and back(get0) != 0:
            userurl0.append(get0)
    us = userurl0[:]
    for ref in refss.keys():
        ref=ref.strip()
        for getr in getref.keys():
            gref1 = getref[getr]
            getr=getr.strip()
            if ref==getr and back(getr)!=0:
                if gref1 not in userurl1:
                    userurl1.append(gref1)
                else:
                    break

    userurl0.extend(refs.keys())
    for url0 in userurl0:
        url0=url0.strip()
        if url0 in userurl1:
           realurl.append(url0)

    realurl.extend(us)
    realurls1 = set(realurl)
    realurls = list(realurls1)
    return realurls

def usermt2(urls01,urls11,Realua):
    refs={}
    userurl0=[]
    userurl1=[]
    realurl=[]
    get01s={}
    getref={}
    #check()
    urls= dict(urls01.items() + urls11.items())
    # print urls
    for fname in urls:
        url=urls[fname]
        url=url.encode("utf-8")
        Get, Host, Ref, UAgent, Cookie = rexurl(url)
        if len(Get)!=0 and UAgent==Realua:
            if len(Ref)==0:
                if Get not in get01s:
                    get01s[Get]=1
                else:
                    get01s[Get]=get01s[Get]+1
            else:
                # if UAgent==Realua:
                    #print fname
                getref[Get]=Ref
                if Ref not in refs:
                    refs[Ref]=1
                else:
                    refs[Ref]=refs[Ref]+1

    refss=fitref(refs)  #simpile fittler T>=10
    for get0 in get01s.keys():
        # print "get0:",get0
        get0 = get0.strip()
        if get0 in refs.keys() and back(get0) != 0:
            userurl0.append(get0)
    us = userurl0[:]
    for ref in refss.keys():
        ref=ref.strip()
        for getr in getref.keys():
            gref1 = getref[getr]
            getr=getr.strip()
            if ref==getr and back(getr)!=0:
                if gref1 not in userurl1:
                    userurl1.append(gref1)
                else:
                    break


    userurl0.extend(refs.keys())
    for url0 in userurl0:
        url0=url0.strip()
        if url0 in userurl1:
           realurl.append(url0)

    realurl.extend(us)
    realurls1 = set(realurl)
    realurls = list(realurls1)
    return realurls

def usermt1(urls01, urls11, Realua):
        refs={}
        userurl0=[]
        userurl1=[]
        realurl=[]
        get01s={}
        getref={}
        #check()
        aas=0
        urls=dict(urls01.items() + urls11.items())
        #print urls
        for fname in urls.keys():
            urls1 = urls[fname]
            a=chardet.detect(urls1)
            typ=a['encoding']
            typs=typ.strip()
            try:
                if typs=="ascii":
                    Get, Host, Ref, UAgent, Cookie = rexurl(urls1)
                    if len(Get) != 0 and UAgent == Realua:
                        if len(Ref) == 0:
                            if Get not in get01s:
                                get01s[Get] = 1
                            else:
                                get01s[Get] = get01s[Get] + 1
                        else:
                            Ref=Ref.strip()
                            getref[Get] = Ref
                            if Ref not in refs:
                                refs[Ref] = 1
                            else:
                                refs[Ref] = refs[Ref] + 1
            except:
                continue

        for get0 in get01s.keys():
            get0=get0.strip()
            if get0 in refs.keys() and back(get0)!=0:
                userurl0.append(get0)
        us=userurl0[:]
        refss = fitref(refs)
        for ref in refss.keys():
            ref = ref.strip()
            for getr in getref.keys():
                gref1 = getref[getr]
                getr = getr.strip()
                if ref == getr and back(getr)!=0:
                    if gref1 not in userurl1:
                        userurl1.append(gref1)
                    else:
                        break

        userurl0.extend(refs.keys())
        for url0 in userurl0:
            url0 = url0.strip()
            if url0 in userurl1:
                realurl.append(url0)

        realurl.extend(us)
        realurls1=set(realurl)
        realurls=list(realurls1)

        print 'first judge realurls:',len(realurls)
        return realurls




def usermt(urls01, urls11, Realua):
    refs = {}
    userurl0=[]
    userurl1=[]
    realurl=[]
    get01s={}
    getref={}
    ac=0
    urls = dict(urls01.items() + urls11.items())
    for fname in urls.keys():
        urls1 = urls[fname]
        a = chardet.detect(urls1)
        #print fname
        # ac=ac+1
        # print urls1
        # print ac
        #print a
        typ = a['encoding']
        typs = typ.strip()
        # ap="\""+typs+"\""
        # #print ap
        # #print typ,type(typ)
        # data1 = urls1.decode(ap)
        # if ap!="ascii":
        #     #urlll = data1.encode("utf-8")
        #     print ap
        #     print "p"
        #     #print chardet.detect(urlll)
        # #print type(data1)
        #
        # #urlll= data1.encode("utf-8")
        # #print chardet.detect(urlll)

        try:
            Get, Host, Ref, UAgent, Cookie = rexurl(urls1)
            if len(Get) != 0 and UAgent == Realua:
                # ac = ac + 1
                # print urls1
                # print ac
                if len(Ref) == 0:
                    if Get not in get01s:
                        get01s[Get] = 1
                    else:
                        get01s[Get] = get01s[Get] + 1
                else:
                    Ref = Ref.strip()
                    getref[Get] = Ref
                    if Ref not in refs:
                        refs[Ref] = 1
                    else:
                        refs[Ref] = refs[Ref] + 1
        except:
            print fname
            continue

    for get0 in get01s.keys():
        get0 = get0.strip()
        if get0 in refs.keys() and back(get0) != 0:
            userurl0.append(get0)
    us = userurl0[:]
    print "len(us):",len(us)
    refss = fitref(refs)
    for ref in refss.keys():
        ref = ref.strip()
        for getr in getref.keys():
            gref1 = getref[getr]
            getr = getr.strip()
            if ref == getr and back(getr) != 0:
                if gref1 not in userurl1:
                    userurl1.append(gref1)
                else:
                    break

    # print len(userurl1)
    userurl0.extend(refs.keys())
    # print userurl0
    for url0 in userurl0:
        url0 = url0.strip()
        if url0 in userurl1:
            realurl.append(url0)  # realurl.extend(us)

    realurl.extend(us)
    realurls1 = set(realurl)
    realurls = list(realurls1)

    print 'kkk:', len(realurls)
    return realurls

    # for get1 in getref.keys():
    #     gref1=getref[get1]
    #     gref1=gref1.strip()
    #     #print "gref1",gref1
    #     if get0==gref1 and get0 in refs.keys():
    #         #print get0
    #         if get0 not in userurl0:
    #             userurl0.append(get0)
    #             userurl1.extend(userurl0)
    #             #print userurl1
    #     if getu(get1,refs,userurl1)==0:
    #         userurl1.append(get1)
    # print refs.keys()
    # print "aas:",aas
    # print "len(get01s):",len(get01s)
    # print "len(refs):", len(refs)
    # # check(fitref(refs))
    # # print refs
    # refss = fitref(refs)  # simpile fittler T>=10
    # # print "len(refss):", len(refss)