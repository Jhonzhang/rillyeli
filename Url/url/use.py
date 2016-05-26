from softclass import rexurl
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

def useget(usergets,numget):
    userurls=[]
    for keyget0 in usergets.keys():
        keyget=usergets[keyget0]
        keyget=float(keyget)/numget
        if keyget>=0.2:
            #uerurl=
            userurls.append(keyget0)
    return userurls



def user(urls01,urls11):
    #ref1=soted(ref11,5)
    #refnum=len(ref1)
    userget0={}
    userget1={}
    #usergets=[]
    other={}
    for key11 in urls11.keys():
        Uurl11 = urls11[key11]
        url1 = Uurl11.replace('\t', '').replace('\n', ';;')
        Get1, Host1, Ref1, UAgent1 = rexurl(url1)

        for key01 in urls01.keys():
            Uurl01=urls01[key01]
            url0 = Uurl01.replace('\t', '').replace('\n', ';;')
            Get0, Host0, Ref0, UAgent0 = rexurl(url0)



            if Get0 not in userget0:
                if len(userget0)==0:
                    userget0[Get0]=1
                elif Ref0 in uersget0:
                    userget0[Get0] = userget0[Get0] + 1
                elif Ref1 in userget0:
                    userget0[Get0] = userget0[Get0] + 1
                else:
                    other[key01]=Uurl01
                    other[key11] = Uurl11


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
                    other[key11] = Uurl11


            else:
                userget1[Get1] = userget1[Get1] + 1
    #print userget0,userget1
    usergets=dict(userget0,**userget1)
    usernum=len(urls01)+len(urls11)
    usergets0=useget(usergets,usernum)
    return usergets0,other





