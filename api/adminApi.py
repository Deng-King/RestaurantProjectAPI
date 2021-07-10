from fastapi import APIRouter
from service import adminService
import schemas

adminRouter = APIRouter()


# 4.1 发布公告消息
@adminRouter.post("/announcement/post", tags=["admin"])
async def post_notice(notice_info: schemas.PostNoticeInfo):
    return adminService.post_notice(notice_info)

# 4.5 管理员添加成员
@adminRouter.post("/admin/profiles/add", tags=["admin"])
async def add_member(info: schemas.AdminAddMember):
    # 用户工号、职位、性别、姓名
    # user_number: str
    # user_position: int
    # user_gender: int
    # user_name: str
    response = adminService.create_member(info.user_number,
                                        info.user_position,
                                        info.user_gender,
                                        info.user_name)
    return response


