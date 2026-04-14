import numpy as np

#tensorflow is Deep learning library (Engine)
import tensorflow as tf

#keros used to build Deep learning models (Steering)
from tensorflow import keras

#create model

model=keras.Sequential([
    keras.layers.Dense(3,activation='relu'),
    keras.layers.Dense(1,)
])

#compile the model

model.compile(
    optimizer='adam', #adjust weight to munimize error
    loss='mean_squared_error'
)

X=np.array([[1],[2],[3]],dtype=float)
y=np.array([[2],[4],[6]],dtype=float) #y=2x

model.fit(X,y, epochs=500)
output=model.predict(np.array([[5.0]]))

print(output)