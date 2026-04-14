from sklearn import svm

X=[[1],[2],[4],[5],[6]]

y=[0,0,1,1,1]

model=svm.SVC(kernel="linear")
model.fit(X,y)
print("co-efficient w value", model.coef_)
print("intercept or biase value", model.intercept_)
res=model.predict([[7]])
print(res)
