from util import responseCode
from dao.cook import cook_update, cook_showall
import schemas
from settings import ip


def modify_meal_state(mod: schemas.ModifyOrder):
    result = cook_update.update(ip, mod.food_id, mod.order_id)
    return responseCode.resp_200(data=result)


def show_meal_list():
    meal_list = cook_showall.show(ip)
    if len(meal_list) == 0:
        return responseCode.resp_4xx(code=400, message="菜品列表为空")
    meal_dict_list = []
    for i in meal_list:
        meal_dict_list.append({
            "food_name": i[0],
            "food_num": i[1],
            "order_id": i[2],
            "order_table": i[3],
            "food_state": i[4],
            
        })
    return responseCode.resp_200(data=meal_dict_list)
