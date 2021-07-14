from fastapi import APIRouter
from service import loginService
import schemas

loginRouter = APIRouter()


@loginRouter.post("/login", tags=["log"])
async def sign_in(info: schemas.LoginInfo):
    """
    接口功能：使用用户名和密码进行登陆操作\n
    接收参数：user_number(str), user_pwd(str)\n
    返回数据：data = {"user_id": id, "user_position": position}\n
    """
    response = loginService.login(info.user_number, info.user_pwd)
    return response
