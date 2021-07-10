from util import responseCode
from dao.notice import notice_create
from dao.food import food_create, food_delete,food_update
import settings
import schemas


def post_notice(info: schemas.PostNoticeInfo):
    result = notice_create.create(
        settings.ip,
        info.user_id,
        info.content,
        info.title,
        info.notice_level
    )
    return responseCode.resp_200(data=result)


def add_meal(meal: schemas.FoodInfo):
    result = food_create.create(
        settings.ip,
        meal.food_name,
        meal.food_info,
        meal.food_price,
        meal.food_recommend,
        meal.food_img
    )
    return responseCode.resp_200(data=result)


def remove_meal(meal_id):
    result = food_delete.delete(settings.ip, meal_id)
    return responseCode.resp_200(data=result)


def modify_meal(meal:schemas.FoodInfo):
    return 1