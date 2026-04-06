# To read post parameter we need basemodel
from pydantic import BaseModel

#defining the schema of student with a call
class Student(BaseModel):
    name:str
    age:int
    standard:str
    marks:int