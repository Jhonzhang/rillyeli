#     print s
    #     lines=""
    #     for line in s:
    #         print line
    #         if line.startswith("GET"):
    #             lines=lines+line
    #         if line.startswith("POST"):
    #             lines=lines+line
    #         if line.startswith("Host"):
    #             lines = lines + line
    #         if line.startswith("User-Agent"):
    #             lines = lines + line
    #         if line.startswith("Cookie"):
    #             lines = lines + line
    #         if line.startswith("Referer"):
    #             lines = lines + line
    #     cursor.execute("insert into url7 (fname,url) values(%s,%s)", [fname, lines])
    #
     #print
        #continue
    #
# cursor.execute("insert into url00 (fname,url,Action, Gett, Host, Referer,"
#                "UserAgent) values(%s,%s,%s,%s,%s,%s,%s)",[fname,data,Action,Gett,Host,
#                                                             Ref, UAgent])
# cursor.execute("insert into url00 (fname,url,Action,"
#                "Gett,Host,Referer) values(%s,%s,%s,%s,%s,%s)", [fname,data,Action,Gett,Host,Ref])
# cursor.execute("insert into url00 (Cookie,Connection, Accept, AcceptCharset, AcceptEncoding,"
#             "ContentLength,AcceptLanguage, AccetpRanges) values(%s,%s,%s,%s,%s,%s,%s,%s)", [Cookie,Connection, Accept, AcceptCharset, AcceptEncoding,
#                                                                                             ContentLength,
#                                                                                             AcceptLanguage,
#                                                                                             AccetpRanges ])

# cursor.execute("insert into url00 (Authorization, CacheControl, ContentType,Date,Expect, Froms,"
#             "IfMatch,IfModifiedSince) values(%s,%s,%s,%s,%s,%s,%s,%s)", [Authorization, CacheControl, ContentType,Date,Expect, Froms,
#                                                                          IfMatch, IfModifiedSince])

# cursor.execute("insert into url00 (IfNoneMatch, IfRange, IfUnmodifiedSince, MaxForwards,"
#                "Pragma, ProxyAuthorization, Ranges, TE) values(%s,%s,%s,%s,%s,%s,%s,%s)",
#                [IfNoneMatch, IfRange, IfUnmodifiedSince, MaxForwards, Pragma, ProxyAuthorization,
#                 Ranges, TE,])
# cursor.execute("insert into url00 (UserAgent) values(%s)", [UAgent])

#print alls
    # url=Action+Get+Host+Ref+UAgent+Cookie+Connection+Accept+AcceptCharset+AcceptEncoding, \
    # ContentLength,AcceptLanguage, AccetpRanges, Authorization, CacheControl, ContentType, \
    # Date, Expect,From, IfMatch,IfModifiedSince, IfNoneMatch, IfRange, IfUnmodifiedSince, MaxForwards, \
    # Pragma, ProxyAuthorization, Range, TE, Upgrade, Via, Warning
    # #print fname,url
    #print type(url)
    #url=url.encode("utf-8")
    #print type(Get)
