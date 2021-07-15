from fastapi import APIRouter
from service import loginService
import schemas

router = APIRouter()


# 1.1登陆和身份验证功能
@router.post("/login", tags=["log"])
async def login(info: schemas.LoginInfo):
    """
    :param info:一个包含登录信息的对象
    :return:用户编号、用户编号对应的身份
    """
    response = loginService.login(info)
    return response
