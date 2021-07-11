from util import responseCode
from dao.food import food_showall
from dao.food import food_showone
from dao.order import order_create
from settings import ip
import schemas
from dao.waiter import waiter_check
from dao.order import order_pay
import settings


# 2.2 服务员点餐页面获取
def show_meal_list():
    food_list = food_showall.show(ip)
    if len(food_list) == 0:
        return responseCode.resp_4xx(400, message="没有菜品可以显示")
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

def fetch_all_tables():
    dataRecieved, isSuccess = waiter_check.show()
    if isSuccess == False:
        return responseCode.resp_4xx(400, message="数据库错误")

    dataResp = []
    for i in range(len(dataRecieved)):
        dic = {
            "table_number":dataRecieved[i][1],
            "state":dataRecieved[i][2]
        }
        dataResp.append(dic)
    return responseCode.resp_200(data=dataResp)

def payment(Orderid:int):
    isSuccess = order_pay(Orderid,1)
    if isSuccess == False:
        return responseCode.resp_4xx(400, message="数据库错误")
    else:
        return responseCode.resp_200(data=None)