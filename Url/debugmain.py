from ClassPart4 import *
import datetime
from url.totTime import Caltime,maxtime,maxtime2
def debug(maxT,results):
    maxtimes = "2012-8-16 01:28:33"
    for row in results:
        fname1 = row[0].encode("utf-8")
        fd = fname1.split("|")
        fname = fd[0].strip()
        url = row[1].encode("utf-8")
        surl = url.replace('\t', '').replace('\n', ';;')
        # print surl1
        try:
            Get, Host, Ref, UAgent, Cookie = rexurl(surl)
            if len(Get) == 0:
                continue
            else:
                Ref=Ref.strip()
                if Ref in maxT.keys():
                    if "/" in fname:
                        date2= datetime.datetime.strptime(fname, "%Y/%m/%d %H:%M:%S")
                    else:
                        date2= datetime.datetime.strptime(fname, "%Y-%m-%d %H:%M:%S")
                    date1=datetime.datetime.strptime(maxtimes, "%Y-%m-%d %H:%M:%S")
                    #date2=datetime.datetime.strptime(fname, "%Y/%m/%d %H:%M:%S")
                    if date1<date2:
                        #print maxtimes
                        maxtimes=fname
                    else:
                        continue


                else:
                    continue


        except:
            continue

    #print maxtimes
    return maxtimes

def debug2(maxT,results):
    maxtimes = "2012/8/16 1:28:33"
    maxreftime={}
    for row in results:
        fname1 = row[0].encode("utf-8")
        fd=fname1.split("|")
        fname=fd[0].strip()
        url = row[1].encode("utf-8")
        surl = url.replace('\t', '').replace('\n', ';;')
        # print surl1

        try:
            Get, Host, Ref, UAgent, Cookie = rexurl(surl)
            if len(Get) == 0:
                continue
            else:
                Ref=Ref.strip()
                # if Ref in maxT.values():
                #     date1=datetime.datetime.strptime(maxtimes, "%Y/%m/%d %H:%M:%S")
                #     date2=datetime.datetime.strptime(fname, "%Y/%m/%d %H:%M:%S")
                #     if date1<date2:
                #         print maxtimes
                #         maxtimes=fname
                #     else:
                #         continue
                #
                #
                # else:
                #     continue
                for get in maxT.keys():
                    get=get.strip()
                    if get==Ref:
                        if len(maxreftime)==0:
                            maxtimes=fname
                        else:
                            maxtimes=maxreftime[Ref]
                        print maxtimes
                        date1 = datetime.datetime.strptime(maxtimes, "%Y/%m/%d %H:%M:%S")
                        date2=datetime.datetime.strptime(fname, "%Y/%m/%d %H:%M:%S")
                        if date1<date2:
                            #print maxtimes
                            #maxtimes=fname
                            maxreftime[Ref]=fname
                        else:
                            continue


        except:
            continue

    #print maxtimes
    return maxreftime

def debug3(maxT,results):
    maxtimes = "2012-08-16 01:28:33"
    for row in results:
        fname1 = row[0].encode("utf-8")
        fd = fname1.split("|")
        fname = fd[0].strip()
        url = row[1].encode("utf-8")
        #id= row[4].encode("utf-8")
        surl = url.replace('\t', '').replace('\n', ';;')
        #print fname1
        try:
            Get, Host, Ref, UAgent, Cookie = rexurl(surl)
            if len(Get) == 0 or "Mozilla/" not in UAgent:
                continue
            else:
                Ref=Ref.strip()
                if Ref in maxT:
                    if "/" in fname:
                        date2 = datetime.datetime.strptime(fname, "%Y/%m/%d %H:%M:%S")
                    else:
                        #print fname
                        date2 = datetime.datetime.strptime(fname, "%Y-%m-%d %H:%M:%S")
                    if "/" in maxtimes:
                        date1 = datetime.datetime.strptime(maxtimes, "%Y/%m/%d %H:%M:%S")
                    else:
                        # print fname
                        date1 = datetime.datetime.strptime(maxtimes, "%Y-%m-%d %H:%M:%S")
                    #date1 = datetime.datetime.strptime(maxtimes, "%Y-%m-%d %H:%M:%S")
                    # date1=datetime.datetime.strptime(maxtimes, "%Y/%m/%d %H:%M:%S")
                    # date2=datetime.datetime.strptime(fname, "%Y/%m/%d %H:%M:%S")
                    if date1<date2:
                        #print date2
                        maxtimes=fname

                    else:
                        continue


                else:
                    continue


        except:
            continue

    #print maxtimes
    return maxtimes