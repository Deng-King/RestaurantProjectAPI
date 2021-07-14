from fastapi import APIRouter
from service import noticeService

noticeRouter = APIRouter()


# 1.2获取公告消息功能
@noticeRouter.get("/announcement/fetch", tags=["notice"])
async def get_notice():
    """
    Usage::获取全部的公告列表
    :return:很多公告组成的list[]，每一个元素包含一个字典：
    {公告ID，公告创建人姓名，公告内容，公告标题，公告创建时间，公告重要级}
    """
    return noticeService.get_notice()
