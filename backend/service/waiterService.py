from util import responseCode
from dao.food import food_showall
from dao.food import food_showone
from dao.order import order_create
from dao.user import user_showone
from settings import ip
import schemas
from dao.waiter import waiter_showall
from dao.order import order_showall
from dao.order import orderinfo_show
from dao.waiter import waiter_updatefood
from dao.waiter import waiter_updateorder
from dao.table import table_showall


# 2.1 服务员桌位请求显示
def fetch_all_tables():
    table_list, success = table_showall.show()
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")

    table_dict_list = []
    for i in range(len(table_list)):
        table_dict_list.append({
            "table_id": table_list[i][0],
            "table_state": table_list[i][1]
        })
    return responseCode.resp_200(data=table_dict_list)


# 2.2 服务员点餐页面获取
def show_meal_list():
    """
    :return: 由dict型的菜品组成的list
    """
    food_list, success = food_showall.show(ip)  # 调用数据库函数，得到菜品列表
    # 返回值包含
    # food_id == food_list[i][0]
    # food_name == food_list[i][1]
    # food_price == food_list[i][2]
    # food_rmd == food_list[i][3]
    # food_img == food_list[i][4]

    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(food_list) == 0:
        return responseCode.resp_4xx(code=400, message="没有菜品可以显示")
    # 将菜品信息列表转换为字典
    food_dic_list = []  # 此list为返回的list

    # 将返回的东西添加进list
    for i in food_list:
        food_dic_list.append({
            "food_id": i[0],
            "food_name": i[1],
            "food_price": i[2],
            "food_recommend": False if i[3] == 0 else True,
            "food_img": i[4],
            "food_value": float(0),
            "food_num": float(0)
        })
    return responseCode.resp_200(data=food_dic_list)


# 2.3 服务员菜品详细页面
def show_food_info(food_id):
    """
        :param food_id: 菜品id
        :return: 菜品详细信息构成的字典
    """
    info, success = food_showone.show(food_id)  # 调用数据库函数，得到某个菜品的信息list
    # info数据返回内容
    # food_id == info[0]
    # food_name == info[1]
    # food_info == info[2]
    # food_price == info[3]
    # food_rmd == info[4]
    # food_img == info[5]

    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    # 将list转换为dict
    info_dict = {
        "food_id": info[0],
        "food_name": info[1],
        "food_info": info[2],
        "food_price": info[3],
        "food_recommend": info[4],
        "food_img": info[5]
    }
    return responseCode.resp_200(data=info_dict)


# 2.4 服务员点餐下单
def post_order(info: schemas.OrderInfo):
    """
        :param info: 包含订单各种信息的一个类
        :return: 成功与否
    """
    # 提取info中的菜品id及其数量
    food_list = []
    for i in info.meal_info:
        if i.food_num==0:
            continue
        food_list.append([
            i.food_id,
            i.food_num
        ])
    # 调用数据库函数建立订单
    result = order_create.create(
        info.order_table,
        info.order_total,
        info.user_id,
        food_list
    )
    return responseCode.resp_200(data=result)


# 2.5 服务员取菜列表显示
def show_cooked_food():
    """
        :return: 由待上菜订单信息dict组成的list
    """
    food_list, success = waiter_showall.show(ip)  # 调用数据库函数，得到待上菜信息列表
    # food_list中的数据为：
    # food_name == food_list[i][0]
    # food_num == food_list[i][1]
    # order_id == food_list[i][2]
    # order_table == food_list[i][3]
    # food_state == food_list[i][4]

    # 检验取回的list是否有效
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(food_list) == 0:
        return responseCode.resp_4xx(code=400, message="无待上菜的菜品")
    # 将信息由list转换为dict类型
    food_dict_list = []
    food_data, flag = food_showall.show()  # 调用数据库函数，获取全部已有的菜品信息，
    # food_data中的数据为：
    # food_id == food_data[i][0]
    # food_name == food_data[i][1]
    # food_price == food_data[i][2]
    # food_rmd == food_data[i][3]
    # food_img == food_data[i][4]

    # 如果调用菜品信息出错
    if not flag:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    
    # 初始化参数
    food_url = ""
    food_id = 0

    # 将food_list中每一个元素取出来
    for i in food_list:
        # 将菜品名与菜品信息进行比较,获取图片地址
        for item in food_data:
            if item[1] == i[0]:
                food_url = item[4]
                food_id = item[0]
        
        # 建立字典
        food_dict_list.append({
            "food_name": i[0],
            "food_num": i[1],
            "order_id": i[2],
            "order_table": i[3],
            "food_state": i[4],
            "food_img": food_url,
            "food_id":food_id
        })
    return responseCode.resp_200(data=food_dict_list)


# 2.6 服务员更改某一道菜的状态
def modify_meal_state(info:schemas.OrderState):
    """
        :param info: 包含订单号与菜品编号的对象
        :return: 成功与否
    """
    # 调用数据库函数
    success = waiter_updatefood.update(info.order_id, info.food_id)
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    else:
        return responseCode.resp_200(data=None)


