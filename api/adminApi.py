from fastapi import APIRouter
from service import adminService
import schemas

adminRouter = APIRouter()


# 4.1 发布公告消息
@adminRouter.post("api/announcement/post", tags=["admin"])
async def post_notice(notice_info: schemas.PostNoticeInfo):
    return adminService.post_notice(notice_info)


