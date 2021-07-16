from util import responseCode
from dao.cook import cook_update, cook_showall
from dao.food import food_showone, food_showall
from dao.order import orderinfo_show
from dao.order import order_showall
import schemas
from settings import ip


# 3.1 后厨更改菜品状态
def modify_meal_state(mod: schemas.ModifyOrder):
    """
        :param mod: 包含修改菜品状态的订单号，菜品编号的一个类
        :return: 成功与否
    """
    # 直接调用数据库函数修改菜品状态
    result = cook_update.update(mod.food_id, mod.order_id)
    return responseCode.resp_200(data=result)


# 3.2 后厨菜品列表显示
def show_meal_list():
    """
        :return: 包含多个菜品信息的dict组成的list
    """
    # 调用数据库函数，获取一个包含菜品信息的list
    meal_list, isSuccess = cook_showall.show(ip)
    # meal_list返回值
    # food_name == meal_list[i][0]
    # food_num == meal_list[i][1]
    # order_id == meal_list[i][2]
    # order_table == meal_list[i][3]
    # food_state == meal_list[i][4]

    if not isSuccess:
        return responseCode.resp_4xx(code=400, message="数据库错误")
    if len(meal_list) == 0:
        # 如果菜品列表没有元素
        return responseCode.resp_4xx(code=400, message="菜品列表为空")
    # 将list中的元素从list转为dict
    meal_dict_list = []
    for i in meal_list:
        # 获取菜品的图片地址
        data, flag = food_showall.show()
        if not flag:
            return responseCode.resp_4xx(code=400, message="数据库错误")
        foodURL = ""
        food_id = 0
        for item in data:
            if item[1] == i[0]:
                foodURL = item[4]
                food_id = item[0]
        # 获取订单的建立时间
        orderCreateTime = ""
        data, flag = order_showall.show()
        # data的返回值有：
        # order_id == data[i][0]
        # order_table == data[i][1]
        # order_state == data[i][2]
        # order_total == data[i][3]
        # order_create_time == data[i][4]
        # user_id(服务员id) == data[i][5]
        # order_end_time == data[i][6]

        if not flag:
            return responseCode.resp_4xx(code=400, message="数据库错误")

        # 遍历data中每一个元素
        for item in data:
            if item[0] == i[2]:
                # 如果order_id 的值相对应
                orderCreateTime = item[4]

        # 如果meal的状态不为0则不需要在厨师端展示
        if i[4] != 0:
            continue
        # 建立dict
        meal_dict_list.append({
            "food_name": i[0],
            "food_num": i[1],
            "order_id": i[2],
            "order_table": i[3],
            "food_state": i[4],
            "food_img": foodURL,
            "order_create_time": orderCreateTime,
            "food_id": food_id,
        })
    return responseCode.resp_200(data=meal_dict_list)
