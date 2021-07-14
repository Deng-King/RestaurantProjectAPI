from fastapi import APIRouter
from service import noticeService

noticeRouter = APIRouter()


# 1.2获取公告消息功能
@noticeRouter.get("/announcement/fetch", tags=["notice"])
async def get_notice():
    return noticeService.get_notice()
