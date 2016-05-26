# url="zhangs"+";;"+"lis"+";;"+"gets"+";;"
# print url
#
# s="GET https://www.telerik.com/UpdateCheck.aspx?isBeta=False HTTP/1.1;;Host: " \
#   "www.telerik.com;;Referer: http://fiddler2.com/client/4.6.2.2;;User-Agent: " \
#   "Fiddler/4.6.2.2 (.NET 4.0.30319.34011; WinNT 6.3.9600.0; zh-CN; 2xAMD64);;"
# print s
# Action="CET"
# GET="https://www.telerik.com/UpdateCheck.aspx?isBeta=False HTTP/1.1"
# Host="www.telerik.com"
# print Action+" "+GET+";;Host: "+Host
#
import re
# a="2016/5/8 11:24:42|00001_c.txt"
# b="2016/5/8 11:25:04|00020_c.txt"
# # res=re.compile(r'(.+)|')
# # fd=re.findall(res,a)
# fd1=a.split("|")
# print fd1[0].strip(" ")
# d={'za':'dd','df':'dfdf'}
# a="za"
# ds=a
# def ie(ies,UAgent):
#     a1=0
#     lenies=len(ies)
#     print lenies
#     for ch1 in ies:
#         if ch1 in UAgent:
#             a1 = a1 + 1
#     if a1==lenies:
#         return 0
# def ieUA(UAgent):
#
#     ie1=['Mozilla','compatible','MSIE','Windows','NT','Trident/']
#     ie2=['Mozilla','compatible','MSIE','Windows','NT']
#     ie3=['Mozilla','compatible','MSIE','Windows','NT','Trident/','.NET4','.NET CLR','Tablet PC']
#     ie4=['Mozilla','rv:','Windows','NT','like Gecko']
#     if ie(ie4,UAgent)==0:
#         return 0
# cha1="Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko"
# print ieUA(cha1)
# UAgent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
# if UAgent.startswith("Mozilla/"):
#     print UAgent
#
#
# a="dd"
# b="dds"
# if a!=b:
#     print "not equal!
# a="Mozilla/dffadfsdfasdfasddf"
# if a.startswith("Mozilla/"):
#     print "love china"

import time,datetime

#a="2012/8/16 1:28:33"
a="2016-05-18 22:06:6"
if "/" in a :
    a1 =datetime.datetime.strptime(a,"%Y/%m/%d %H:%M:%S")
else:
    a1 = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
print a1
print a
