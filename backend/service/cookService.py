from util import responseCode
from dao.cook import cook_update, cook_showall
from dao.food import food_showone,food_showall
from dao.order import orderinfo_show
from dao.order import order_showall
import schemas
from settings import ip


def modify_meal_state(mod: schemas.ModifyOrder):
    result = cook_update.update(mod.food_id, mod.order_id)
    return responseCode.resp_200(data=result)


def show_meal_list():
    meal_list,isSuccess = cook_showall.show(ip)
    if isSuccess == False:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(meal_list) == 0:
        return responseCode.resp_4xx(code=400, message="菜品列表为空")
    meal_dict_list = []
    for i in meal_list:
        data,flag = food_showall.show()
        # print(data,flag)
        if flag == False:
            return responseCode.resp_4xx(code=400, message="数据库错误")
        foodURL = ""
        foodid = 0
        for item in data:
            if item[1] == i[0]:
                foodURL = item[4]
                foodid = item[0]

        data, flag = (),False
        orderCreateTime = ""
        data, flag = order_showall.show()
        if flag == False:
            return responseCode.resp_4xx(code=400, message="数据库错误")
        for item in data:
            if item[0] == i[2]:
                orderCreateTime = item[4]
        if i[4] != 0:
            continue
        meal_dict_list.append({
            "food_name": i[0],
            "food_num": i[1],
            "order_id": i[2],
            "order_table": i[3],
            "food_state": i[4],
            "food_img": foodURL,
            "order_create_time": orderCreateTime,
            "food_id":foodid,
        })
    return responseCode.resp_200(data=meal_dict_list)
