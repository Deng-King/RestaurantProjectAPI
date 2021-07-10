from fastapi import APIRouter
from service import loginService
from pydantic import BaseModel
import schemas

loginRouter = APIRouter()
class LoginInfo(BaseModel):
    user_number: str
    user_pwd: str

@loginRouter.post("/login",tags=["login"])
async def sign_in(info:LoginInfo):
    # user_number: str
    # user_pwd: str
    response = loginService.login(info.user_number,info.user_pwd)
    return response
