#Neural Network Layer Examples

import numpy as np

inputs=np.array([1.0,2.0,3.0])
weights=np.array([[0.2,0.8,-0.5],
                 [0.5,-0.19,0.26],
                 [-0.22,0.9,0.4]]) 

biases=np.array([2.0,3.0,0.5])

output=np.dot(inputs,weights) + biases

def relu(output):
    return np.maximum(0,output)

res=relu(output)
print(res)
