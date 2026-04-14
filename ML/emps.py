import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
#train_test_split used to split the data 1)training 2)testing
from sklearn.model_selection import train_test_split #[10,20,30,40] 80#training #20% testing

#Features (emp experiences)
X=np.array([2,3,4,5,6]).reshape(-1,1)
#print(X)

#label (salaries in lacks)
y=np.array([4,8,10,12,14])

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,random_state=42)
# print(X_train)
# print("-----------------")
# print(X_test)

model=LinearRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

print(y_pred, y_test)
# new_exp=[[6]]
# salary=model.predict(new_exp)
# print("salary for 6 years",salary[0])


print("Prediction:", y_pred)
print("Actual", y_test)