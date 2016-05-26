def Realurl(userurl):
    #filepath = "E:/confg/urls.txt
    a=0
    click=0
    F1=0
    row = len(userurl)
    #print"row of Clickurl:",row
    realurl=[]
    no=[]
    #f1=open("D:/confg/ClickUrl1.txt",'r')
    f1=open("D:/confg/Click2.txt", 'r')
    #f1 = open("D:/confg/test/Click01.txt", 'r')
    #f2=open("E:/confg/RealUrl.txt","a")
    for line in f1.readlines():
        sfp = line.replace('\n','')
        #print sfp
        if len(line) != 1:
            click=click+1
            if sfp in userurl:
                #print sfp
                a=a+1
                realurl.append(sfp)
            else:
                no.append(sfp)
        else:
            break
    print "click:", click
    # print realurl
    Recall=float(a)/click
    R= round(Recall,3)
    Precise = float(a)/row
    P = round(Precise,3)
    F1=float(2*P*R)/(P+R)
    F1= round(F1,2)
    return F1,R,P,realurl,no