from fastapi import APIRouter
from service import waiterService
import schemas

waiterRouter = APIRouter()


# 2.1 服务员桌位请求显示
@waiterRouter.get("/waiter/table/fetch", tags=["waiter"])
async def fetch_all_tables():
    response = waiterService.fetch_all_tables()
    return response


# 2.2 服务员点餐页面获取
@waiterRouter.get("/waiter/meals/list", tags=["waiter"])
async def show_meal_list():
    """
    :return: 由dict型的菜品组成的list
    """
    return waiterService.show_meal_list()


# 2.3 服务员菜品详细页面
@waiterRouter.get("/waiter/meals/list/details/", tags=["waiter"])
async def show_meal_info(food_id: int):
    """
    :param food_id: 菜品id
    :return: 菜品详细信息构成的字典
    """
    return waiterService.show_food_info(food_id)


# 2.4 服务员点餐下单
@waiterRouter.post("/waiter/order/post", tags=["waiter"])
async def post_order(info: schemas.OrderInfo):
    """
    :param info: 包含订单各种信息的一个类
    :return: 成功与否
    """
    return waiterService.post_order(info)


# 2.5 服务员取菜列表显示
@waiterRouter.get("/waiter/meals/states/fetch", tags=["waiter"])
async def show_cooked_food():
    """
    :return: 由待上菜订单信息dict组成的list
    """
    return waiterService.show_cooked_food()


# 2.6 服务员更改某一道菜的状态
@waiterRouter.post("/waiter/meals/states/modify", tags=["waiter"])
async def modify_meal_state(info: schemas.OrderState):
    """
    :param info: 包含订单号与菜品编号的对象
    :return: 成功与否
    """
    response = waiterService.modify_meal_state(info)
    return response


# 2.7 服务员结单显示页面
@waiterRouter.get("/waiter/orders/list/fetch", tags=["waiter"])
async def get_orders_list():
    """
    :return:一个由订单的详细信息组成的dict构成的list
    """
    response = waiterService.get_orders()
    return response


# 2.8 服务员对某订单确认结账
@waiterRouter.get("/waiter/order/states/payment", tags=["waiter"])
async def order_payment(order_id: int):
    response = waiterService.payment(order_id)
    return response


# 2.9 服务员获取订单详情
@waiterRouter.get("/waiter/order/details", tags=["waiter"])
async def get_order_details(order_id: int):
    response = waiterService.get_order_details(order_id)
    return response
