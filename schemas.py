from pydantic import BaseModel
from typing import Optional


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


class PostNoticeInfo(BaseModel):
    user_id: int
    content: str
    title: str
    notice_level: int


class FoodInfo(BaseModel):
    food_id: Optional[int] = None
    food_name: str
    food_info: str
    food_price: float
    food_recommend: int
    food_img: str
