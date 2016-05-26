import sys
import os
import webbrowser
sys.path.append("libs")
from time import sleep
os.startfile("D:/win8/fiddler/Fiddler2/Fiddler.exe")
sleep(20)
def openbrower():
    filepath="D:/confg/ClickUrl1.txt"
    with open(filepath) as f:
        for line in f.readlines():
            if len(line)!=1:
                try:
                    webbrowser.open(line)
                    sleep(25)
                except:
                    continue
            else:
                break

def opensoft():
    filepath="D:/confg/opensoft.txt"
    with open(filepath) as f:
        for line in f.readlines():
            #print line
            sfp= line.replace('\\', '/').replace('\n','')
            if len(line) != 1:
                os.startfile(sfp)
                sleep(30)
            else:
                break


# def Realurl(userurl):
#     #filepath = "E:/confg/urls.txt
#     a=0
#     row=0
#     realurl=[]
#     f1=open("E:/confg/urls.txt",'r')
#     f2=open("E:/confg/RealUrl.txt","a")
#     for line in f1.readlines():
#         sfp = line.replace('\n','')
#         #print "sfp0:",sfp
#         #sfp=" "+sfp
#         #print "sfp1:",sfp
#         if len(line) != 1:
#             row=row+1
#             if sfp in userurl:
#                 a=a+1
#                 realurl.append(sfp)
#
#     cvall = float(a) /row
#     cvall = round(cvall, 2)
#     return cvall,realurl

# userurl=[' http://www.111cn.net/phper/python/62060.htm',' http://music.baidu.com/']
# print userurl
# a=Realurl(userurl)
# print a
openbrower()
#opensoft()
    #fPath = filepath.replace('\\', '/')

    # while True:
    #     line = f.readline()
    #     #print type(line)
    #     if len(line)!=0:
    #         print line
    #         webbrowser.open(line)
    #         sleep(15)
    #     else:
    #         break