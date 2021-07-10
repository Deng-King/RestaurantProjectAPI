from pydantic import BaseModel


class LoginInfo(BaseModel):
    user_id: str
    user_pwd: str
