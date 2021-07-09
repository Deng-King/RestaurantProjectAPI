from fastapi import APIRouter
import schemas

router=APIRouter()

@router.post("/signin")
async def signin(info:schemas.loginInfo):
    return {"user_position":"管理员"}
