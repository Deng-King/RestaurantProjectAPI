from fastapi import APIRouter
from fastapi import File
from fastapi import Form
from service import profilesService
from pydantic import BaseModel
import schemas

profilesRouter = APIRouter()

@profilesRouter.post("/profiles/exit",tags=["profiles"])
async def sign_out(info: schemas.ProfilesExit):
    # user_number: str
    # user_pwd: str
    response = profilesService.exit(info.user_id)
    return response

@profilesRouter.get("/profiles",tags=["profiles"])
async def get_profiles(user_id:int):
    # user_id: int
    response = profilesService.get_profiles(user_id)
    return response

@profilesRouter.get("/profiles/details",tags=["profiles"])
async def get_profiles_details(user_id: int):
    # user_id: int
    response = profilesService.get_profiles_details(user_id)
    return response

@profilesRouter.post("/profiles/edit",tags=["profiles"])
async def edit_profiles(info: schemas.ProfilesEdit):
    # 当前用户编号，修改用户编号，修改码（1：修改头像，2：修改密码），修改内容
    # user_id_a, user_id_b, tag, content
    response = profilesService.edit_profiles(info.user_id_a,
                                            info.user_id_b,
                                            info.tag,
                                            info.content)
    return response

@profilesRouter.post("/profiles/image/cover", tags=["profiles"])
async def create_files(file: bytes = File(...), user_id: str = Form(...)):
    response = profilesService.modify_image(file,user_id)
    return response
