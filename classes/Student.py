from pydantic import BaseModel, Field
class Student(BaseModel):
    id: str
    name: str
    age: int


# if __name__ == "__main__":
#     s = Student(123,123,123)
#     print(s)