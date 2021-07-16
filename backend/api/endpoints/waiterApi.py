from fastapi import APIRouter
from service import waiterService
from ConnectionManager import manager
import schemas

router = APIRouter()


# 2.1 服务员桌位请求显示
@router.get("/waiter/table/list", tags=["waiter"])
async def fetch_all_tables():
    response = waiterService.fetch_all_tables()
    return response


# 2.2 服务员点餐页面获取
@router.get("/waiter/meals/list", tags=["waiter"])
async def show_meal_list():
    """
    :return: 由dict型的菜品组成的list
    """
    return waiterService.show_meal_list()


# 2.3 服务员菜品详细页面
@router.get("/waiter/meals/list/details/", tags=["waiter"])
async def show_meal_info(food_id: int):
    """
    :param food_id: 菜品id
    :return: 菜品详细信息构成的字典
    """
    return waiterService.show_food_info(food_id)


# 2.4 服务员点餐下单
@router.post("/waiter/order/post", tags=["waiter"])
async def post_order(info: schemas.OrderInfo):
    """
    :param info: 包含订单各种信息的一个类
    :return: 成功与否
    """
    success, response = waiterService.post_order(info)
    print(success)
    if success:
        # 利用websocket进行广播
        print("broadcast")
        await manager.broadcast_post_order()
    return response


# 2.5 服务员取菜列表显示
@router.get("/waiter/meals/states/list", tags=["waiter"])
async def show_cooked_food():
    """
    :return: 由待上菜订单信息dict组成的list
    """
    return waiterService.show_cooked_food()


# 2.6 服务员更改某一道菜的状态
@router.post("/waiter/meals/states/modify", tags=["waiter"])
async def modify_meal_state(info: schemas.OrderState):
    """
    :param info: 包含订单号与菜品编号的对象
    :return: 成功与否
    """
    response = waiterService.modify_meal_state(info)
    return response


# 2.7 服务员结单显示页面
@router.get("/waiter/orders/list", tags=["waiter"])
async def get_orders_list():
    """
    :return:一个由订单的详细信息组成的dict构成的list
    """
    response = waiterService.get_orders()
    return response


# 2.8 服务员对某订单确认结账
@router.get("/waiter/order/states/payment", tags=["waiter"])
async def order_payment(order_id: int):
    """
    :param order_id:订单编号
    :return:成功与否
    """
    success, response = waiterService.payment(order_id)
    if success:
        # 利用websocket进行广播
        await manager.broadcast_order_states()
    return response


# 2.9 服务员获取订单详情
@router.get("/waiter/order/details", tags=["waiter"])
async def get_order_details(order_id: int):
    """
       :param order_id:订单编号
       :return:服务员姓名、订单编号、创建时间、桌号、总价、
       菜品列表（所有信息：菜品编号、菜品数量、菜品状态、菜品价格、菜品图形、菜品名字）
       最后以list套dict的形式返回
    """
    response = waiterService.get_order_details(order_id)
    return response
