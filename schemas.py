from pydantic import BaseModel


class LoginInfo(BaseModel):
    user_number: str
    user_pwd: str

class ProfilesExit(BaseModel):
    user_id: int

class Profiles(BaseModel):
    # 用户编号
    user_id: int

class ProfilesEdit(BaseModel):
    # user_id_a, user_id_b, tag, content
    user_id_a: int
    user_id_b: int
    tag: int
    content: str
