from util import responseCode
from dao.user import user_logout
from dao.user import user_showone
from dao.user import user_update


def exit(id: int):
    isSuccess = user_logout.login(id)
    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


def get_profiles(user_id: int):
    dataRecieved, isSuccess = user_showone.show(user_id)
    # 用户编号、用户工号、用户姓名、职位
    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="数据库错误")
    else:
        dataResp = {}
        print(dataRecieved, isSuccess)
        dataResp["user_id"] = dataRecieved[0]
        dataResp["user_number"] = dataRecieved[1]
        dataResp["user_name"] = dataRecieved[2]
        dataResp['user_position'] = dataRecieved[3]
        return responseCode.resp_200(data=dataResp)


def get_profiles_details(user_id: int):
    dataRecieved, isSuccess = user_showone.show(user_id)
    # {用户编号，用户工号、职位、头像路径、性别、姓名}
    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="数据库错误")
    else:
        dataResp = {
            # "user_id": dataRecieved[0],
            "user_number": dataRecieved[1],
            'user_position': "管理员" if dataRecieved[3] == 1 else "后厨" if dataRecieved[3] == 3 else "服务员",
            'user_img': dataRecieved[4],
            'user_gender': "woman" if dataRecieved[5] == 1 else "man",
            "user_name": dataRecieved[2],
        }
        return responseCode.resp_200(data=dataResp)


def edit_profiles(user_id_a: int, user_id_b: int, tag: int, content: str):
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


def modify_image(file, user_id: int):
    dataResp = {
        "user_img":str
    }
    # 定义dataResp
    try:
        url = "http://124.70.200.142:8080/img/person/"+user_id+".jpg"
        # 这里根据user_id更换数据库人员的头像图片链接 
        path = "/root/tomcat/webapps/img/person/"+user_id+".jpg"
        with open(path, 'wb') as f:
            f.write(file)
        
        flag = user_update.updateimg(user_id,url)
        if flag == False:
            return responseCode.resp_4xx(code = 400, message = "数据库错误", data = None)

        dataResp["user_img"] = url
        print("运行了这里")
    except:
        return responseCode.resp_4xx(code = 400, message = "更换头像出错",data = None)
    return responseCode.resp_200(data =dataResp)
