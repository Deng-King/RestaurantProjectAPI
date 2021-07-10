from pydantic import BaseModel


class LoginInfo(BaseModel):
    user_number: str
    user_pwd: str
