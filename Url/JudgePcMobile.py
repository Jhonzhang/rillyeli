import mysql.connector
from ClassPart4 import *
from fclient import client
from mobilemain import mobile
from pcmain import pc
#from debugmain import  debug
from url.startnot import start
conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                               use_unicode=True)
cursor = conn.cursor()
ids=0
#sql = "select fname, url, Gett, UserAgent from url02  limit '%d','%d'+1000"
#sql2="select id ,fname from url02"
try:
    ids=0
    #cursor.execute("select fname, url, Gett, UserAgent from url02  limit '%s','%s'"  [%ids,%(ids+2000)])
    cursor.execute("select fname, url, Gett, UserAgent from url01")
    results = cursor.fetchall()
    rows = cursor.rowcount
    cursor.execute("select id ,fname from url01")
    results2 = cursor.fetchall()

    print rows
    back=client(results,rows)
    print back
    if back==0:
        maxTime1 =mobile(results)
        ids = start(results2, maxTime1)
        print "maxT1", maxTime1
    else:
        maxTime2=pc(results)
        ids=start(results2,maxTime2)
        print "maxT2id",ids


except:
    print "-" * 80
    print "bad Please check codes!"
