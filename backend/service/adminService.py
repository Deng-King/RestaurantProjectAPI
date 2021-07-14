from util import responseCode
from dao.notice import notice_create
from dao.food import food_create, food_delete, food_update
from dao.food import food_showone
from dao.food import food_update
from dao.user import user_create
from dao.user import user_delete
from dao.user import user_showone
from dao.user import user_update
from dao.user import user_showall
from dao.order import order_pay
from dao.order import order_showall
from dao.table import table_create
from dao.table import table_delete
from dao.table import table_showall
from settings import ip
import time
import schemas


# 4.1 发布公告消息
def post_notice(info: schemas.PostNoticeInfo):
    """
        :param info:包含发布人用户编号，发布信息内容，公告标题，重要级别的对象
        :return:成功与否
    """
    result = notice_create.create(
        info.user_id,
        info.content,
        info.title,
        info.notice_level
    )
    if not result:
        return responseCode.resp_4xx(data=None, code=400, message="数据库错误")
    elif result == "无法连接数据库":
        return responseCode.resp_4xx(data=None, code=400, message="无法连接数据库")
    return responseCode.resp_200(data=result)


# 4.2 管理员对订单进行免费处理
def freeofcharge(order_id: int):
    """
        :param order_id:订单编号
        :return:成功与否
    """
    success = order_pay.update(order_id, 2)
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


# 4.2.1 管理员对订单进行结账处理
def payment(order_id: int):
    """
        :param order_id:订单编号
        :return:成功与失败
        """
    success = order_pay.update(order_id, 1)
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


# 4.3 所有用户个人信息列表展示
def show_profiles_list():
    """
        :return: 一个list，包含字典：{用户编号、用户工号、用户姓名、职位、show（默认为false)}
    """
    profiles_list, success = user_showall.show(ip)
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(profiles_list) == 0:
        return responseCode.resp_4xx(code=400, message="用户信息为空")
    profiles_dict_list = []
    for i in profiles_list:
        profiles_dict_list.append({
            "user_id": i[0],
            "user_number": i[1],
            "user_name": i[2],
            "user_position": i[3],
            "user_img": i[4],
            "user_gender": i[5],
            "user_state": i[6],
            "show": False,
        })
    return responseCode.resp_200(data=profiles_dict_list)


def add_meal(file, food_name, food_info, food_price, food_rmd):
    print("输出：", type(food_price), food_name, food_info, food_price, food_rmd)
    dataRecieved, isSuccess = food_create.create(food_name, food_info, food_price, rmd=int(food_rmd))
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="创建菜品失败")

    try:
        # tick 是当前的时间(单位s)
        ticks = str(int(time.time()))
        url = "http://124.70.200.142:8080/img/food/" + dataRecieved + ".jpg"
        # 这里根据food_id更换数据库食品的图片链接 
        path = "/root/tomcat/webapps/img/food/" + dataRecieved + ".jpg"
        with open(path, 'wb') as f:
            f.write(file)

        dataResp["food_img"] = url

        flag = food_update.updateimg(dataRecieved, url)
        if flag == False:
            return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    except:
        return responseCode.resp_4xx(code=400, message="服务器错误", data=None)
    return responseCode.resp_200(data=None)

    return responseCode.resp_200(data={"food_id": result})


def remove_meal(food_id):
    result = food_delete.delete(food_id)
    if result == False:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    return responseCode.resp_200(data=result)


def modify_meal(file, food_id, food_name, food_info, food_price, food_rmd):
    # file,
    # int(food_id),
    # food_name,
    # food_info,
    # float(food_price),
    # int(food_rmd)
    Flags = []

    flag = False
    flag = food_update.updatename(food_id, food_name)
    Flags.append(flag)

    flag = False
    flag = food_update.updateinfo(food_id, food_info)
    Flags.append(flag)

    flag = False
    flag = food_update.updateprice(food_id, float(food_price))
    Flags.append(flag)

    flag = False
    flag = food_update.updatermd(food_id, int(food_rmd))
    Flags.append(flag)

    isSuccess = True
    for item in Flags:
        isSuccess = isSuccess and item

    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    try:
        # tick 是当前的时间(单位s)
        ticks = str(int(time.time()))
        url = "http://124.70.200.142:8080/img/food/" + ticks + ".jpg"
        # 这里根据food_id更换数据库食品的图片链接 
        path = "/root/tomcat/webapps/img/food/" + ticks + ".jpg"
        with open(path, 'wb') as f:
            f.write(file)

        flag = food_update.updateimg(food_id, url)
        if flag == False:
            return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    except:
        return responseCode.resp_4xx(code=400, message="服务器错误", data=None)
    return responseCode.resp_200(data=None)


