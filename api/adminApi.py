from fastapi import APIRouter
from service import adminService
import schemas

adminRouter = APIRouter()


# 4.1 发布公告消息
@adminRouter.post("/announcement/post", tags=["admin"])
async def post_notice(notice_info: schemas.PostNoticeInfo):
    return adminService.post_notice(notice_info)


#4.3 所有用户个人信息列表展示
@adminRouter.get("/admin/profiles",tags=["admin"])
async def show_profiles_list():
    return adminService.show_profiles_list()


# 4.8 管理员添加新品
@adminRouter.post("/admin/meals/add", tags=["admin"])
async def add_meal(meal: schemas.FoodInfo):
    return adminService.add_meal(meal)


# 4.9 管理员删除菜品信息
@adminRouter.post("/admin/meals/remove", tags=["admin"])
async def remove_meal(meal_id:int):
    return adminService.remove_meal(meal_id)


# 4.10 管理员修改菜品
@adminRouter.post("/admin/meals/modify",tags=["admin"])
async def modify_meal(mod:schemas.ModifyMeal):
    return adminService.modify_meal(mod)