# -*- coding: utf-8 -*-
import mysql.connector
import chardet
conn = mysql.connector.connect(host='192.168.20.50', user='root', password='root', port='3306', database='url',
                               use_unicode=True)
cursor = conn.cursor()
sql = "select tag1,tag2 from tb_6655"
tag1s={}
tag2s={}
a=0
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        tag1=row[0]
        tag2=row[1]
        #print type(tag11)
        tag11=tag1.encode("utf-8")
        tag22=tag2.encode("utf-8")
        #print chardet.detect(tag22)
        #print type(tag11)
        if tag11 not in tag1s:
            tag1s[tag11]=1
        else:
            tag1s[tag11]=tag1s[tag11]+1

        if tag22 not in tag2s:
            tag2s[tag22] = 1
        else:
            tag2s[tag22] = tag2s[tag22] + 1


    #print type(tag2s.keys())

except:
    a=a+1

print len(tag1s),tag1s
print len(tag2s),tag2s
print "bad of a:",a
# keyss=[]
for key in tag1s.keys():
    print key,tag1s[key]