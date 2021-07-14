from pydantic import BaseModel
from typing import Optional, List


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
    user_id: int
    content: str

class ProfilesEdit2(BaseModel):
    user_id_a : int
    user_id_b : int 
    tag : int
    content : str 


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

class AdminAddFood(BaseModel):
    food_name: str
    food_info: str
    food_price: float
    food_recommend: int


class ModifyMeal(BaseModel):
    food_id: int
    food_name: str
    food_info: str
    food_price: float
    food_rmd: int


class ModifyOrder(BaseModel):
    order_id: int
    food_id: int


class MiniOrderInfo(BaseModel):
    food_id:int
    food_num:int


class OrderInfo(BaseModel):
    order_table: int
    order_total: float
    user_id: int
    meal_info: List[MiniOrderInfo]

class AdminAddMember(BaseModel):
    # 用户工号、职位、性别、姓名
    user_number: str
    user_position: int
    user_gender: int
    user_name: str

class TableNumber(BaseModel):
    table_number:int

class OrderState(BaseModel):
    order_id:int
    food_id:int
    
class FoodId(BaseModel):
    food_id:int