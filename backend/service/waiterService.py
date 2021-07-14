from util import responseCode
from dao.food import food_showall
from dao.food import food_showone
from dao.order import order_create
from dao.user import user_showone
from settings import ip
import schemas
from dao.waiter import waiter_check, waiter_showall
from dao.order import order_pay
from dao.order import order_showall
from dao.order import orderinfo_show
from dao.waiter import waiter_updatefood
from dao.waiter import waiter_updateorder
from dao.table import table_showall
import settings


# 2.1 服务员桌位请求显示
def fetch_all_tables():
    dataRecieved, isSuccess = table_showall.show()
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")

    dataResp = []
    for i in range(len(dataRecieved)):
        dic = {
            "table_id": dataRecieved[i][0],
            "table_state": dataRecieved[i][1]
        }
        dataResp.append(dic)
    return responseCode.resp_200(data=dataResp)


# 2.2 服务员点餐页面获取
def show_meal_list():
    food_list,isSuccess = food_showall.show(ip)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(food_list) == 0:
        return responseCode.resp_4xx(code=400, message="没有菜品可以显示")
    food_dic_list = []
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
def show_meal_info(food_id):
    i,isSuccess = food_showone.show(food_id)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    print(i)
    food_info_dict = {
        "food_id": i[0],
        "food_name": i[1],
        "food_info": i[2],
        "food_price": i[3],
        "food_recommend": i[4],
        "food_img": i[5]
    }
    return responseCode.resp_200(data=food_info_dict)


# 2.4 服务员点餐下单
def post_order(info: schemas.OrderInfo):
    food_list = []
    for i in info.meal_info:
        food_list.append([
            i.food_id,
            i.food_num
        ])
    result = order_create.create(
        info.order_table,
        info.order_total,
        info.user_id,
        food_list
    )
    return responseCode.resp_200(data=result)


# 2.5 服务员取菜列表显示
def show_cooked_food():
    food_list, isSuccess = waiter_showall.show(ip)
    print(food_list)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(food_list) == 0:
        return responseCode.resp_4xx(code=400, message="无待上菜的菜品")
    food_dict_list = []
    for i in food_list:
        foodData, flag = food_showall.show()
        if flag == False:
            return responseCode.resp_4xx(code=400, message="数据库错误")
        foodURL = ""
        for item in foodData:
            if item[1] == i[0]:
                foodURL = item[4]

        food_dict_list.append({
            "food_name": i[0],
            "food_num": i[1],
            "order_id": i[2],
            "order_table": i[3],
            "food_state": i[4],
            "food_img":foodURL
        })
    return responseCode.resp_200(data=food_dict_list)


# 2.8 服务员对某订单确认结账
def payment(Orderid: int):
    isSuccess = waiter_updateorder.update(Orderid)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


def modify_meal_state(order_id:int, food_id:int):
    isSuccess = waiter_updatefood.update(order_id, food_id)
    if isSuccess == False:
        return responseCode.resp_4xx(code = 400, message="数据库错误", data = None)
    else:
        return responseCode.resp_200(data=None)

def get_orders():
    # 订单编号，桌位号、付款状态（默认为待付款），
    dataRecieved,isSuccess = order_showall.show()

    dataResp = []
    for i in range(len(dataRecieved)):
        if dataRecieved[i][2] != 0:
            continue
        dic = {
            "order_id":dataRecieved[i][0],
            "order_table":dataRecieved[i][1],
            "order_state":dataRecieved[i][2],
            "order_total":dataRecieved[i][3],
            "order_create_time":dataRecieved[i][4]
        }
        dataResp.append(dic)
    
    if isSuccess == False:
        return responseCode.resp_4xx(code = 400, message = "数据库错误", data = None)
    else:
        return responseCode.resp_200(data = dataResp)


def get_order_details(Orderid:int):
    # 订单编号、服务员姓名、创建时间、桌号、总价、
    # 菜品列表（所有信息：菜品编号、菜品数量、菜品状态、
    # 菜品价格、菜品图形，菜品名称）
    
    dataResp = {
        "user_name":str,
        "order_id":int,
        "order_create_time":str,
        "order_table":int,
        "order_total":float,
        "meal_list":list # 最后这个是列表套字典
    }   # 将变量dataResp定义为字典，同时指定内容
    
    lisResp = []    # 将变量lisResp定义为列表


    # 先获取这个订单的基本信息
    dataRecieved,isSuccess = order_showall.show()
    # dataRecieved返回的是全部信息，需要进行筛选
    # order_id, [i][0] 
    # order_table, [i][1] 
    # order_state, [i][2] 
    # order_total, [i][3] 
    # order_create_time, [i][4] 
    # user_id 服务员id, [i][5]
    if isSuccess == False:
        return responseCode.resp_4xx(code = 400, message = "数据库错误", data = None)

    i = 0   # 初始化
    # 线性查找，只有一对一的映射关系，可以找到了中途退出遍历
    for i in range(len(dataRecieved)):
        if dataRecieved[i][0] == Orderid:
            break   # 此刻拿到了这个id对应的订单信息
    
    # 下面把前五个内容放进字典里面
    dataResp["order_id"] = dataRecieved[i][0]
    user, flag = user_showone.show(dataRecieved[i][5])
    if flag == "not found":
        return responseCode.resp_4xx(code = 400, message = "未找到用户(id为:"+\
            str(dataRecieved[i][5])+")的数据，请检查数据库", data = None)
    elif flag == False:
        return responseCode.resp_4xx(code = 400, message = "数据库错误", data = None)
    dataResp["user_name"] = user[2]
    dataResp["order_create_time"] = dataRecieved[i][4]
    dataResp["order_table"] = dataRecieved[i][1]
    dataResp["order_total"] = dataRecieved[i][3]

    # 之后再获取这个订单的对应的菜品列表
    # 好习惯，先清空变量
    dataRecieved,isSuccess,i = (),False,0
    # 调用数据库获取信息
    dataRecieved,isSuccess = orderinfo_show.show()
    # 返回的是元组，需要遍历筛选。因为存在一对多现象，需要全部遍历一次
    # order_id, [i][0]
    # food_id, [i][1]
    # food_num, [i][2]
    # food_state, [i][3]
    for i in range(len(dataRecieved)):
        if dataRecieved[i][0] == Orderid:
            dic = {
                "food_id":int,
                "food_num":int,
                "food_state":int,
                "food_price":float,
                "food_img":str,
                "food_name":str
            }    # 初始化
            dic["food_id"] = dataRecieved[i][1]
            dic["food_num"] = dataRecieved[i][2]
            dic["food_state"] = dataRecieved[i][3]
            
            # 这里根据food_id去查找这一道菜的价格和图片
            dataReciFood,flag = food_showone.show(dataRecieved[i][1])
            # 返回的是每一道菜的信息
            # food_id, [i][0]
            # food_name, [i][1]
            # food_info, [i][2]
            # food_price, [i][3]
            # food_rmd, [i][4]
            # food_img, [i][5]
            if flag == False:
                return responseCode.resp_4xx(400, message = "数据库错误")
            dic["food_price"] = dataReciFood[3]
            dic["food_img"] = dataReciFood[5]
            dic["food_name"] = dataReciFood[1]
            # 到这里dic的内容就完了，append到列表里面就ok

            lisResp.append(dic)
    
    # 不要忘了把处理好的lisResp装回返回字典里面
    dataResp["meal_list"] = lisResp
    return responseCode.resp_200(data = dataResp)

