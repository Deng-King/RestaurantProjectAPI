from fastapi import APIRouter
from service import adminService
import schemas

adminRouter = APIRouter()


# 4.1 发布公告消息
@adminRouter.post("api/announcement/post", tags=["admin"])
async def post_notice(notice_info: schemas.PostNoticeInfo):
    return adminService.post_notice(notice_info)


# 4.8 管理员添加新品
@adminRouter.post("api/admin/meals/add", tags=["admin"])
async def add_meal(meal: schemas.FoodInfo):
    return adminService.add_meal(meal)


# 4.9 管理员删除菜品信息
@adminRouter.post("api/admin/meals/remove", tags=["admin"])
async def remove_meal(meal_id:int):
    return adminService.remove_meal(meal_id)


# 4.10 管理员修改菜品
@adminRouter.post("api/admin/meals/modify",tags=["admin"])
async def modify_meal(mod:schemas.ModifyChoice):
    return adminService.modify_meal(mod)