from ClassPart4 import *
from back import back
import chardet
from totTime import Caltime,maxtime,maxtime2
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


def usermt11(urls01, urls11, Realua):
    refs = {}
    userurl0 = []
    userurl1 = []
    realurl = []
    get01s = {}
    getref = {}
    #getTime={}
    gettimes={}
    # global gettime1
    # global gettime2
    gettime1 = {}
    gettime2 = {}
    gettime11 = {}
    gettime22 = {}
    # check()
    aas = 0
    urls = dict(urls01.items() + urls11.items())
    # print urls
    for fnames in urls.keys():
        fd=fnames.split("|")
        fname=fd[0].strip()
       #print type(fname)
        urls1 = urls[fnames]
        a = chardet.detect(urls1)
        # print fname
        # print urls1
        # print a
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
            if typs == "ascii":
                # aas = aas + 1
                # print "aas:", aas
                Get, Host, Ref, UAgent, Cookie = rexurl(urls1)
                # print UAgent
                if len(Get) != 0 and UAgent==Realua:
                    if Get not in gettimes:
                        gettimes[Get]=fname
                    else:
                        tims1=gettimes[Get]
                        if Caltime(tims1,fname)>120:
                            gettimes[Get]=fname
                            #print gettimes
                        else:
                            continue
                    # print fname,Get
                    # aas = aas + 1
                    # print "aas:", aas
                    #     aas = aas + 1
                    #     # print "aas:", aas
                    if len(Ref) == 0:
                        # print Get
                        #gettime1[Get]=fname
                        if Get not in get01s:
                            # print len(Get)
                            get01s[Get]=1
                            #gettime1[fname]=Get
                            gettime1[Get]=fname
                            #print gettime1
                        else:
                            get01s[Get] = get01s[Get] + 1
                            # tims1=gettime1[Get]
                            # if Caltime(tims1,fname)>120:
                            #     get01s[Get] = get01s[Get] + 1

                                #gettime1[fname] = Get

                    else:
                        # if UAgent==Realua:
                        # print fname
                        Ref = Ref.strip()
                        getref[Get] = Ref
                        #gettime2[Ref]=fname
                        if Ref not in refs:
                            refs[Ref] = 1
                            # gettime2[Ref] =fname
                            #gettime2[fname]=Ref
                        else:
                            refs[Ref]=refs[Ref] + 1
                            # tims2=gettime1[Ref]
                            # if Caltime(tims2, fname) > 120:
                            #     refs[Ref] = refs[Ref] + 1

                                #gettime2[fname] = Ref
        except:
            continue

    #print "gettimes:",len(gettime1)
    # for key in gettime1.keys():
    #     # keys=gettime1[key].encode("utf-8")
    #     # a = chardet.detect(keys)
    #     # print a
    #     key=key.strip()
    #     #print key
    #     #print gettime1[key]
    #     # print "http://www.genshuixue.com/cd/"
    #     st="http://edu.iqiyi.com/"
    #     # print chardet.detect(st)
    #     st1 = st.strip()
    #     #print st1
    #     if key==st1:
    #         print key
    #         key=key+" "
    #         print gettime1[key]
    #print gettime1['http://www.genshuixue.com/cd/']

    for get0s in get01s.keys():
        get0 = get0s.strip()
        if get0 in refs.keys() and back(get0)!=0:
            userurl0.append(get0)
            #print get0
            #get0=get0.strip()
            # fa1=gettime1[get0s]
            # #print fa1
            # gettime11[fa1]=get0s
    us = userurl0[:]
    #print gettime11
    # print "len(us):",len(us)
    refss = fitref(refs)
    for ref1 in refss.keys():
        ref = ref1.strip()
        for getr in getref.keys():
            gref1=getref[getr]
            getr=getr.strip()
            if ref==getr and back(getr)!=0:
                if gref1 not in userurl1:
                    userurl1.append(gref1)
                    # fa2=gettime2[ref1]
                    # #print fa2
                    # gettime22[fa2]=ref1
                else:
                    break

    #print len(userurl1)
    #print userurl1
    userurl0.extend(refs.keys())
    # print userurl0
    # gettime2s=gettime2[:]

    for url0 in userurl0:
        url0 = url0.strip()
        #print url0
        if url0 in userurl1:
            realurl.append(url0)
            # print url0
            # fa2=gettime2[url0]
            # print fa2
            # gettime22[fa2]=url0
            #realurl.extend(us)
    #print realurl
    #print gettime22
    # gettimes=dict(gettime1.items()+gettime2.items())
    # print gettimes

    realurl.extend(us)
    realurls1=set(realurl)
    realurls=list(realurls1)
    #print gettimes
    #maxT = maxtime2(gettimes, realurls)
    #print "maxT:",maxT
    print 'kkk:', len(realurls)
    return realurls,gettimes

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