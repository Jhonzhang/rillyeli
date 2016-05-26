from ClassPart4 import *
from back import back
from Rua import ReURL
from Realuser import Realurl
from url.check import *
def fitref(refs):
    frefs={}
    for re in refs.keys():
        numref=refs[re]
        if numref>=1 and back(re)!=0:
            frefs[re]=numref
    return frefs




# def RUA(ua,results):
#
#     refs = {}
#     userurl0 = []
#     userurl1 = []
#     realurl = []
#     get01s = {}
#     getref = {}
#     # print ua
#     for row in results:
#         try:
#             fnames = row[0].encode("utf-8")
#             fd = fnames.split("|")
#             times = fd[0].strip()
#             url = row[1].encode("utf-8")
#             surl = url.replace('\t', '').replace('\n', ';;')
#             # print surl1
#             Get, Host, Ref, UAgent, Cookie = rexurl(surl)
#
#             if len(Get) == 0 and ua != UAgent:
#                 continue
#             else:
#                 if len(Ref) == 0:
#                     # print Get
#                     if Get not in get01s:
#                         # print len(Get)
#                         get01s[Get] = 1
#                     else:
#                         get01s[Get] = get01s[Get] + 1
#                 else:
#                     # if UAgent==Realua:
#                     # print fname
#                     Ref = Ref.strip()
#                     getref[Get] = Ref
#                     if Ref not in refs:
#                         refs[Ref] = 1
#                     else:
#                         refs[Ref] = refs[Ref] + 1
#         except:
#             continue
#
#     for get0 in get01s.keys():
#         get0 = get0.strip()
#         if get0 in refs.keys() and back(get0) != 0:
#             userurl0.append(get0)
#     us=userurl0[:]
#     print us
#     print "len(us):",len(us)
#     refss = fitref(refs)
#     for ref in refss.keys():
#         ref = ref.strip()
#         for getr in getref.keys():
#             gref1 = getref[getr]
#             getr = getr.strip()
#             if ref == getr and back(getr) != 0:
#                 if gref1 not in userurl1:
#                     userurl1.append(gref1)
#                 else:
#                     break
#
#                     # print len(userurl1)
#     userurl0.extend(refs.keys())
#     # print userurl0
#     for url0 in userurl0:
#         url0 = url0.strip()
#         if url0 in userurl1:
#             realurl.append(url0)  # realurl.extend(us)
#
#     realurl.extend(us)
#     realurls1 = set(realurl)
#     realurls = list(realurls1)
#     realurlss = realurls[:]
#     #print realurls
#     print 'len of realurls:', len(realurlss)

def DealUa1(uas,results):
    countua = 0
    allurls=[]
    for ua in uas.keys():
        countua=countua+1
        ua = ua.strip()
        realurls1=ReURL(ua,results)
        allurls.extend(realurls1)
        #print realurls1
        #print "*"*60
        #print realurls
    print "*"*60
    print "number of possible urls:",len(allurls)
    if len(allurls)!=0:
        F1, R, P, realurl = Realurl(allurls)
        print "F1:", F1
        print "Recall:", R
        print "Precise:", P
        print "userurl:", len(realurl)
        checklist(realurl)

def DealUa2(uas,results):
    backurl = {}
    allurls=[]
    for ua in uas.keys():
        ua=ua.strip()
        refs = {}
        userurl0 = []
        userurl1 = []
        realurl = []
        get01s = {}
        getref = {}

        #print ua
        for row in results:
            try:
                fnames = row[0].encode("utf-8")
                fd = fnames.split("|")
                times = fd[0].strip()
                url = row[1].encode("utf-8")
                surl = url.replace('\t', '').replace('\n', ';;')
                # print surl1
                Get, Host, Ref, UAgent, Cookie = rexurlg(surl)
                if back(Get)!=0:
                    if len(Get) != 0 and ua==UAgent:
                        if len(Ref) == 0:
                            # print Get
                            if Get not in get01s:
                                # print len(Get)
                                get01s[Get] = 1
                            else:
                                get01s[Get] = get01s[Get] + 1
                        else:
                            # if UAgent==Realua:
                            # print fname
                            Ref = Ref.strip()
                            getref[Get] = Ref
                            if Ref not in refs:
                                refs[Ref] = 1
                            else:
                                refs[Ref] = refs[Ref] + 1
                else:
                    backurl[times]=Get
            except:
                continue
        allurls.extend(get01s.keys())
        allurls.extend(refs.keys())
    print "*" * 60
    print "number of possible urls:", len(allurls)
    if len(allurls) != 0:
        F1, R, P, realurl = Realurl(allurls)
        print "F1:", F1
        print "Recall:", R
        print "Precise:", P
        print "userurl:", len(realurl)
        checklist(realurl)


