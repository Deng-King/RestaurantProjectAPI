from fastapi import APIRouter
from service import profilesService
from pydantic import BaseModel
import schemas

profilesRouter = APIRouter()

@profilesRouter.post("/profiles/exit",tags=["profiles"])
async def sign_out(info:schemas.ProfilesExit):
    # user_number: str
    # user_pwd: str
    response = profilesService.exit(info.user_id)
    return response
