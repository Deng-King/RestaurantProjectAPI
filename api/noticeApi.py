from fastapi import APIRouter
from service import noticeService
import schemas

noticeRouter = APIRouter()


@noticeRouter.get("/announcement/fetch", tags=["notice"])
async def get_notice():
    return noticeService.get_notice()
