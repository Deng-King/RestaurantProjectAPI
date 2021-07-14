from util import responseCode
from dao.user import user_login
import schemas


# 1.1登陆和身份验证功能
def login(info: schemas.LoginInfo):
    """
        :param info:一个包含登录信息的对象
        :return:用户编号、用户编号对应的身份
    """
    msg, user_id, position = user_login.login(info.user_number, info.user_pwd)  # 数据库中查询id是否存在，是否已经登陆
    if msg == '用户名错误':
        return responseCode.resp_4xx(code=401, message="用户不存在")
    elif msg == '用户已登录':
        # 否则返回已经登陆
        return responseCode.resp_4xx(code=401, message='该用户已经登陆')
    elif msg == '密码错误':
        # 否则返回已经登陆
        return responseCode.resp_4xx(code=401, message='密码错误')
    else:
        respData = {
            "user_id": user_id,
            "user_position": position,
        }
        return responseCode.resp_200(data=respData)
