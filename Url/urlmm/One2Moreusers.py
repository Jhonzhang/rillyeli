import sys
sys.path.append("F:/Url/url")
import mysql.connector
#from url.check import *
from user import *
from Realuser import Realurl
from url.pickurl import Realhost
from url.checksql import maxua
from url.UserMT import usermt
from url.UA import UAMbPc
from Fillter import *
from url.check import *
from class4 import *
from url.check import *
from dealua import DealUa2,DealUa1,dealurl,dealurl2
# filepath=r"E:\testdata\test1\raw"
# excep,account,fnamenum=putMysql(filepath)
# print excep,account,fnamenum
conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='browsers',
                                 use_unicode=True)
cursor = conn.cursor()
sql = "select fname, url, Gett, UserAgent from test2"
try:
  cursor.execute(sql)
  results = cursor.fetchall()
  # uas=UAMbPc(results)
  # print "*" * 80
  # check(uas)
  # DealUa1(uas,results)
  dealurl2(results)


except:
    print 'Error! check !!!'
conn.commit()
cursor.close()
conn.close()