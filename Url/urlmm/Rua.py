from ClassPart4 import *
from back import back
from url.check import *
from commonfun import http
def fitref(refs):
    frefs={}
    for re in refs.keys():
        numref=refs[re]
        #if numref>=2 and back(re)!=0:
        if numref >=1:
            frefs[re]=numref
    return frefs


def ReURL(ua,results):
    #print ua
    refs = {}
    #print refs
    userurl0=[]
    userurl1=[]
    realurl=[]
    URL=[]
    get01s={}
    getref={}
    #print ua
    for row in results:
        try:
            fnames = row[0].encode("utf-8")
            fd = fnames.split("|")
            times = fd[0].strip()
            url = row[1].encode("utf-8")
            surl = url.replace('\t', '').replace('\n', ';;')
            #print times
            Get, Host, Ref, UAgent, Cookie = rexurlg(surl)
            #print Get
            #if len(Get) == 0 and ua != UAgent:
            if UAgent==ua and len(Get) != 0:
                if len(Ref) == 0:
                    # print Get
                    if Get not in get01s:
                        # print len(Get)
                        get01s[Get] = 1
                    else:
                        get01s[Get]=get01s[Get] + 1
                else:
                    Ref = Ref.strip()
                    if http(Get)!=0:
                        getref[Get]=Ref
                        if Ref not in refs:
                            refs[Ref] = 1
                        else:
                            refs[Ref] = refs[Ref] + 1
                    else:
                        continue
            else:
                continue
        except:
            continue
    #print refs
    #print "len(refs):",refs
    for get0 in get01s.keys():
        get0 = get0.strip()
        #if get0 in refs.keys() and back(get0) != 0:
        if get0 in refs.keys():
            userurl0.append(get0)
    us=userurl0[:]
    #print us
    #print "len(us):",get01s
    refss = fitref(refs)
    #print "len(refss):",len(getref)
    userurl1GR={}
    for ref in refss.keys():
        ref = ref.strip()
        for getr in getref.keys():
            gref1 = getref[getr]
            getr = getr.strip()
            if ref == getr:
                #userurl1.append(gref1)
                userurl1GR[gref1]=getr
                if gref1 not in userurl1:
                    userurl1.append(gref1)
                #     userurl1GR[gref1]=getr
                else:
                    break

    # for urlgref in userurl1GR.keys():
    #     rget = userurl1GR[urlgref]
    #     #if urlgref in realurl and rget not in realurl:
    #     if urlgref in userurl1:
    #         if back(rget) != 0:
    #             URL.append(rget)
    #print "userurl1:",userurl1
    #print "len(userurl1)",len(userurl1)
    userurl0.extend(refss.keys())
    # print userurl0
    for url0 in userurl0:
        url0 = url0.strip()
        if url0 in userurl1:
            realurl.append(url0)

    for urlgref in userurl1GR.keys():
        rget = userurl1GR[urlgref]
        if urlgref in realurl and rget not in realurl:
        #if urlgref in  realurl:
            if back(rget) != 0:
                URL.append(rget)
    #print realurl
    #print "last:",URL
    #checklist(URL)
    # realurl.extend(us)

    URL.extend(us)
    #print realurl
    realurl.extend(URL)
    realurls1 = set(realurl)
    realurls2 = list(realurls1)
    #print realurls
    #print 'len of possible urls:', len(realurls)
    return realurls2