from util import responseCode
from dao.notice import notice_showall
import settings


# 1.2获取公告消息功能
def get_notice():
    """
    :return: 所有公告组成的list，其中的公告是dict类型
    """

    # 获取公告list
    notice_list, isSuccess = notice_showall.show(settings.ip)  
    # notice_list中的内容有：
    # notice_id == notice_list[i][0]
    # user_id == notice_list[i][1]
    # user_name == notice_list[i][2]
    # notice_content == notice_list[i][3]
    # notice_title == notice_list[i][4]
    # notice_level == notice_list[i][5]
    # notice_create_time == notice_list[i][6]


    if not isSuccess:
        return responseCode.resp_4xx(code=400, message='数据库错误')
    if len(notice_list) == 0:
        # 如果公告列表中啥都没有
        return responseCode.resp_4xx(code=400, message='没有新的公告可以显示')

    # 将list转换为dict
    notice_dic_list = []
    
    # 遍历notice_list中的每一个元素
    for i in notice_list:
        notice_dic_list.append({
            "notice_id": i[0],
            "user_name": i[2],
            "content": i[3],
            "title": i[4],
            "notice_level": i[5],
            "notice_create_time": i[6]
        })
    return responseCode.resp_200(data=notice_dic_list)
