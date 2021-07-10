from util import responseCode
from dao.notice import notice_create
import settings
import schemas


def post_notice(info: schemas.PostNoticeInfo):
    success=notice_create.create(
        settings.ip,
        info.user_id,
        info.content,
        info.title,
        info.notice_level
    )
    return responseCode.resp_200(data=success)