# 4.5 管理员添加成员
def create_member(user_number: str, user_position: int, user_gender: int, user_name: str):
    """
        :param info:用户工号、职位、性别、姓名
        :return:成功与否
    """
    # 下面需要判断职位来选择相关的默认头像
    if user_position == 1:
        # 1代表管理员
        userImage = "http://124.70.200.142:8080/img/person/admin.jpg"
    elif user_position == 2:
        # 2代表服务员
        userImage = "http://124.70.200.142:8080/img/person/waiter.jpg"
    elif user_position == 3:
        # 3代表厨师
        userImage = "http://124.70.200.142:8080/img/person/cook.jpg"
    else:
        return responseCode.resp_4xx(code=400, message='没有此职位', data=None)

    msgRecived = user_create.create(
        number=user_number,
        position=user_position,
        gender=user_gender,
        name=user_name,
        img=userImage
    )
    if msgRecived == '创建成功':
        return responseCode.resp_200(data=None)
    elif msgRecived == '用户已存在':
        return responseCode.resp_4xx(code=400, message="此工号已经存在")
    else:
        return responseCode.resp_4xx(code=500, message="数据库错误")


# 4.6 管理员删除成员
def remover_member(user_id: int):
    """
        :param user_id: 用户编号
        :return:成功与否
    """
    success = user_delete.delete(user_id)
    if success:
        return responseCode.resp_200(data=None)
    elif success == "admin":
        return responseCode.resp_4xx(code=400, message="不能删除管理员")
    else:
        return responseCode.resp_4xx(code=400, message="数据库出现错误")


# 4.7 管理员修改成员信息
def edit_profiles(info:schemas.ProfilesEdit2):
    """
        :param info:当前用户编号，修改用户编号，修改码（1：修改职位，2：修改密码），修改内容
        :return:成功与否
    """
    # 先获取这个id对应的职位，如果id不是管理员，则只能改自己的，如果是管理员，则可以改其他人的
    user_a, user_b = 0, 0  # 这两个是对应a和b的职位，1为管理员

    data_received, success = user_showone.show(info.user_id_a)
    if not success:
        return responseCode.resp_4xx(code=401, data=None, message="获取id错误")
    user_a = data_received[3]

    data_received, success = user_showone.show(info.user_id_b)
    if not success:
        return responseCode.resp_4xx(code=401, data=None, message="获取id错误")
    user_b = data_received[3]

    data_received, success = (), None  # 初始化这两个变量
    if user_a == 1 and user_b != 1:  # 如果当前为管理员则可以随便改，但是不可以修改其他管理员
        if info.tag == 1:  # 1表示修改职位
            success = user_update.updatepos(info.user_id_b, int(info.content))
        elif info.tag == 2:  # 2表示修改密码
            success = user_update.updatepwd(info.user_id_b, info.content)
    elif user_a == user_b == 1 and info.user_id_a != info.user_id_b:  # 不可以修改其他管理员
        return responseCode.resp_4xx(code=401, data=None, message="不可以修改其他管理员")
    elif info.user_id_a == info.user_id_b:
        if info.tag == 1:  # 1表示修改头像
            success = user_update.updateimg(info.user_id_b, info.content)
        elif info.tag == 2:  # 2表示修改密码
            success = user_update.updatepwd(info.user_id_b, info.content)
    else:
        return responseCode.resp_4xx(code=401, data=None, message="此id没有修改其他用户信息的权限")
    return responseCode.resp_200(data=None)


