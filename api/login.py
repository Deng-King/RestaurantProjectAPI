from fastapi import APIRouter
import schemas
from service import loginService

router = APIRouter()


@router.post("/login")
async def sign_in(info: schemas.LoginInfo):
    return loginService
