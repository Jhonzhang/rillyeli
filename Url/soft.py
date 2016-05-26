from confg2list import conf
from ClassPart4 import rexurl
#import re
pathofsoft=r"D:/confg/soft.txt"
charset=conf(pathofsoft)
# print charset
def soft(get,host,ref,uagent):
  for c in charset:
    if c in get:
      #print c
      return 0
    elif c in ref:
      #print c
      return 0
    elif c in uagent:
      #print c
      return 0
    elif c in host:
      #print c
      return 0
    else:
      continue

def soft1(get,host,ref,uagent):
  for c in charset:
    if c in get:
      print c
      return 0
    elif c in ref:
      print c
      return 0
    elif c in uagent:
      print c
      return 0
    elif c in host:
      print c
      return 0
    else:
      continue

url="GET http://rm.api.weibo.com/2/remind/push_count.json?trim_null=1&with_dm_group=0&with_settings=1&exclude_attitude=1&with_common_cmt=1&with_comment_attitude=1&with_common_attitude=1&with_moments=1&with_dm_unread=1&msgbox=true&with_page_group=1&with_chat_group=1&with_chat_group_notice=1&_pid=1&count=15&source=3818214747&status_type=0&callback=STK_146115688485446 HTTP/1.1;;Host: rm.api.weibo.com;;Referer: http://weibo.com/1939498534/DrGh1oYw1?from=page_1006061939498534_profile&wvr=6&mod=weibotime&type=comment;;User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36;;Cookie: UOR=www.sootoo.com,widget.weibo.com,news.ifeng.com; SUB=_2AkMgS_M6f8NhqwJRmP0XzGvnboh0yQnEiebDAHzsJxJjHlEe7T9lqCSDQ_e00lNBZc1Zw_5ZFtiw-_9TkA..; SUBP=0033WrSXqPxfM72-Ws9jqgMF55z29P9D9WhfgO6O9bCcyrCmisaVqWBL; _s_tentry=-; Apache=8359468904139.436.1461156882921; SINAGLOBAL=8359468904139.436.1461156882921; ULV=1461156883060:1:1:1:8359468904139.436.1461156882921:;;"
# url=url.encode("utf-8")
Get, Host, Ref, UAgent,Cookie= rexurl(url)
soft1(Get, Host, Ref, UAgent)
# get="http://pos.baidu.com/fchm?di=u2523041&dri=0&dis=4&dai=1&ps=542x0&coa=at%3D3%26rsi0%3D172%26rsi1%3D425%26pat%3D6%26tn%3DbaiduCustNativeAD%26rss1%3D%2523FFFFFF%26conBW%3D0%26adp%3D1%26ptt%3D0%26titFF%3D%2525E5%2525BE%2525AE%2525E8%2525BD%2525AF%2525E9%25259B%252585%2525E9%2525BB%252591%26titFS%3D14%26rss2%3D%2523000000%26titSU%3D0%26ptbg%3D90%26piw%3D130%26pih%3D80%26ptp%3D0&dcb=BAIDU_SSP_define&dtm=BAIDU_DUP_SETJSONADSLOT&dvi=0.0&dci=-1&dpt=none&tsr=0&tpr=1460796032725&ari=1&dbv=0&drs=3&pcs=-8x-8&pss=750x542&cfv=11&cpl=0&chi=1&cce=true&cec=utf-8&tlm=1460085051&ltu=http%3A%2F%2Fs.ap.wps.cn%2Fciba%2Fmini%2Findex.797c9a37.html%3Fmode%3Dlnp&ecd=1&psr=1440x900&par=1440x860&pis=-1x-1&ccd=24&cja=true&cmi=0&col=zh-CN&cdo=-1&tcn=1460796033&sz=172x425 "
# host="pos.baidu.com"
# ref=" http://s.ap.wps.cn/ciba/mini/index.797c9a37.html?mode=lnp"
# uagent="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/7.0)"
# soft(get,host,ref,uagent)

