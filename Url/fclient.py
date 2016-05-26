import chardet
def favf(Gets):
    favs=['favicon.','icon','logo.']
    for f in favs:
        if f in Gets:
            return 0

def common(UserAgent):
    account=0
    MobileUA1 = ['Mozilla', 'Mobile', 'Safari', 'KHTML', 'Gecko', 'AppleWebKit']
    for chs1 in MobileUA1:
        if chs1 in UserAgent:
            account=account+1
    if account==6:
        return 0
def specile(UserAgent):
    MobileUA2 = ['UCBrowser', 'MQQBrowser', 'MxBrowser', '2345Browser', 'SogouMobileBrowse',
                 'LieBaoFast', ' OPR', 'baidubrowse','MiuiBrowser']
    for ch in MobileUA2:
        if ch in UserAgent and common(UserAgent)==0:
            return 0

def fiphone(UserAgent):
    iphone=['iPhone', 'iPod','iPad']
    for ch1 in iphone:
        if ch1 in UserAgent and common(UserAgent)==0:
            return 0

def fandriod(UserAgent):
    andriod = ['Andriod', 'Linux']
    for ch2 in andriod:
        if ch2 in UserAgent and common(UserAgent)==0:
            return 0


def fget(Gett,UserAgent):
    MobileUrl = ['3g', 'wap','andriod.api']
    Gett = Gett.lower()
    for char1 in MobileUrl:
        if char1 in Gett and fandriod(UserAgent)==0:
            return 0


def mobile(UserAgent,Gett):
    if fiphone(UserAgent)==0:
        return 0
    elif specile(UserAgent)==0:
        return 0
    elif fget(Gett,UserAgent)==0:
        return 0
    elif favf(Gett)==0 and "Moblile" in UserAgent:
        return 0
    else:
        return 1

def client(results,rows):
    cont = 0
    for row in results:
        Gett = row[2].encode("utf-8")
        UserAgent = row[3].encode("utf-8")
        cont=cont+1
        #UserAgent=row[6].encode("utf-8")
        # print row
        back= mobile(UserAgent,Gett)
        #print usercount
        # print back,usercount
        # print len(usercount)
        #print "back:",back
        if back==0:
            return back
        else:
            continue
            # if back == 0:
            #     print "mobile"
            #     print usercount
          #     break
    if cont==rows:
        return 1
