from util import responseCode
from dao.notice import notice_create
from dao.user import user_create
import settings
import schemas


def post_notice(info: schemas.PostNoticeInfo):
    success=notice_create.create(
        settings.ip,
        info.user_id,
        info.content,
        info.title,
        info.notice_level
    )
    return responseCode.resp_200(data=success)

def create_member(user_number: str, user_position: int, user_gender: int, user_name: str):
    # user_number: str
    # user_position: int
    # user_gender: int
    # user_name: str
    msgRecived = user_create.create(number = user_number,
                    position = user_position,
                    gender = user_gender,
                    name = user_name)
    if msgRecived == '创建成功':
        return responseCode.resp_200(data = None)
    elif msgRecived == '用户已存在':
        return responseCode.resp_4xx(code = 400, message = "此工号已经存在")
    else:
        return responseCode.resp_4xx(code = 500, message = "数据库错误")

