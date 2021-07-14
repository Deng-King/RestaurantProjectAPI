from fastapi import APIRouter
from service import loginService
import schemas

loginRouter = APIRouter()


@loginRouter.post("/login", tags=["log"])
async def sign_in(info: schemas.LoginInfo):
    """
    功能:前端提供账号与密码，后端以此查询数据库\n
    参数:账号和密码\n
    返回:用户编号、用户编号对应的身份\n
    """
    response = loginService.login(info.user_number, info.user_pwd)
    return response
