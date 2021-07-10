from util import responseCode
from dao.food import food_showall
from dao.food import food_showone
import settings


# 2.2 服务员点餐页面获取
def show_meal_list():
    food_list = food_showall.show(settings.ip)
    if food_list is None:
        return  responseCode.resp_4xx(400,message="没有菜品可以显示")
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
    i = food_showone.show(settings.ip, food_id)
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
