from fastapi import APIRouter
from service import noticeService

router = APIRouter()


# 1.2获取公告消息功能
@router.get("/announcement/fetch", tags=["notice"])
async def get_notice():
    """
    :return: 所有公告组成的list，其中的公告是dict类型
    """
    return noticeService.get_notice()
