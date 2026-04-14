# FastAPI is the class available in "fastapi" module/library
from fastapi import FastAPI

#import Base Model and Schema from another file
from student import Student

#CORSMiddleware used to connect with other technologies with different port numbers
from fastapi.middleware.cors import CORSMiddleware

#app object used to develoep the API calls
app=FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_cradentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
 

def home():
    return {"message":"Welcome to basic example of FastAPI !"}

#path Parameter
@app.get("/student/{id}")
def get_student(id:int):
    return {"Student id":id}


#query parameter
@app.get("/search")
def search(name:str,age:int):
    return {"name":name,"age":age}    

#Post Request
@app.post("/add")
def add_student(student:Student):
    return {"data":student}

#Put Request
@app.put("/update/{id}")
def update_student(id:int,std:Student):
    return {"id":id,"update_data":std}

@app.delete("/delete/{id}")
def delete_student(id:int):
    return {"message": f"Student:{id} deleted"}
