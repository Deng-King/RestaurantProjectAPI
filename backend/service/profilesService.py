from util import responseCode
from dao.user import user_logout
from dao.user import user_showone
from dao.user import user_update
import time


def exit(id: int):
    isSuccess = user_logout.login(id)
    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


# 1.6获取个人信息概览
def get_profiles(user_id: int):
    """
        :param user_id:用户编号
        :return:字典：{用户编号、用户工号、用户姓名、职位}
    """
    dataReceived, isSuccess = user_showone.show(user_id)
    # 用户编号、用户工号、用户姓名、职位
    # dataReceived内容
    # user_id == dataReceived[0]
    # user_number == dataReceived[1]
    # user_name == dataReceived[2]
    # user_position == dataReceived[3]
    # user_img == dataReceived[4]
    # user_gender == dataReceived[5]
    # user_pwd == dataReceived[6]
    # user_state == dataReceived[7]

    if isSuccess == False:
        # 如果错误
        return responseCode.resp_4xx(code=401, data=None, message="数据库错误")
    else:
        dataResp = {}   # 初始化返回字典
        dataResp["user_id"] = dataReceived[0]
        dataResp["user_number"] = dataReceived[1]
        dataResp["user_name"] = dataReceived[2]
        dataResp['user_position'] = dataReceived[3]
        return responseCode.resp_200(data=dataResp)


# 1.4个人信息详细查询
def get_profiles_details(user_id: int):
    """
        :param user_id:用户编号
        :return:字典：{用户编号，用户工号、职位（字符串）、头像路径、性别(字符串)、姓名}
    """
    dataReceived, isSuccess = user_showone.show(user_id)
    # dataReceived详细内容如下
    # user_id == dataReceived[0]
    # user_number == dataReceived[1]
    # user_name == dataReceived[2]
    # user_position == dataReceived[3]
    # user_img == dataReceived[4]
    # user_gender == dataReceived[5]
    # user_pwd == dataReceived[6]
    # user_state == dataReceived[7]

    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="数据库错误")
    else:
        dataResp = {
            # "user_id": dataRecieved[0],
            "user_number": dataReceived[1],
            'user_position': "管理员" if dataReceived[3] == 1 else "后厨" if dataReceived[3] == 3 else "服务员",
            'user_img': dataReceived[4],
            'user_gender': "woman" if dataReceived[5] == 1 else "man",
            "user_name": dataReceived[2],
        }
        return responseCode.resp_200(data=dataResp)


# 1.3 修改个人信息功能
def edit_profiles(user_id_a: int, user_id_b: int, tag: int, content: str):
    """
    :param user_id_a: 执行修改操作的用户的编号
    :param user_id_b: 被修改的用户的编号
    :param tag: 用于选择修改内容，2是修改密码，1是修改头像
    :param content: 修改内容
    :return: 成功与否
    """
    # 先获取这个id对应的职位，如果id不是管理员，则只能改自己的，如果是管理员，则可以改其他人的
    user_a, user_b = 0, 0  # 这两个是对应a和b的职位，1为管理员

    dataRecieved, isSuccess = user_showone.show(user_id_a)
    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="获取id错误")
    user_a = dataRecieved[3]

    dataRecieved, isSuccess = user_showone.show(user_id_b)
    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="获取id错误")
    user_b = dataRecieved[3]

    dataRecieved, isSuccess = (), None  # 初始化这两个变量
    if user_a == 1 and user_b != 1:  # 如果当前为管理员则可以随便改，但是不可以修改其他管理员
        if tag == 1:  # 1表示修改头像
            isSuccess = user_update.updateimg(user_id_b, content)
        elif tag == 2:  # 2表示修改密码
            isSuccess = user_update.updatepwd(user_id_b, content)
    elif user_a == user_b == 1 and user_id_a != user_id_b:  # 不可以修改其他管理员
        return responseCode.resp_4xx(code=401, data=None, message="不可以修改其他管理员")
    elif user_id_a == user_id_b:
        if tag == 1:  # 1表示修改头像
            isSuccess = user_update.updateimg(user_id_b, content)
        elif tag == 2:  # 2表示修改密码
            isSuccess = user_update.updatepwd(user_id_b, content)
    else:
        return responseCode.resp_4xx(code=401, data=None, message="此id没有修改其他用户信息的权限")

    return responseCode.resp_200(data=None)


# 1.7 修改个人头像功能
def modify_image(file:bytes, user_id: int):
    """
        :param file:头像文件
        :param user_id:用户编号
        :return:成功与否
    """
    dataResp = {
        "user_img":str
    }
    # 定义dataResp
    try:
        # tick 是当前的时间(单位s)
        ticks = str(int(time.time()))
        url = "http://124.70.200.142:8080/img/person/" + ticks + ".jpg"
        # 这里根据user_id更换数据库人员的头像图片链接 
        path = "/root/tomcat/webapps/img/person/" + ticks + ".jpg"
        print("path="+path)
        with open(path, 'wb') as f:
            f.write(file)
        flag = user_update.updateimg(user_id,url)
        if flag == False:
            return responseCode.resp_4xx(code = 400, message = "数据库错误", data = None)
        dataResp["user_img"] = url
    except:
        return responseCode.resp_4xx(code = 400, message = "更换头像出错",data = None)
    return responseCode.resp_200(data =dataResp)
