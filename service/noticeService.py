from util import responseCode
from dao.notice import notice_showall
import settings


def get_notice():
    notice_list = notice_showall.show(settings.ip)
    if notice_list == None:
        return responseCode.resp_4xx(code=404, message='没有新的公告可以显示')
    return responseCode.resp_200(data=notice_list)
