import re
from tld import get_tld
def rexurlmm(url0):
    urls=[]
    iset = re.compile(r'(.+?HTTP/1.[0|1];;)')
    get=re.findall(iset,url0)
    get = "".join(get)
    gets=get.split(" ")
    Action=gets[0]
    if len(Action)==0:
        Action='0'
    else:
        urls.append(Action)
    isGet = re.compile(r'[GE|POS]T(.+?)HTTP/1.[0|1];;')
    Get = re.findall(isGet, url0)
    Get = "".join(Get)[1:]
    if len(Get)==0:
        Get='0'
    else:
        urls.append(Get)

    isHost = re.compile(r'Host:(.+?);;')
    Host = re.findall(isHost, url0)
    Host = "".join(Host)[1:]
    if len(Host) == 0:
        Host= '0'
    else:
        urls.append(Host)
    #Host0=Host[1:]
    #print Host
    isReferer = re.compile(r'Referer:(.+?);;')
    Ref = re.findall(isReferer, url0)
    Ref = "".join(Ref)[1:]
    if len(Ref)==0:
        Ref='0'
    else:
        urls.append(Ref)
    isUser = re.compile(r'User-Agent:(.+?);;')
    UAgent = re.findall(isUser, url0)
    UAgent = "".join(UAgent)[1:]
    if len(UAgent) == 0:
        UAgent= '0'
    else:
        urls.append(UAgent)
    isCookie =re.compile(r'Cookie:(.+?);;')
    Cookie= re.findall(isCookie,url0)
    Cookie= "".join(Cookie)[1:]
    if len(Cookie) == 0:
        Cookie= '0'
    else:
        urls.append(Cookie)
    isConnection= re.compile(r'Connection:(.+?);;')
    Connection= re.findall(isConnection, url0)
    Connection= "".join(Connection)[1:]
    if len(Connection) == 0:
        Connection = '0'
    else:
        urls.append(Connection)
    isAccept= re.compile(r'Accept:(.+?);;')
    Accept = re.findall(isAccept, url0)
    Accept = "".join(Accept)[1:]
    if len(Accept) == 0:
        Accept = '0'
    else:
        urls.append(Accept)
    isAcceptCharset=re.compile(r'Accept-Charset:(.+?);;')
    AcceptCharset = re.findall(isAcceptCharset, url0)
    AcceptCharset= "".join(AcceptCharset)[1:]
    if len(AcceptCharset) == 0:
        AcceptCharset = '0'
    else:
        urls.append(AcceptCharset)
    isAcceptEncoding= re.compile(r'Accept-Encoding:(.+?);;')
    AcceptEncoding= re.findall(isAcceptEncoding, url0)
    AcceptEncoding= "".join(AcceptEncoding)[1:]
    if len(AcceptEncoding) == 0:
        AcceptEncoding = '0'
    else:
        urls.append(AcceptEncoding)
    isContentLength = re.compile(r'Content-Length:(.+?);;')
    ContentLength = re.findall(isContentLength , url0)
    ContentLength = "".join(ContentLength )[1:]
    if len(ContentLength) == 0:
        ContentLength = '0'
    else:
        urls.append(ContentLength)
    isAcceptLanguage = re.compile(r'Accept-Language:(.+?);;')
    AcceptLanguage= re.findall(isAcceptLanguage, url0)
    AcceptLanguage= "".join(AcceptLanguage)[1:]
    if len(AcceptLanguage) == 0:
        AcceptLanguage = '0'
    else:
        urls.append(AcceptLanguage)
    isAccetpRanges= re.compile(r'Accetp-Ranges:(.+?);;')
    AccetpRanges= re.findall(isAccetpRanges, url0)
    AccetpRanges= "".join(AccetpRanges)[1:]
    if len(AccetpRanges) == 0:
        AccetpRanges= '0'
    else:
        urls.append(AccetpRanges)
    # isAge = re.compile(r'Age:(.+?);;')
    # Age= re.findall(isAge, url0)
    # Age= "".join(Age)[1:]

    isAuthorization= re.compile(r'Authorization:(.+?);;')
    Authorization = re.findall(isAuthorization, url0)
    Authorization= "".join(Authorization)[1:]
    if len(Authorization) == 0:
        Authorization = '0'
    else:
        urls.append(Authorization)
    isCacheControl= re.compile(r'Cache-Control:(.+?);;')
    CacheControl= re.findall(isCacheControl, url0)
    CacheControl= "".join(CacheControl)[1:]
    if len(CacheControl) == 0:
        CacheControl = '0'
    else:
        urls.append(CacheControl)
    isContentType= re.compile(r'Content-Type:(.+?);;')
    ContentType= re.findall(isContentType, url0)
    ContentType= "".join(ContentType)[1:]
    if len(ContentType) == 0:
        ContentType = '0'
    else:
        urls.append(ContentType)
    isDate = re.compile(r'Date:(.+?);;')
    Date= re.findall(isDate, url0)
    Date= "".join(Date)[1:]
    if len(Date) == 0:
        Date = '0'
    else:
        urls.append(Date )
    isExpect= re.compile(r'Expect:(.+?);;')
    Expect= re.findall(isExpect, url0)
    Expect= "".join(Expect)[1:]
    if len(Expect) == 0:
        Expect = '0'
    else:
        urls.append(Expect)
    isFrom= re.compile(r'From:(.+?);;')
    Froms= re.findall(isFrom, url0)
    Froms= "".join(Froms)[1:]
    #print From
    if len(Froms) == 0:
        Froms='0'
    else:
        urls.append(Froms)
    #print From  From
    isIfMatch = re.compile(r'If-Match:(.+?);;')
    IfMatch= re.findall(isIfMatch, url0)
    IfMatch= "".join(IfMatch)[1:]
    if len(IfMatch) == 0:
        IfMatch = '0'
    else:
        urls.append(IfMatch)

    isIfModifiedSince= re.compile(r'If-Modified-Since:(.+?);;')
    IfModifiedSince= re.findall(isIfModifiedSince, url0)
    IfModifiedSince= "".join(IfModifiedSince)[1:]
    if len(IfModifiedSince) == 0:
        IfModifiedSince = '0'
    else:
        urls.append(IfModifiedSince)

    isIfNoneMatch = re.compile(r'If-None-Match:(.+?);;')
    IfNoneMatch = re.findall(isIfNoneMatch, url0)
    IfNoneMatch = "".join(IfNoneMatch)[1:]
    if len(IfNoneMatch ) == 0:
        IfNoneMatch = '0'
    else:
        urls.append(IfNoneMatch)

    isIfRange= re.compile(r'If-Range:(.+?);;')
    IfRange = re.findall(isIfRange, url0)
    IfRange = "".join(IfRange )[1:]
    if len(IfRange) == 0:
        IfRange = '0'
    else:
        urls.append(IfRange)

    isIfUnmodifiedSince= re.compile(r'If-Unmodified-Since:(.+?);;')
    IfUnmodifiedSince= re.findall(isIfUnmodifiedSince, url0)
    IfUnmodifiedSince= "".join(IfUnmodifiedSince)[1:]
    if len(IfUnmodifiedSince) == 0:
        IfUnmodifiedSince = '0'
    else:
        urls.append(IfUnmodifiedSince)

    isMaxForwards = re.compile(r'Max-Forwards:(.+?);;')
    MaxForwards = re.findall(isMaxForwards, url0)
    MaxForwards = "".join(MaxForwards)[1:]
    if len(MaxForwards) == 0:
        MaxForwards = '0'
    else:
        urls.append(MaxForwards)

    isPragma= re.compile(r'Pragma:(.+?);;')
    Pragma= re.findall(isPragma, url0)
    Pragma= "".join(Pragma)[1:]
    if len(Pragma) == 0:
        Pragma= '0'
    else:
        urls.append(Pragma)

    isProxyAuthorization = re.compile(r'Proxy-Authorization:(.+?);;')
    ProxyAuthorization = re.findall(isProxyAuthorization, url0)
    ProxyAuthorization = "".join(ProxyAuthorization)[1:]
    if len(ProxyAuthorization) == 0:
        ProxyAuthorization = '0'
    else:
        urls.append(ProxyAuthorization)


    isRange = re.compile(r'Range:(.+?);;')
    Ranges = re.findall(isRange, url0)
    Ranges = "".join(Ranges)[1:]
    if len(Ranges) == 0:
        Ranges = '0'
    else:
        urls.append(Ranges)

    isTE= re.compile(r'TE:(.+?);;')
    TE=re.findall(isTE, url0)
    TE= "".join(TE)[1:]
    #print len(TE)
    if len(TE) == 0:
        TE = '0'
    else:
        urls.append(TE)
        #print TE

    isUpgrade= re.compile(r'Upgrade:(.+?);;')
    Upgrade= re.findall(isUpgrade, url0)
    Upgrade= "".join(Upgrade)[1:]
    if len(Upgrade)==0:
        Upgrade='0'
    else:
        urls.append(Upgrade)

    isVia = re.compile(r'Via:(.+?);;')
    Via = re.findall(isVia, url0)
    Via= "".join(Via)[1:]
    if len(Via)==0:
        Via = '0'
    else:
        urls.append(Via)

    isWarning= re.compile(r'Warning:(.+?);;')
    Warning= re.findall(isWarning, url0)
    Warning= "".join(Warning)[1:]
    if len(Warning)==0:
        Warning='0'
    else:
        urls.append(Warning)

    return urls,Action, Get, Host, Ref, UAgent, Cookie,Connection, Accept, AcceptCharset, AcceptEncoding, \
    ContentLength,AcceptLanguage, AccetpRanges, Authorization, CacheControl, ContentType, \
    Date, Expect,Froms, IfMatch,IfModifiedSince, IfNoneMatch, IfRange, IfUnmodifiedSince, MaxForwards, \
    Pragma, ProxyAuthorization, Ranges, TE, Upgrade, Via, Warning




