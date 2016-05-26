import datetime
from back import back
import chardet
#from datetime import *
import re
def Caltime(date1,date2):
    date1=datetime.datetime.strptime(date1,"%Y-%m-%d %H:%M:%S")
    date2=datetime.datetime.strptime(date2,"%Y-%m-%d %H:%M:%S")
    #print date2
    # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    if date2>date1:
        return (date2-date1).seconds
    else:
        return (date1-date2).seconds
def Caltime2(date1,date2):
    #print date2
    date1=datetime.datetime.strptime(date1,"%Y/%m/%d %H:%M:%S")
    date2=datetime.datetime.strptime(date2,"%Y/%m/%d %H:%M:%S")
    print date1
    print date2
    # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    return (date1-date2).seconds
    #print date1
    # if date1>date2:
    #     return date1
    # else:
    #     return date2

# d1="2016/4/25 10:7:55"
# d2="2016/4/25 10:7:31"
# Caltime2(d1,d2)
# fd=d1.split(' ')
# fd1=fd[0].split('/')
# fd2=fd[1].split(':')
# # res=re.compile(r'(.+?)')
# # fd=re.findall(res,d1)
# print fd
# print fd1
# print fd2
# date1="2012-08-16 01:28:33"
# date2="2012-08-16 01:28:34"
# a=Caltime2(date1,date2)
# aw=Caltime2(d11,d2)
# print aw

def maxtime(gettimes):
    maxT={}
    maxtime = "2015-12-31 23:55:59"
    lentime = len(gettimes)
    print "len(lentime):",lentime
    cont = 0
    for ti in gettimes.keys():
        cont = cont + 1
        # lentime=len(gettimes)
        ftime = ti.strip()
        maxtime = Caltime2(maxtime, ftime)
        if cont == lentime:
            maxT[maxtime] = gettimes[ti]
            return maxT

def maxtime2(gettimes,realurl):
    maxT={}
    urltime={}
    maxs=" "
    maxtimes = "2012/8/16 1:28:33"
    lentime = len(realurl)
    #print "len(lentime):",lentime
    cont = 0
    #print realurl
    for ti in gettimes.keys():
        ftime=gettimes[ti]
        ftime = ftime.strip()
        # ftime=ftime.replace('/','-')
        #print chardet.detect(ftime)

        # print ftime
        # cont = cont + 1
        # lentime=len(gettimes)
        tis=ti.strip()

        if back(tis)!=0 and tis in realurl:
            urltime[ftime]=tis
            #print maxtimes
            #print ftime
            cont = cont + 1
            #print tis
            date1 = datetime.datetime.strptime(maxtimes, "%Y/%m/%d %H:%M:%S")
            date2 = datetime.datetime.strptime(ftime, "%Y/%m/%d %H:%M:%S")
            #print cont
            if cont==lentime:
                maxT[maxtimes]=urltime[maxtimes]
                return maxT
            #print ftime

            #print date2
            # # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
            # # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
            # # return date1-date2
            # #print date1
            if date1 <date2:
                #cont = cont + 1
                #print cont
                maxtimes=ftime
                print maxtimes

                #print cont
                # cont = cont + 1
                # print cont
                #return date1
            else:
                continue
                # maxs =ftime
                #return date2
            # print maxs
            # maxtime2 = Caltime2(maxtime, ftime)
            # maxtime=maxtime2
            #print maxtime
            # maxT[maxtime] = gettimes[tis]
            # print ftime


        else:
            continue
    # if cont == lentime:
    #     return maxtimes

def maxtime3(gettimes,realurl):
    maxT={}
    urltime={}
    maxs=" "
    maxtimes = "2012/8/16 1:28:33"
    lentime = len(realurl)
    #print "len(lentime):",lentime
    cont = 0
    #print realurl
    for ti in gettimes.keys():
        ftime=gettimes[ti]
        ftime = ftime.strip()
        # ftime=ftime.replace('/','-')
        #print chardet.detect(ftime)

        # print ftime
        # cont = cont + 1
        # lentime=len(gettimes)
        tis=ti.strip()

        if back(tis)!=0 and tis in realurl:
            #urltime[ftime]=tis
            #print maxtimes
            #print ftime
            cont = cont + 1
            #print ftime,tis
            maxT[tis]=ftime
            # #print tis
            # date1 = datetime.datetime.strptime(maxtimes, "%Y/%m/%d %H:%M:%S")
            # date2 = datetime.datetime.strptime(ftime, "%Y/%m/%d %H:%M:%S")
            #print cont
            if cont==lentime:
                #maxT[maxtimes]=urltime[maxtimes]
                return maxT
            #print ftime

            #print date2
            # # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
            # # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
            # # return date1-date2
            # #print date1
            # if date1 <date2:
            #     #cont = cont + 1
            #     #print cont
            #     maxtimes=ftime
            #     print maxtimes

                #print cont
                # cont = cont + 1
                # print cont
                #return date1
            else:
                continue
                # maxs =ftime
                #return date2
            # print maxs
            # maxtime2 = Caltime2(maxtime, ftime)
            # maxtime=maxtime2
            #print maxtime
            # maxT[maxtime] = gettimes[tis]
            # print ftime


        else:
            continue
