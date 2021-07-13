from util import responseCode
from dao.user import user_login


def login(user_number: str, user_pwd: str):
    msg,id,position = user_login.login(user_number,user_pwd) # 数据库中查询id是否存在，是否已经登陆
    if msg == '用户名错误':
        return responseCode.resp_4xx(code = 401, message = "用户不存在")
    elif msg == '用户已登录':
        # 否则返回已经登陆
        return responseCode.resp_4xx(code = 401, message = '该用户已经登陆')
    elif msg == '密码错误':
        # 否则返回已经登陆
        return responseCode.resp_4xx(code = 401, message = '密码错误')
    else:
        respData = {
            "user_id": id,
            "user_position": position,
        }
        return responseCode.resp_200(data = respData)
