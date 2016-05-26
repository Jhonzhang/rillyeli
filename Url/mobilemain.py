from ClassPart4 import *
from Realuser import Realurl
from url.pickurl import Realhost
from url.checksql import maxua
from url.UserMT import *
from url.UA import RealUAMobile
from Fillter import *
from url.check import *
import chardet
from debugmain import  debug,debug2,debug3


def mobile(results):
    urls00, urls01, urls10, urls11, host00, host01, host10, \
    host11, ref10, ref11, ua00, ua01, ua10, ua11, get00, get01, \
    get10, get11, cookie00, cookie01, cookie10, cookie11 = classpc(results)
    print "-" * 80
    print "Testxx:", "urls, host, get, ua, cookie,ref"
    print "Test00:", len(urls00), len(host00), len(get00), len(ua00), len(cookie00)
    print "Test01:", len(urls01), len(host01), len(get01), len(ua01), len(cookie01)
    print "Test10:", len(urls10), len(host10), len(get10), len(ua10), len(cookie10), len(ref10)
    print "Test11:", len(urls11), len(host11), len(get11), len(ua11), len(cookie11), len(ref11)
    #print ua00
    #check(ua00)
    # print "-" * 80
    # check(ua01)
    # print "-" * 80
    # check(ua11)
    # print chardet.detect(urls11)
    print "-" * 80
    realuas= RealUAMobile(urls11)
    #realua, uanum = RealUA(urls11, ua11)
    print realuas
    print "-" * 80
    Rurls=[]
    #usermt(urls01, urls11, realua)
    # print "Real UserAgent:",UserAgent
    for realua in realuas:
        try:
            realurl = usermt1(urls01, urls11,realua)
            Rurls.extend(realurl)

        except:
            continue
    print "Df:",Rurls
    datatime=debug3(Rurls,results)
    return datatime

    # print "-"*80
    # print checklist(realurl)
    # print "number of possible urls:", len(realurl)
    # sames0, nosames0, sam0 = check2d(get01, ref11)
    # sames1, nosames1, sam1 = check2d(get11, ref11)
    # # # same=dict(sames0,**sames1)
    # # same = dict(sames0.items() + sames1.items())
    # # sames2, nosames2, sam2 = check2d(ref11,same)
    # # sames3, nosames3, sam3 = check2get(get01, get11)
    # # sames4, nosames4, sam4 = check2d(host00, host11)
    # #     # print "sames1:",len(sames1)
    # check(sames0)
    # # print "-" * 80
    # # #check(sames1)
    # print "sames0:",len(sames0)
    # print "sames1:",len(sames1)
        # for g in sames0.keys():
        #     g = g.strip()
        #     if g in realurl:
        #         print g
        # F1, R, P, realurls = Realurl(realurl)
        # print "F1:", F1
        # print "Recall:", R
        # print "Precise:", P
        # print "userurl:", len(realurls)


    # # same=dict(sames0,**sames1)
    # same = dict(sames0.items() + sames1.items())
    # print "sames1:",len(sames0)
    # check(sames0)
    # print "-" * 80
    # for g in sames0.keys():
    #     g=g.strip()
    #     if g in realurl:
    #         print g

