from fastapi import APIRouter
from service import loginService
import schemas

loginRouter = APIRouter()

@loginRouter.post("/login",tags=["log"])
async def sign_in(info:schemas.LoginInfo):
    # user_number: str
    # user_pwd: str
    response = loginService.login(info.user_number,info.user_pwd)
    return response
