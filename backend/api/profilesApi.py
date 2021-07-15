from fastapi import APIRouter
from fastapi import File
from fastapi import Form
from service import profilesService
import schemas

profilesRouter = APIRouter()


# 1.5退出请求 ***********要改
@profilesRouter.post("/profiles/exit", tags=["profiles"])
async def sign_out(info: schemas.ProfilesExit):
    """
    :param info:
    :return:
    """
    response = profilesService.exit(info.user_id)
    return response

# 1.6获取个人信息概览
@profilesRouter.get("/profiles", tags=["profiles"])
async def get_profiles(user_id: int):
    """
    :param user_id:用户编号
    :return:字典：{用户编号、用户工号、用户姓名、职位}
    """
    response = profilesService.get_profiles(user_id)
    return response


# 1.4个人信息详细查询
@profilesRouter.get("/profiles/details", tags=["profiles"])
async def get_profiles_details(user_id: int):
    """
    :param user_id:用户编号
    :return:字典：{用户编号，用户工号、职位（字符串）、头像路径、性别(字符串)、姓名}
    """
    response = profilesService.get_profiles_details(user_id)
    return response


# 1.3 修改个人密码功能
@profilesRouter.post("/profiles/edit", tags=["profiles"])
async def edit_profiles(info: schemas.ProfilesEdit):
    """
    :param info: 一个包含用户编号与修改内容的对象
    :return: 成功与否
    """
    response = profilesService.edit_profiles(info.user_id,
                                             info.user_id,
                                             2,
                                             info.content)
    return response


# 1.7 修改个人头像功能
@profilesRouter.post("/profiles/image/cover", tags=["profiles"])
async def modify_image(file: bytes = File(...), user_id: int = Form(...)):
    """
    :param file:头像文件
    :param user_id:用户编号
    :return:成功与否
    """
    response = profilesService.modify_image(file,user_id)
    return response