# 4.4 个人信息详细信息页面在管理员端的展示
def show_details(user_id: int):
    """
        :param user_id:用户编号
        :return:用户编号、用户工号、职位、密码、性别、登陆状态、姓名
    """
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


def modify_table_number(table_number: int):
    dataRecieved, isSuccess = table_showall.show()
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    # 目前的桌子数量
    currentTableNum = len(dataRecieved) + 1

    # 这里要判断目前的桌子上面是否空闲
    # 一旦有任何一张桌子空闲则返回401无权限错误
    for table in dataRecieved:
        if table[1] == 1:
            return responseCode.resp_4xx(code=401, message="有桌位被占用，你没有权限修改桌子数量", data=None)

    # 下面有三种情况，小于等于和大于
    if table_number == currentTableNum:
        # 等于则返回错误
        return responseCode.resp_4xx(code=400, message="桌子数量相等", data=None)
    elif table_number < currentTableNum:
        # 如果修改的桌子数量比之前大，则删除桌子
        diff = abs(table_number - currentTableNum)
        # 因为是一次一次改的，某一次删除可能会出错
        # 要统计没有出错的数量是什么
        isSuccess = True
        delNum = 0
        for i in range(diff - 1):
            flag = table_delete.delete()
            if flag == True:
                delNum += 1
            else:
                isSuccess = False
        # 下面的代码判断添加是否成功决定返回值
        if isSuccess == False:
            msg = "删除桌位请求出现错误，目前已成功删除" + str(i + 1) + "张桌位"
            return responseCode.resp_4xx(code=400, message=msg, data=None)
        else:
            return responseCode.resp_200(data=None)
    else:
        # 如果修改的桌子数量比之前小，则增加桌子
        diff = abs(table_number - currentTableNum + 1)
        flag = table_create.create(diff)
        if flag == False:
            return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
        return responseCode.resp_200(data=None)


def modify_food_image(file, food_id: int):
    dataResp = {
        "food_img": str
    }
    try:
        # tick 是当前的时间(单位s)
        ticks = str(int(time.time()))
        url = "http://124.70.200.142:8080/img/food/" + ticks + ".jpg"
        # 这里根据food_id更换数据库食品的图片链接 
        path = "/root/tomcat/webapps/img/food/" + ticks + ".jpg"
        with open(path, 'wb') as f:
            f.write(file)

        dataResp["food_img"] = url

        flag = food_update.updateimg(food_id, url)
        if flag == False:
            return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    except:
        return responseCode.resp_4xx(code=400, message="服务器错误", data=None)
    return responseCode.resp_200(data=dataResp)


def get_meal_details(food_id: int):
    # food_id、food_name、food_info、food_price、food_recommend、food_img
    dataRecieved, isSuccess = food_showone.show(food_id)
    print(dataRecieved, isSuccess)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    elif dataRecieved == None:
        return responseCode.resp_4xx(code=400, message="未找到此菜品", data=None)
    # dataRecieved内容：
    # food_id [i][0]
    # food_name [i][1]
    # food_info [i][2]
    # food_price [i][3]
    # food_rmd [i][4]
    # food_img [i][5]
    dataResp = {
        "food_id": dataRecieved[0],
        "food_name": dataRecieved[1],
        "food_info": dataRecieved[2],
        "food_price": dataRecieved[3],
        "food_rmd": dataRecieved[4],
        "food_img": dataRecieved[5],
    }
    return responseCode.resp_200(data=dataResp)

def get_orders():
    # 订单编号，桌位号、付款状态（默认为待付款），
    dataRecieved, isSuccess = order_showall.show()

    dataResp = []
    for i in range(len(dataRecieved)):
        dic = {
            "order_id": dataRecieved[i][0],
            "order_table": dataRecieved[i][1],
            "order_state": dataRecieved[i][2],
            "order_total": dataRecieved[i][3],
            "order_create_time": dataRecieved[i][4]
        }
        dataResp.append(dic)

    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    else:
        return responseCode.resp_200(data=dataResp)