import numpy as np
import pandas as pd
#split data into training data and testing data
from sklearn.model_selection import train_test_split
#for Normalization
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
import matplotlib.pyplot as plt
#load predefined dataset
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
#print(data)
X = data.data # input data
y = data.target # Output data

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.2, random_state=42)

scalar=StandardScaler()
X_train=scalar.fit_transform(X_train)
#transform --> for normalization
# fit --> Allo model to learn patterns
X_test=scalar.transform(X_test)

model=keras.Sequential([
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

#training
history=model.fit(X_train,y_train,epochs=100,validation_data=(X_test,y_test))

#history.history["accuracy"] --> Train (80%) plot
#history.history["val_accuracy"] --> Test (20%) plot

if model.predict(X_test[0].reshape(1,-1))[0][0] > 0.5:
    print("Not effected with Cancer, Safe")
else:
    print("Effected, Danger!!!!!")

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Trainng <> Test ")
plt.legend(["Train","Test"])
plt.show()
