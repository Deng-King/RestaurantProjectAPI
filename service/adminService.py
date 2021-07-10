from util import responseCode
from dao.notice import notice_create
from dao.food import food_create, food_delete, food_update
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

