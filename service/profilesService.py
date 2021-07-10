from util import responseCode
from dao.user import user_logout

def exit(id:int):
    isSuccess = user_logout.login(id)
    if isSuccess == False:
        return responseCode.resp_4xx(code = 401, data = None, message = "数据库错误")
    else:
        return responseCode.resp_200(data = None)
