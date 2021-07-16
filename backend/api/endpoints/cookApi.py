from fastapi import APIRouter
from service import cookService
from ConnectionManager import manager
import schemas

router = APIRouter()


# 3.1 后厨更改菜品状态
@router.post("/cook/meals/states/modify", tags=["cook"])
async def modify_meal_state(mod: schemas.ModifyOrder):
    """
    :param mod: 包含修改菜品状态的订单号，菜品编号的一个类
    :return: 成功与否
    """
    success,response=cookService.modify_meal_state(mod)
    if success:
        # 利用websocket进行广播
        await manager.broadcast_meal_states()
    return response


# 3.2 后厨菜品列表显示
@router.get("/cook/meals/states/fetch", tags=["cook"])
async def show_meal_list():
    """
    :return: 包含多个菜品信息的dict组成的list
    """
    return cookService.show_meal_list()
