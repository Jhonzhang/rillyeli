from ClassPart4 import rexurl
def soted(d,n=2,m=1):
    a = sorted(d.items(), lambda x, y: cmp(x[1], y[1]))
    nu=0-(n+1)
    b=a[-1:nu:-1]
    numb=len(b)
    userhosts=[]
    for c in range(numb):
        bnum=b[c][1]
        if bnum>=m:
            userhost=b[c][0]
            userhosts.append(userhost)
    return userhosts
def add(x,y):
    return x+y
def soteuser(d):
    userurl=[]
    userother={}
    av=[]
    #lend=len(d)
    dvalue=d.values()
    sum = reduce(add,dvalue)
    #print "sum:",sum
    for ck in d.keys():
        cval=d[ck]
        #print ck
        cvall=float(cval)/sum
        cvall=round(cvall,5)
        av.append(cvall)
        if cvall>=0.04:
            userurl.append(ck)
        else:
            userother[ck]=cval

    return userurl,userother,av

def userurls(d):
    userurl=[]
    otherurl=[]
    threshold=16
    for refk in d.keys():
        if d[refk]>=threshold:
            userurl.append(refk)
        else:
            otherurl.append(refk)

    return userurl,otherurl

def useget(usergets,numget):
    userurls=[]
    for keyget0 in usergets.keys():
        keyget=usergets[keyget0]
        keyget=float(keyget)/numget
        if keyget>=0.2:
            #uerurl=
            userurls.append(keyget0)
    return userurls



def userf(urls01,urls11):
    #ref1=soted(ref11,5)
    #refnum=len(ref1)
    userget0={}
    userget1={}
    #usergets=[]
    other={}
    if len(urls11)!=0:
        for key11 in urls11.keys():
            Uurl11 = urls11[key11]
            url1 = Uurl11.replace('\t', '').replace('\n', ';;')
            Get1, Host1, Ref1, UAgent1 ,Cookie1= rexurl(url1)
            #print Get1,'GO',Ref1
            if len(urls01)!=0:
                for key01 in urls01.keys():
                    Uurl01=urls01[key01]
                    url0 = Uurl01.replace('\t', '').replace('\n', ';;')
                    Get0, Host0, Ref0, UAgent0 ,Cookie0= rexurl(url0)


                    if Get0 not in userget0:
                        if len(userget0)==0:
                            userget0[Get0]=1
                        elif Ref0 in userget0:
                            userget0[Get0] = userget0[Get0] + 1
                        elif Ref1 in userget0:
                            userget0[Get0] = userget0[Get0] + 1
                        else:
                            other[key01]=Uurl01
                            other[key11] = Uu
                    else:
                        userget0[Get0]=userget0[Get0]+1

                    if Get1 not in userget1:
                        if len(userget1) == 0:
                            userget1[Get1] = 1
                        elif Ref0 in uersget1:
                            userget1[Get1] = userget1[Get1] + 1
                        elif Ref1 in userget1:
                            userget1[Get1] = userget1[Get1] + 1
                        else:
                            other[key01] = Uurl01
                            other[key11] = Uurl1
                    else:
                        userget1[Get1] = userget1[Get1] + 1

            else:
                #print Get1, 'GO', Ref1
                if Get1 not in userget1:
                    if len(userget1)==0:
                        userget1[Get1]=1
                    else:
                        if Ref1 in userget1:
                            userget1[Ref1]=userget1[Ref1]+1
                        else:
                            userget1[Get1] =1

                else:
                    userget1[Get1]=userget1[Get1]+1

    print userget0,userget1
    usergets=dict(userget0,**userget1)

    usernum=len(urls01)+len(urls11)
    print usergets,usernum
    usergets0=useget(usergets,usernum)
    return usergets0,other
# def userf2(urls01,urls11,userurl):
#     #ref1=soted(ref11,5)
#     #refnum=len(ref1)
#     userget0={}
#     userget1={}
#     #usergets=[]
#     other={}
#     if len(urls11)!=0:
#         for key11 in urls11.keys():
#             Uurl11 = urls11[key11]
#             url1 = Uurl11.replace('\t', '').replace('\n', ';;')
#             Get1, Host1, Ref1, UAgent1 = rexurl(url1)
#             #print Get1,'GO',Ref1
#             if len(urls01)!=0:
#                 for key01 in urls01.keys():
#                     Uurl01=urls01[key01]
#                     url0 = Uurl01.replace('\t', '').replace('\n', ';;')
#                     Get0, Host0, Ref0, UAgent0 = rexurl(url0)
#
#
#                     if Get0 not in userget0:
#                         if len(userget0)==0:
#                             userget0[Get0]=1
#                         elif Ref0 in uersget0:
#                             userget0[Get0] = userget0[Get0] + 1
#                         elif Ref1 in userget0:
#                             userget0[Get0] = userget0[Get0] + 1
#                         else:
#                             other[key01]=Uurl01
#                             other[key11] = Uu
#                     else:
#                         userget0[Get0]=userget0[Get0]+1
#
#                     if Get1 not in userget1:
#                         if len(userget1) == 0:
#                             userget1[Get1] = 1
#                         elif Ref0 in uersget1:
#                             userget1[Get1] = userget1[Get1] + 1
#                         elif Ref1 in userget1:
#                             userget1[Get1] = userget1[Get1] + 1
#                         else:
#                             other[key01] = Uurl01
#                             other[key11] = Uurl1
#                     else:
#                         userget1[Get1] = userget1[Get1] + 1
#
#             else:
#                 #print Get1, 'GO', Ref1
#                 if Get1 not in userget1:
#                     if len(userget1)==0:
#                         userget1[Get1]=1
#                     else:
#                         if Ref1 in userget1:
#                             userget1[Ref1]=userget1[Ref1]+1
#                         else:
#                             userget1[Get1] =1
#
#                 else:
#                     userget1[Get1]=userget1[Get1]+1
#
#     print userget0,userget1
#     usergets=dict(userget0,**userget1)
#
#     usernum=len(urls01)+len(urls11)
#     print usergets,usernum
#     usergets0=useget(usergets,usernum)
#     return usergets0,other





