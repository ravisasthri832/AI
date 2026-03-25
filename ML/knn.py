import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X1=pd.read_csv("body.csv")
print(X1(2,2))
X=[[150,50],[160,55],[170,65],[180,80],[175,75]]

y=["Slim","Slim","Fit","Heavy","Heavy"]

model=KNeighborsClassifier(n_neighbors=4) 
model.fit(X,y)
res=model.predict([[165,60]])
print(res)