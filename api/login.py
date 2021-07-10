from fastapi import APIRouter
import schemas

router = APIRouter()


@router.post("/login")
async def sign_in(info: schemas.LoginInfo):
    return {"user_position": "管理员"}
