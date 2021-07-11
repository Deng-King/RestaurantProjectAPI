from util import responseCode
from dao.food import food_showall
from dao.food import food_showone
from dao.order import order_create
from settings import ip
import schemas
from dao.waiter import waiter_check, waiter_showall
from dao.order import order_pay
from dao.order import order_showall
from dao.waiter import waiter_updatefood
import settings


# 2.1 服务员桌位请求显示
def fetch_all_tables():
    dataRecieved, isSuccess = waiter_check.show()
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")

    dataResp = []
    for i in range(len(dataRecieved)):
        dic = {
            "table_number": dataRecieved[i][1],
            "state": dataRecieved[i][2]
        }
        dataResp.append(dic)
    return responseCode.resp_200(data=dataResp)


# 2.2 服务员点餐页面获取
def show_meal_list():
    food_list = food_showall.show(ip)
    if len(food_list) == 0:
        return responseCode.resp_4xx(code=400, message="没有菜品可以显示")
    food_dic_list = []
    for i in food_list:
        food_dic_list.append({
            "food_id": i[0],
            "food_name": i[1],
            "food_price": i[2],
            "food_recommend": i[3],
            "food_img": i[4]
        })
    return responseCode.resp_200(data=food_dic_list)


# 2.3 服务员菜品详细页面
def show_meal_info(food_id):
    i = food_showone.show(ip, food_id)
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
        ip,
        info.order_table,
        info.order_total,
        info.user_id,
        food_list
    )
    return responseCode.resp_200(data=result)


# 2.5 服务员取菜列表显示
def show_cooked_food():
    food_list = waiter_showall.show(ip)
    print(food_list)
    if len(food_list) == 0:
        return responseCode.resp_4xx(code=400, message="无待上菜的菜品")
    food_dict_list = []
    for i in food_list:
        food_dict_list.append({
            "food_name": i[0],
            "food_num": i[1],
            "order_id": i[2],
            "order_table": i[3],
            "food_state": i[4]
        })
    return responseCode.resp_200(data=food_dict_list)


# 2.8 服务员对某订单确认结账
def payment(Orderid: int):
    isSuccess = order_pay.update(Orderid, 1)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)


def modify_meal_state(order_id:int, food_id:int):
    isSuccess = waiter_updatefood.update(order_id, food_id)
    if isSuccess == False:
        return responseCode.resp_4xx(400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)

def get_orders():
    # 订单编号，桌位号、付款状态（默认为待付款），
    dataRecieved,isSuccess = order_showall.show()

    dataResp = []
    for i in range(len(dataRecieved)):
        dic = {
            "order_id":dataRecieved[i][0],
            "order_table":dataRecieved[i][1],
            "order_state":dataRecieved[i][2],
            "order_total":dataRecieved[i][3],
            "order_create_time":dataRecieved[i][4]
        }
        dataResp.append(dic)
    
    if isSuccess == False:
        return responseCode.resp_4xx(400, message = "数据库错误")
    else:
        return responseCode.resp_200(data = dataResp)
