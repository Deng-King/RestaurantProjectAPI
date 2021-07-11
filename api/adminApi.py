from fastapi import APIRouter
from service import adminService
import schemas

adminRouter = APIRouter()


# 4.1 发布公告消息
@adminRouter.post("/announcement/post", tags=["admin"])
async def post_notice(notice_info: schemas.PostNoticeInfo):
    return adminService.post_notice(notice_info)

#4.4 个人信息详细信息页面在管理员端的展示
@adminRouter.get("/admin/profiles/details", tags=["admin"])
async def show_profiles_details(info: schemas.Profiles):
    response = adminService.show_details(info.user_id)
    return response

# 4.5 管理员添加成员
@adminRouter.post("/admin/profiles/add", tags=["admin"])
async def add_member(info: schemas.AdminAddMember):
    # 用户工号、职位、性别、姓名
    # user_number: str
    # user_position: int
    # user_gender: int
    # user_name: str
    response = adminService.create_member(info.user_number,
                                        info.user_position,
                                        info.user_gender,
                                        info.user_name)
    return response


# 4.6 管理员删除成员
@adminRouter.get("/admin/profiles/remove",tags=["admin"])
async def remove_member(info:schemas.Profiles):
    response = adminService.remover_member(info.user_id)
    return response

# 4.7 管理员修改成员信息
@adminRouter.post("/admin/profiles/modify",tags=["admin"])
async def edit_profiles(info: schemas.ProfilesEdit):
    # 当前用户编号，修改用户编号，修改码（1：修改职位，2：修改密码）
    # user_id_a, user_id_b, tag, content
    response = adminService.edit_profiles(info.user_id_a,
                                            info.user_id_b,
                                            info.tag,
                                            info.content)
    return response



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
