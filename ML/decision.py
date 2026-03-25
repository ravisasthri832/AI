from sklearn.tree import DecisionTreeClassifier

X=[[2],[5],[6],[1]]

y=["Fail","Pass","Pass","Fail"]

model=DecisionTreeClassifier()
model.fit(X,y)
Res = model.predict([[4]])
print(Res)