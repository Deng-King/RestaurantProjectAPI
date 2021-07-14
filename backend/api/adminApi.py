from fastapi import APIRouter
from fastapi import File
from fastapi import Form
from service import adminService
import schemas
from ConnectionManager import manager

adminRouter = APIRouter()


# 4.1 发布公告消息
@adminRouter.post("/announcement/post", tags=["admin"])
async def post_notice(notice_info: schemas.PostNoticeInfo):
    """
        功能:前端发送公告信息，后端将消息存入数据库，并且给相关的接口更新状态，说明现在有新的公告发布。\n
        参数:发布人用户编号，发布信息内容，公告标题，重要级别\n
        返回:成功与否\n
    """
    response = adminService.post_notice(notice_info)
    await manager.broadcast(notice_info.title)
    return response


# 4.2 管理员对订单进行免费处理
@adminRouter.get("/admin/order/states/freeofcharge", tags=["admin"])
async def order_freeofcharge(order_id: int):
    """
        功能:对订单免单\n
        参数:订单编号\n
        返回:成功与失败\n
    """
    response = adminService.freeofcharge(order_id)
    return response


# 4.2.1 管理员对订单进行结账处理
@adminRouter.get("/admin/order/states/payment", tags=["admin"])
async def order_payment(order_id: int):
    """
        功能:对订单结账\n
        参数:订单编号\n
        返回:成功与失败\n
    """
    response = adminService.payment(order_id)
    return response


# 4.3 所有用户个人信息列表展示
@adminRouter.get("/admin/profiles", tags=["admin"])
async def show_profiles_list():
    """
        返回:一个list，包含字典：{用户编号、
        用户工号、用户姓名、职位、show（默认为false)}\n
    """
    return adminService.show_profiles_list()


# 4.4 个人信息详细信息页面在管理员端的展示
@adminRouter.get("/admin/profiles/details", tags=["admin"])
async def show_profiles_details(user_id: int):
    """
        参数:用户编号\n
        返回:\用户编号、用户工号、
        职位、密码、性别、登陆状态、姓名\n
    """
    response = adminService.show_details(user_id)
    return response


# 4.5 管理员添加成员
@adminRouter.post("/admin/profiles/add", tags=["admin"])
async def add_member(info: schemas.AdminAddMember):
    """
        参数:用户工号、职位、性别、姓名\n
        返回:成功与否\n
    """
    response = adminService.create_member(info.user_number,
                                          info.user_position,
                                          info.user_gender,
                                          info.user_name)
    return response


# 4.6 管理员删除成员
@adminRouter.get("/admin/profiles/remove", tags=["admin"])
async def remove_member(user_id: int):
    """
    参数:用户编号\n
    返回:成功与否\n
    """
    response = adminService.remover_member(user_id)
    return response


# 4.7 管理员修改成员信息
@adminRouter.post("/admin/profiles/modify",tags=["admin"])
async def edit_profiles(info: schemas.ProfilesEdit2):
    """
        参数:当前用户编号，修改用户编号，
        修改码（1：修改职位，2：修改密码），修改内容\n
        返回:成功与否\n
    """
    response = adminService.edit_profiles(info.user_id_a,
                                          info.user_id_b,
                                          info.tag,
                                          info.content)
    return response


# 4.8 管理员添加新品
@adminRouter.post("/admin/meals/add", tags=["admin"])
async def add_meal(
    file:       bytes   = File(...),
    food_name:  str     = Form(...),
    food_info:  str     = Form(...),
    food_price: str   = Form(...),
    food_rmd:   int     = Form(...)
    ):
    """
        参数:菜品编号，菜品名称，
        菜品介绍，图像路径，菜品价格，是否推荐\n
        返回:成功与否\n
    """
    return adminService.add_meal(file, food_name, food_info, float(food_price), food_rmd)


# 4.9 管理员删除菜品信息
@adminRouter.get("/admin/meals/remove", tags=["admin"])
async def remove_meal(food_id: int):
    """
        参数:菜品编号\n
        返回:成功与否\n
    """
    return adminService.remove_meal(food_id)


# 4.10 管理员修改菜品
@adminRouter.post("/admin/meals/modify", tags=["admin"])
async def modify_meal(mod: schemas.ModifyMeal):
    """
        参数:菜品编号，菜品名称，菜品介绍，菜品价格，是否推荐\n
        返回:成功与否\n
    """
    return adminService.modify_meal(mod)


# 4.11 管理员对桌子数量的修改
@adminRouter.get("/admin/table/modify", tags=["admin"])
async def modify_table_number(table_number: int):
    """
        参数:桌子数量\n
        返回:成功与否\n
    """
    response = adminService.modify_table_number(table_number)
    return response

# # 4.12 管理员上传照片
# @adminRouter.post("/admin/image/photo", tags=["admin"])
# async def create_files(file: bytes = File(...), food_id: int = Form(...)):
#     response = adminService.modify_food_image(file, food_id)
#     return response

# 4.13 管理员返回菜品的信息
@adminRouter.get("/admin/meal/details/fetch", tags=["admin"])
async def get_meal_details(food_id: int):
    """
        参数:菜品的id\n
        返回:food_id、food_name、food_info、food_price、food_recommend、food_img\n
    """
    response = adminService.get_meal_details(food_id)
    return response
