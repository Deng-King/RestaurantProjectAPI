from pydantic import BaseModel


class loginInfo(BaseModel):
    user_id: str
    user_pwd: str