# 2.7 服务员结单显示页面
def get_orders():
    """
        :return:一个由订单的详细信息组成的dict构成的list
    """
    order_list, success = order_showall.show()
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    order_dict_list = []
    for order in order_list:
        if order[2] != 0:
            continue
        table_food_list, success = orderinfo_show.show(order[0])
        if not success:
            return responseCode.resp_4xx(code=400, message="访问订单菜品信息错误")
        complete = True
        for food in table_food_list:
            if food[3] != 1:
                complete = False
                break

        order_dict_list.append({
            "order_id": order[0],
            "order_table": order[1],
            "order_state": order[2],
            "order_total": order[3],
            "order_create_time": order[4],
            "order_complete": complete
        })

    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    else:
        return responseCode.resp_200(data=order_dict_list)


# 2.8 服务员对某订单确认结账
def payment(order_id: int):
    """
    :param order_id:订单编号
    :return:成功与否
    """
    success = waiter_updateorder.update(order_id)
    if success == "有菜品未上桌":
        return responseCode.resp_4xx(code=400, message="有菜品未上桌")
    elif not success:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


# 2.9 服务员获取订单详情
def get_order_details(order_id: int):
    """
           :param order_id:订单编号
           :return:服务员姓名、订单编号、创建时间、桌号、总价、
           菜品列表（所有信息：菜品编号、菜品数量、菜品状态、菜品价格、菜品图形、菜品名字）
           最后以list套dict的形式返回
    """
    data_reformat = {
        "user_name": str,
        "order_id": int,
        "order_create_time": str,
        "order_table": int,
        "order_total": float,
        "meal_list": list  # 最后这个是列表套字典
    }  # 将变量dataResp定义为字典，同时指定内容

    lis_resp = []  # 将变量lisResp定义为列表

    # 先获取这个订单的基本信息
    order_list, success = order_showall.show()
    # dataRecieved返回的是全部信息，需要进行筛选
    # order_id, [i][0] 
    # order_table, [i][1] 
    # order_state, [i][2] 
    # order_total, [i][3] 
    # order_create_time, [i][4] 
    # user_id 服务员id, [i][5]
    if not success:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)

    i = 0  # 初始化
    # 线性查找，只有一对一的映射关系，可以找到了中途退出遍历
    for i in range(len(order_list)):
        if order_list[i][0] == order_id:
            break  # 此刻拿到了这个id对应的订单信息

    # 下面把前五个内容放进字典里面
    data_reformat["order_id"] = order_list[i][0]
    user, flag = user_showone.show(order_list[i][5])
    if flag == "not found":
        return responseCode.resp_4xx(code=400, message="未找到用户(id为:" + \
                                                       str(order_list[i][5]) + ")的数据，请检查数据库", data=None)
    elif flag == False:
        return responseCode.resp_4xx(code=400, message="数据库错误", data=None)
    data_reformat["user_name"] = user[2]
    data_reformat["order_create_time"] = order_list[i][4]
    data_reformat["order_table"] = order_list[i][1]
    data_reformat["order_total"] = order_list[i][3]

    # 之后再获取这个订单的对应的菜品列表
    # 好习惯，先清空变量
    order_list, success, i = (), False, 0
    # 调用数据库获取信息
    order_list, success = orderinfo_show.show(order_id)
    # 返回的是元组，需要遍历筛选。因为存在一对多现象，需要全部遍历一次
    # order_id, [i][0]
    # food_id, [i][1]
    # food_num, [i][2]
    # food_state, [i][3]
    for i in range(len(order_list)):
        if order_list[i][0] == order_id:
            dic = {
                "food_id": order_list[i][1],
                "food_num": order_list[i][2],
                "food_state": order_list[i][3],
                "food_price": float,
                "food_img": str,
                "food_name": str
            }  # 初始化
            # 这里根据food_id去查找这一道菜的价格和图片
            data_food, success = food_showone.show(order_list[i][1])
            # 返回的是每一道菜的信息
            # food_id, [i][0]
            # food_name, [i][1]
            # food_info, [i][2]
            # food_price, [i][3]
            # food_rmd, [i][4]
            # food_img, [i][5]
            if not success:
                return responseCode.resp_4xx(code=400, message="数据库错误")
            elif data_food == None:
                return responseCode.resp_4xx(code=400, message="未找到(food_id = "\
                     + str(order_list[i][1]) + ")的数据，请检查数据库")
            
            dic["food_price"] = data_food[3]
            dic["food_img"] = data_food[5]
            dic["food_name"] = data_food[1]
            # 到这里dic的内容就完了，append到列表里面就ok

            lis_resp.append(dic)

    # 不要忘了把处理好的lisResp装回返回字典里面
    data_reformat["meal_list"] = lis_resp
    return responseCode.resp_200(data=data_reformat)