def dealurl(results):
    backurl = {}
    allurls=[]
    refs = {}
    userurl0 = []
    userurl1 = []
    realurl = []
    get01s = {}
    getref = {}
    acount=len(results)
    for row in results:
        try:

            fnames = row[0].encode("utf-8")
            fd = fnames.split("|")
            times = fd[0].strip()
            url = row[1].encode("utf-8")
            surl = url.replace('\t', '').replace('\n', ';;')
            # print surl1
            Get, Host, Ref, UAgent, Cookie = rexurlg(surl)
            if back(Get)!=0 and "Mozilla/" in UAgent:
                if len(Get) != 0:
                    if len(Ref) == 0:
                            # print Get
                            if Get not in get01s:
                                # print len(Get)
                                get01s[Get] = 1
                            else:
                                get01s[Get] = get01s[Get] + 1
                    else:
                            # if UAgent==Realua:
                            # print fname
                        Ref = Ref.strip()
                        getref[Get]=Ref
                        if Ref not in refs:
                            refs[Ref]=1
                        else:
                            refs[Ref]=refs[Ref] + 1
                else:
                    backurl[times]=Get
        except:
            continue
    allurls.extend(get01s.keys())

    #allurls.extend(getref.values())
    allurls.extend(refs.keys())
    print "*" * 60
    lenallurls=len(allurls)
    print "number of possible urls:", len(allurls)
    if len(allurls) != 0:
        F1, R, P, realurl ,nourl= Realurl(allurls)
        Leandegree =float(lenallurls)/acount
        Leandegree = round(Leandegree, 3)
        print "The original data:",acount
        print "F1:", F1
        print "Recall:", R
        print "Precise:", P
        print "Leandegree:",Leandegree
        print "userurl:", len(realurl)
        print "*" * 60
        checklist(nourl)
        print "*" * 60
        checklist(realurl)

def dealurl2(results):
    backurl = {}
    allurls=[]
    refs = {}
    userurl0=[]
    userurl1=[]
    realurl=[]
    get01s={}
    getref={}
    acount=len(results)
    backref=[]
    for row in results:
        try:
            fnames = row[0].encode("utf-8")
            fd = fnames.split("|")
            times = fd[0].strip()
            url = row[1].encode("utf-8")
            surl = url.replace('\t', '').replace('\n', ';;')
            # print surl1
            Get, Host, Ref, UAgent, Cookie = rexurlg(surl)
            if back(Get)!=0:
                if len(Get) != 0:
                    if len(Ref) == 0:
                            # print Get
                            if Get not in get01s:
                                # print len(Get)
                                get01s[Get] = 1
                            else:
                                get01s[Get] = get01s[Get] + 1
                    else:
                            # if UAgent==Realua:
                            # print fname
                        Ref = Ref.strip()
                        getref[Get]=Ref
                        if Ref not in refs:
                            refs[Ref]=1
                        else:
                            refs[Ref]=refs[Ref] + 1
                else:
                    backurl[times]=Get

            else:
                if Ref not in backref:
                    backref.append(Ref)

        except:
            continue
    allurls.extend(get01s.keys())

    #allurls.extend(getref.values())
    allurls.extend(backref)
    print "*" * 60
    lenallurls=len(allurls)
    print "number of possible urls:", len(allurls)
    if len(allurls) != 0:
        F1, R, P, realurl ,nourl= Realurl(allurls)
        Leandegree =float(lenallurls)/acount
        Leandegree = round(Leandegree, 3)
        print "The original data:",acount
        print "F1:", F1
        print "Recall:", R
        print "Precise:", P
        print "Leandegree:",Leandegree
        print "userurl:", len(realurl)
        print "*" * 60
        checklist(nourl)
        print "*" * 60
        checklist(realurl)