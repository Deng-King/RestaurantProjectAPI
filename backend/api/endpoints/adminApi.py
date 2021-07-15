from fastapi import APIRouter
from fastapi import File
from fastapi import Form
from service import adminService
import schemas
from ConnectionManager import manager

router = APIRouter()


# 4.1 发布公告消息
@router.post("/announcement/post", tags=["admin"])
async def post_notice(info: schemas.PostNoticeInfo):
    """
        :param info:包含发布人用户编号，发布信息内容，公告标题，重要级别的对象
        :return:成功与否
    """
    response = adminService.post_notice(info)
    # 利用websocket进行广播
    await manager.broadcast(info.user_id, info.title)
    return response


# 4.2 管理员对订单进行免费处理
@router.get("/admin/order/states/freeofcharge", tags=["admin"])
async def order_freeofcharge(order_id: int):
    """
    :param order_id:订单编号
    :return:成功与否
    """
    response = adminService.freeofcharge(order_id)
    return response


# 4.2.1 管理员对订单进行结账处理
@router.get("/admin/order/states/payment", tags=["admin"])
async def order_payment(order_id: int):
    """
    :param order_id:订单编号
    :return:成功与失败
    """
    response = adminService.payment(order_id)
    return response


# 4.3 所有用户个人信息列表展示
@router.get("/admin/profiles", tags=["admin"])
async def show_profiles_list():
    """
    :return: 一个list，包含字典：{用户编号、用户工号、用户姓名、职位、show（默认为false)}
    """
    return adminService.show_profiles_list()


# 4.4 个人信息详细信息页面在管理员端的展示
@router.get("/admin/profiles/details", tags=["admin"])
async def show_profiles_details(user_id: int):
    """
    :param user_id:用户编号
    :return:用户编号、用户工号、职位、密码、性别、登陆状态、姓名
    """
    response = adminService.show_details(user_id)
    return response


# 4.5 管理员添加成员
@router.post("/admin/profiles/add", tags=["admin"])
async def add_member(info: schemas.AdminAddMember):
    """
    :param info:用户工号、职位、性别、姓名
    :return:成功与否
    """
    response = adminService.create_member(info.user_number,
                                          info.user_position,
                                          info.user_gender,
                                          info.user_name)
    return response


# 4.6 管理员删除成员
@router.get("/admin/profiles/remove", tags=["admin"])
async def remove_member(user_id: int):
    """
    :param user_id: 用户编号
    :return:成功与否
    """
    response = adminService.remover_member(user_id)
    return response


# 4.7 管理员修改成员信息
@router.post("/admin/profiles/modify", tags=["admin"])
async def edit_profiles(info: schemas.ProfilesEdit2):
    """
    :param info:当前用户编号，修改用户编号，修改码（1：修改职位，2：修改密码），修改内容
    :return:成功与否
    """
    response = adminService.edit_profiles(info)
    return response


# 4.8 管理员添加新品
@router.post("/admin/meals/add", tags=["admin"])
async def add_meal(
        file: bytes = File(...),
        food_name: str = Form(...),
        food_info: str = Form(...),
        food_price: str = Form(...),
        food_rmd: int = Form(...)
):
    """
    :param file: 菜品图片文件
    :param food_name: 菜品名
    :param food_info: 菜品信息
    :param food_price: 菜品价格
    :param food_rmd: 是否推荐菜品
    :return:成功与否
    """
    return adminService.add_meal(file, food_name, food_info, float(food_price), food_rmd)


# 4.9 管理员删除菜品信息
@router.get("/admin/meals/remove", tags=["admin"])
async def remove_meal(food_id: int):
    """
    :param food_id: 菜品编号
    :return: 成功与否
    """
    return adminService.remove_meal(food_id)


# 4.10 管理员修改菜品
@router.post("/admin/meals/modify", tags=["admin"])
async def modify_meal(
        file: bytes = File(...),
        food_id: int = Form(...),
        food_name: str = Form(...),
        food_info: str = Form(...),
        food_price: str = Form(...),
        food_rmd: int = Form(...)):
    """
    :param file: 菜品图片文件
    :param food_id:菜品编号
    :param food_name: 菜品名
    :param food_info: 菜品信息
    :param food_price: 菜品价格
    :param food_rmd: 是否推荐菜品
    :return:成功与否
    """
    return adminService.modify_meal(
        file,
        food_id,
        food_name,
        food_info,
        food_price,
        food_rmd
    )


# 4.11 管理员对桌子数量的修改
@router.get("/admin/table/modify", tags=["admin"])
async def modify_table_number(table_number: int):
    """
    :param table_number: 桌子数量
    :return: 成功与否
    """
    response = adminService.modify_table_number(table_number)
    return response


# # 4.12 管理员上传照片
# @adminRouter.post("/admin/image/photo", tags=["admin"])
# async def create_files(file: bytes = File(...), food_id: int = Form(...)):
#     response = adminService.modify_food_image(file, food_id)
#     return response

# 4.13 管理员返回菜品的信息
@router.get("/admin/meal/details/fetch", tags=["admin"])
async def get_meal_details(food_id: int):
    """
    :param food_id: 菜品编号
    :return: 菜品的全部信息组成的dict
    """
    response = adminService.get_meal_details(food_id)
    return response


# 4.14 管理员获取所有状态的订单
@router.get("/admin/orders/list", tags=["admin"])
async def get_orders():
    """
    :return: 一个list，包含状态为n的订单，其中包含{订单编号，桌位号、付款状态，订单创建时间}
    """
    response = adminService.get_orders()
    return response


# 4.15 管理员删除公告
@router.get("/admin/announcement/delete", tags=["admin"])
async def announcement_delete(notice_id: int):
    """
    :param notice_id: 公告编号
    :return:成功与否
    """
    response = adminService.announcement_delete(notice_id)
    return response
