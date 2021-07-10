from util import responseCode
from dao.notice import notice_showall
import settings


def get_notice():
    notice_list = notice_showall.show(settings.ip)
    if notice_list is None:
        return responseCode.resp_4xx(code=400, message='没有新的公告可以显示')
    notice_dic_list = []
    for i in notice_list:
        notice_dic_list.append({
            "notice_id": i[0],
            "user_id": i[1],
            "content": i[2],
            "title": i[3],
            "notice_level": i[4],
            "notice_create_time": i[5]
        })
    return responseCode.resp_200(data=notice_dic_list)
