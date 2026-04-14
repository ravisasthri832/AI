#Perceptron Model Examples

import numpy as np
inputs=np.array([1.0,2.0,3.0])
weights=np.array([0.2,0.8,-0.5])

bias=2.0

output=np.dot(inputs,weights) + bias
print(output)

def relu(x):
    return np.maximum(0,x)
    

# x<0 ------> 0
# x>0 ------> 1