from util import responseCode
from dao.notice import notice_create
from dao.food import food_create, food_delete, food_update
from dao.user import user_create
from dao.user import user_delete
from dao.user import user_showone
from dao.user import user_update
from dao.user import user_showall
from settings import ip
import schemas


def post_notice(info: schemas.PostNoticeInfo):
    result = notice_create.create(
        ip,
        info.user_id,
        info.content,
        info.title,
        info.notice_level
    )
    return responseCode.resp_200(data=result)


def show_profiles_list():
    profiles_list=user_showall.show(ip)
    if len(profiles_list)==0:
        return responseCode.resp_4xx(code=400,message="用户信息为空")
    profiles_dict_list=[]
    for i in profiles_list:
        profiles_dict_list.append({
            "user_id":i[0],
            "user_number":i[1],
            "user_name":i[2],
            "user_position":i[3],
            "user_img":i[4],
            "user_gender":i[5],
            "user_state":i[6]
        })
    return responseCode.resp_200(data=profiles_dict_list)


def add_meal(meal: schemas.FoodInfo):
    result = food_create.create(
        ip,
        meal.food_name,
        meal.food_info,
        meal.food_price,
        meal.food_recommend,
        meal.food_img
    )
    return responseCode.resp_200(data=result)


def remove_meal(meal_id):
    result = food_delete.delete(ip, meal_id)
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
        return responseCode.resp_4xx(code=400,message="输入的信息格式错误")


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

def remover_member(user_id: int):
    isSuccess = user_delete.delete(user_id)
    if isSuccess == True:
        return responseCode.resp_200(data = None)
    elif isSuccess == "admin":
        return responseCode.resp_4xx(code = 400, message = "不能删除管理员")
    else:
        return responseCode.resp_4xx(code = 400, message = "数据库出现错误")


def edit_profiles(user_id_a:int, user_id_b:int ,tag:int ,content:str):
    # 先获取这个id对应的职位，如果id不是管理员，则只能改自己的，如果是管理员，则可以改其他人的
    user_a, user_b = 0,0    # 这两个是对应a和b的职位，1为管理员

    dataRecieved, isSuccess = user_showone.show(user_id_a)
    if isSuccess == False:
        return responseCode.resp_4xx(code = 401, data = None, message = "获取id错误")
    user_a = dataRecieved[3]

    dataRecieved, isSuccess = user_showone.show(user_id_b)
    if isSuccess == False:
        return responseCode.resp_4xx(code = 401, data = None, message = "获取id错误")
    user_b = dataRecieved[3]

    dataRecieved, isSuccess = (),None   # 初始化这两个变量
    if user_a == 1 and user_b != 1: # 如果当前为管理员则可以随便改，但是不可以修改其他管理员
        if tag == 1:    # 1表示修改职位
            isSuccess = user_update.updatepos(user_id_b, int(content))
        elif tag == 2:  # 2表示修改密码
            isSuccess = user_update.updatepwd(user_id_b, content)
    elif user_a == user_b == 1 and user_id_a != user_id_b:  # 不可以修改其他管理员
        return responseCode.resp_4xx(code = 401, data = None, message = "不可以修改其他管理员")
    elif user_id_a == user_id_b:
        if tag == 1:    # 1表示修改头像
            isSuccess = user_update.updateimg(user_id_b, content)
        elif tag == 2:  # 2表示修改密码
            isSuccess = user_update.updatepwd(user_id_b, content)
    else:
        return responseCode.resp_4xx(code = 401, data = None, message = "此id没有修改其他用户信息的权限")
    return responseCode.resp_200(data = None)

def show_details(user_id:int):
    dataRecieved, isSuccess = user_showone.show(user_id)
    # {用户编号、用户工号、职位、密码、性别、登陆状态、姓名}
    dataResp = {
        "user_id": dataRecieved[0],
        "user_number": dataRecieved[1],
        'user_position': dataRecieved[3],
        'user_pwd':dataRecieved[6],
        'user_gender': dataRecieved[5],
        'user_state':dataRecieved[7],
        "user_name": dataRecieved[2],
    }
    if isSuccess == False:
        return responseCode.resp_4xx(code = 401, data = None, message = "数据库错误")
    else:
        return responseCode.resp_200(data = dataResp)


def modify_table_number(table_number:int):
    pass