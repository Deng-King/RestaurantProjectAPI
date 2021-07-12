from fastapi import APIRouter
from service import cookService
import schemas

cookRouter=APIRouter()


# 3.1 后厨更改菜品状态
@cookRouter.post("/cook/meals/states/modify",tags=["cook"])
async def modify_meal_state(mod:schemas.ModifyOrder):
    return cookService.modify_meal_state(mod)


# 3.2 后厨菜品列表显示
@cookRouter.get("/cook/meals/states/fetch",tags=["cook"])
async def show_meal_list():
    return cookService.show_meal_list()