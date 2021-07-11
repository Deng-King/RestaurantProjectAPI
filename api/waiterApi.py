from fastapi import APIRouter
from service import waiterService
import schemas

waiterRouter = APIRouter()


# 2.2 服务员点餐页面获取
@waiterRouter.get("/waiter/meals/list", tags=["waiter"])
async def show_meal_list():
    return waiterService.show_meal_list()


# 2.3 服务员菜品详细页面
@waiterRouter.get("/waiter/meals/list/details/{food_id}", tags=["waiter"])
async def show_meal_info(food_id: int):
    return waiterService.show_meal_info(food_id)


# 2.4 服务员点餐下单
@waiterRouter.post("/waiter/order/post", tags=["waiter"])
async def post_order(info: schemas.OrderInfo):
    return waiterService.post_order(info)
