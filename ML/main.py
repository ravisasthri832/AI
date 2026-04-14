import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #CORSMiddleware will used to connect to react and other 
import pandas as pd
from sklearn.linear_model import LinearRegression
from pydantic import BaseModel #used to build the schema


app=FastAPI()  #initialising api
app.add_middleware(CORSMiddleware, 
                   allow_origins=["*"],
                   allow_cradentials=True,
                   allow_methods="*",
                   allow_headers=["*"]) # initializing CORSMiddleware

df=pd.read_csv("dataset/house_data.csv")
X=df[["size","bedrooms","age"]]
y=df[["price"]]

model=LinearRegression()
model.fit(X,y)

class HouseDetails(BaseModel):
    size:float
    bedrooms:int
    age:int

@app.post("/predict")
def prected_price(input:HouseDetails):
    house_details=np.array([[input.size,input.bedrooms,input.age]])
    price=model.predict(house_details)
    
    return{
        "predicted price":price[0]
    }


#uvicorn main:app --reload  #used to start the server