import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# X= [[1],[2],[33],[11]] #input must be 2d array

#define features
#2d shape
X=np.array([1,2,3,4,5]).reshape(-1,1) #converting 1d to 2d
#print(X)

#define labels
y=np.array([10,20,30,40,50])

#choose the model
model=LinearRegression()

#train the model
model.fit(X,y)

# test the model (predict the model)
sample=[[30]]
marks = model.predict(sample)
print(marks[0])

plt.scatter(X,y, color="red")
plt.scatter(sample,marks)
plt.plot(X,y,color="blue")


plt.show()