from util import responseCode
from dao.notice import notice_create
from dao.food import food_create, food_delete, food_update
from dao.user import user_create
from dao.user import user_delete
from dao.user import user_showone
from dao.user import user_update
from dao.user import user_showall
from dao.order import order_pay
from dao.table import table_create
from dao.table import table_delete
from dao.table import table_showall
from settings import ip
import schemas


def post_notice(info: schemas.PostNoticeInfo):
    result = notice_create.create(
        info.user_id,
        info.content,
        info.title,
        info.notice_level
    )
    return responseCode.resp_200(data=result)


def freeofcharge(order_id: int):
    isSuccess = order_pay.update(order_id, 2)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


def payment(order_id: int):
    isSuccess = order_pay.update(order_id, 1)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


def show_profiles_list():
    profiles_list, isSuccess = user_showall.show(ip)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(profiles_list) == 0:
        return responseCode.resp_4xx(code=400, message="用户信息为空")
    profiles_dict_list = []
    for i in profiles_list:
        profiles_dict_list.append({
            "user_id":i[0],
            "user_number":i[1],
            "user_name":i[2],
            "user_position":i[3],
            "user_img":i[4],
            "user_gender":i[5],
            "user_state":i[6],
            "show": False,
        })
    return responseCode.resp_200(data=profiles_dict_list)


def add_meal(food: schemas.AdminAddFood):
    result = food_create.create(
        ip,
        food.food_name,
        food.food_info,
        food.food_price,
        food.food_recommend,
    )
    if result == 0:
        return responseCode.resp_4xx(code=400, message="创建菜品失败")
    return responseCode.resp_200(data={"food_id": result})


def remove_meal(food_id):
    result = food_delete.delete(ip, food_id)
    return responseCode.resp_200(data=result)


def modify_meal(mod: schemas.ModifyMeal):
    if mod.type == "food_name":
        return responseCode.resp_200(data=food_update.updatename(
            ip, mod.id, mod.value
        ))
    elif mod.type == "food_info":
        return responseCode.resp_200(data=food_update.updateinfo(
            ip, mod.id, mod.value
        ))
    elif mod.type == "food_price":
        return responseCode.resp_200(data=food_update.updateprice(
            ip, mod.id, float(mod.value)
        ))
    elif mod.type == "meal.food_recommend":
        return responseCode.resp_200(data=food_update.updatermd(
            ip, mod.id, int(mod.value)
        ))
    elif mod.type == "food_img":
        return responseCode.resp_200(data=food_update.updateimg(
            ip, mod.id, mod.value
        ))
    else:
        return responseCode.resp_4xx(code=400, message="输入的信息格式错误")


def create_member(user_number: str, user_position: int, user_gender: int, user_name: str):
    # user_number: str
    # user_position: int
    # user_gender: int
    # user_name: str
    msgRecived = user_create.create(number=user_number,
                                    position=user_position,
                                    gender=user_gender,
                                    name=user_name)
    if msgRecived == '创建成功':
        return responseCode.resp_200(data=None)
    elif msgRecived == '用户已存在':
        return responseCode.resp_4xx(code=400, message="此工号已经存在")
    else:
        return responseCode.resp_4xx(code=500, message="数据库错误")


def remover_member(user_id: int):
    isSuccess = user_delete.delete(user_id)
    if isSuccess == True:
        return responseCode.resp_200(data=None)
    elif isSuccess == "admin":
        return responseCode.resp_4xx(code=400, message="不能删除管理员")
    else:
        return responseCode.resp_4xx(code=400, message="数据库出现错误")


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
        if tag == 1:  # 1表示修改职位
            isSuccess = user_update.updatepos(user_id_b, int(content))
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


def show_details(user_id: int):
    dataRecieved, isSuccess = user_showone.show(user_id)
    # {用户编号、用户工号、职位、密码、性别、登陆状态、姓名}
    dataResp = {
        "user_id": dataRecieved[0],
        "user_number": dataRecieved[1],
        'user_position': dataRecieved[3],
        'user_pwd': dataRecieved[6],
        'user_gender': dataRecieved[5],
        'user_state': dataRecieved[7],
        "user_name": dataRecieved[2],
    }
    if isSuccess == False:
        return responseCode.resp_4xx(code=401, data=None, message="数据库错误")
    else:
        return responseCode.resp_200(data=dataResp)


def modify_table_number(table_number:int):
    dataRecieved, isSuccess = table_showall.show()
    if isSuccess == False:
        return responseCode.resp_4xx(code = 400, message = "数据库错误", data = None)
    # 目前的桌子数量
    currentTableNum = len(dataRecieved) + 1
    
    # 这里要判断目前的桌子上面是否空闲
    # 一旦有任何一张桌子空闲则返回401无权限错误
    for table in dataRecieved:
        if table[1] == 1:
            return responseCode.resp_4xx(code = 401, message = "有桌位被占用，你没有权限修改桌子数量",data = None)
    
    # 下面有三种情况，小于等于和大于
    if table_number == currentTableNum:
        # 等于则返回错误
        return responseCode.resp_4xx(code = 400, message = "桌子数量相等",data = None)
    elif table_number < currentTableNum:
        # 如果修改的桌子数量比之前大，则删除桌子
        diff = abs(table_number - currentTableNum)
        # 因为是一次一次改的，某一次删除可能会出错
        # 要统计没有出错的数量是什么
        isSuccess = True
        delNum = 0
        for i in range(diff):
            flag = table_delete.delete()
            if flag == True:
                delNum += 1
            else:
                isSuccess = False
        # 下面的代码判断添加是否成功决定返回值
        if isSuccess == False:
            msg = "删除桌位请求出现错误，目前已成功删除" + str(i+1) + "张桌位"
            return responseCode.resp_4xx(code = 400, message = msg, data = None)
        else:
            return responseCode.resp_200(data = None)
    else:
        # 如果修改的桌子数量比之前小，则增加桌子
        diff = abs(table_number - currentTableNum)
        flag = table_create.create(diff)
        if flag == False:
            return responseCode.resp_4xx(code = 400, message = "数据库错误", data = None)
        return responseCode.resp_200(data = None)
    

def modify_food_image(file,food_id:int):
    try:
        url = "http://124.70.200.142:8080/img/food/" + food_id + ".jpg"
        # 这里根据food_id更换数据库食品的图片链接 
        path = "/root/tomcat/webapps/img/food/" + food_id + ".jpg"
        with open(path, 'wb') as f:
            f.write(file)
    except:
        return responseCode.resp_4xx(code=400, message="服务器错误", data=None)
    return responseCode.resp_200(data=None)