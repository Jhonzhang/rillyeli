import re
import chardet
import mysql.connector
def charpick(files):
    path = r"D:\testdata\testsoft1\raw"
    path = path.replace('\\', '/')
    conn = mysql.connector.connect(host='127.0.0.1', user='rootztf', password='rootztf', port='3306', database='url',
                                   use_unicode=True)
    cursor = conn.cursor()

    for filename in files:
        #print chardet.detect(filename)
        with open(path + '/' + filename) as f1:
            data0 = f1.read()
            #print chardet.detect(data)
            data1=data0.decode("ISO-8859-2")
            data=data1.encode("utf-8")
            print chardet.detect(data)

            cursor.execute("insert into urlsoft2 (url) values (%s)",[data])









    conn.commit()
    cursor.close()
    conn.close()

files=['0002_c.txt', '0230_c.txt', '0231_c.txt', '0244_c.txt', '0261_c.txt', '0335_c.txt']
       # '0338_c.txt', '0399_c.txt', '0400_c.txt', '0408_c.txt', '0409_c.txt', '0783_c.txt',
       # '0786_c.txt', '0787_c.txt', '0788_c.txt', '0805_c.txt', '0806_c.txt', '0807_c.txt',
       # '0808_c.txt', '0810_c.txt', '0811_c.txt', '0812_c.txt', '0813_c.txt', '0814_c.txt',
       # '0815_c.txt', '0817_c.txt', '0819_c.txt', '0821_c.txt', '0823_c.txt', '0886_c.txt',
       # '0985_c.txt', '1071_c.txt', '1072_c.txt', '1073_c.txt', '1074_c.txt', '1075_c.txt',
       # '1076_c.txt', '1079_c.txt', '1080_c.txt', '1081_c.txt', '1468_c.txt', '1469_c.txt',
       # '1470_c.txt', '1842_c.txt', '1843_c.txt', '1844_c.txt', '1845_c.txt', '1846_c.txt',
       # '1847_c.txt', '1848_c.txt', '1851_c.txt', '1852_c.txt', '1853_c.txt', '1855_c.txt',
       # '1857_c.txt', '1858_c.txt', '1871_c.txt', '1878_c.txt', '1884_c.txt', '1888_c.txt',
       # '1891_c.txt', '1892_c.txt', '1893_c.txt', '1896_c.txt', '1897_c.txt', '1903_c.txt',
       # '1906_c.txt', '1920_c.txt', '1922_c.txt']

charpick(files)
