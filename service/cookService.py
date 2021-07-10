from util import responseCode
from dao.cook import cook_update
import schemas
from settings import ip


def modify_meal_state(mod:schemas.ModifyOrder):
    result=cook_update.update(ip,mod.food_id,mod.order_id)
    return responseCode.resp_200(data=result)