from sklearn.cluster import AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt

#step 1: Data
X=np.array([
    [1,2],[3,5],[7,4],[8,8],[9,0],[3,3]
])

#step 2: Model
model=AgglomerativeClustering(n_clusters=4)

#step 3: Training + Predict
labels= model.fit_predict(X)

print("Cluster Labels:", labels)

#step 4: Scatter Plot
plt.scatter(X[:,0],X[:,1],c=labels)

#Optional: Label points
for i,txt in enumerate(range(len(X))):
    plt.annotate(txt,(X[i,0],X[i,1]))

plt.title("Agglomerative Clustering")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()                       