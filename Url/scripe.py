#coding:utf-8
import re
# import requests
#
# r=requests.get("http://www.hao123.com/")
# data=r.text
#
# link_list=re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
# for url in link_list:
#     print url

from lxml import etree
import httplib2
import os

http=httplib2.Http()
response,content=http.request("http://www.hao123.com/woman")
#print content
tree=etree.HTML(content)
#print tree
#links=tree.xpath(u"//div[@class='study-sites']//a/@href")
links=tree.xpath(u"//div[@id='bd']//a/@href")
print len(links)
with open("D:\confg\ClickUrl2.txt","a+") as f:
    for link in links:
        print link
        f.writelines(link)
        f.write('\n')


    # def http(s):
    #     p=re.compile(r'^(https?://\w+(?:\.[^\.]+)+(?:/.+)*/.+\.html)?#?((?:/[^/]+)*)')
    #     url=re.findall(p,s)
    #     return url
    # a=filter(http,tree)
    # p=re.compile(r'^http(s)?://.+?')
    # for a in links:
    #     url = re.findall(p, a)
    #     if len(url)!=0:
    #         print a
    # for a in links:
    #     print type(a)
    #print type(link)
    # if link.startstwith("http"):
    #     print link

