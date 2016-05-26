import re

def http(Get):
    res=re.compile(r'(http).+?')
    https=re.findall(res,Get)
    #print https
    if len(https)>1:
        return 0
    else:
        return 1
    #return https

# Get="http://pos.baidu.com/xclm?rdid=2251460&dc=2&di=u2251460&dri=0&dis=3&d" \
#     "ai=1&ps=0x0&dcb=BAIDU_SSP_define&dtm=BAIDU_DUP_SETJSONADSLOT&dvi=0.0&dci" \
#     "=-1&dpt=none&tsr=0&tpr=1463543485283&ti=%E9%AA%9E%E5%9E%AE%E6%86%A1&ari=1" \
#     "&dbv=2&drs=1&pcs=728x90&pss=728x0&cfv=0&cpl=29&chi=3&cce=true&cec=GBK&tlm=1" \
#     "440742533&ltu=http%3A%2F%2Fdetail.zol.com.cn%2Fnotebook_index%2Fsubcate16_218" \
#     "_list_1_s6327_8_2_0_1.html&liu=http%3A%2F%2Fpic.zol.com.cn%2F201508%2Fcriteo_" \
#     "product_728_0828.html&ltr=http%3A%2F%2Fdetail.zol.com.cn%2Fnotebook_index%2Fsubcate16_" \
#     "218_list_1_s6327_8_2_0_1.html&ecd=1&psr=1440x900&par=1440x860&pis=728x90&ccd=24&cja=tr" \
#     "ue&cmi=51&col=zh" \
#     "-CN&cdo=-1&tcn=1463543485&qn=5f0af3d49c766b85&tt=1463543485001.293.745.753"
# print http(Get)