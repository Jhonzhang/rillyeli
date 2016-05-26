from ClassPart4 import *
from Realuser import Realurl
from url.pickurl import Realhost
from url.checksql import maxua
from url.UserMT import *
from url.UA import RealUAPC
from Fillter import *
from url.check import *
from url.UserRealUrl import *
from url.totTime import *
from debugmain import  debug,debug2,debug3
def pc(results):
    urls00, urls01, urls10, urls11, host00, host01, host10, \
    host11, ref10, ref11, ua00, ua01, ua10, ua11, get00, get01, \
    get10, get11, cookie00, cookie01, cookie10, cookie11 = classpc(results)
    print "-" * 80
    print "Testxx:", "urls, host, get, ua, cookie,ref"
    print "Test00:", len(urls00), len(host00), len(get00), len(ua00), len(cookie00)
    print "Test01:", len(urls01), len(host01), len(get01), len(ua01), len(cookie01)
    print "Test10:", len(urls10), len(host10), len(get10), len(ua10), len(cookie10), len(ref10)
    print "Test11:", len(urls11), len(host11), len(get11), len(ua11), len(cookie11), len(ref11)


    print "-" * 80
    realuas= RealUAPC(urls11)
    realurls=[]
    if len(realuas)!= 0:
        for realua in realuas:
            try:
                #print realua
                realurl=usermt1(urls01, urls11, realua)
                realurls.extend(realurl)
                #realurl ,gettimes= usermt11(urls01, urls11, realua)
                #print realurl

                # maxT = maxtime3(gettimes, realurls)
                # print "maxT",maxT

            except:
                continue
    else:
        print "not click url"

    print "number of possible urls:", len(realurls)
    F1, R, P, realurlLast = Realurl(realurls)
    print "F1:", F1
    print "Recall:", R
    print "Precise:", P
    print "userurl:", len(realurlLast)
    #checklist(realurls)
    debtime = debug3(realurls, results)
    return debtime
