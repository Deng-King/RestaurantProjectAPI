from fastapi import APIRouter
from service import cookService
import schemas

cookRouter=APIRouter()

@cookRouter.post("/cook/meals/states/modify",tags=["cook"])
async def modify_meal_state(mod:schemas.ModifyOrder):
    return cookService.modify_meal_state(mod)