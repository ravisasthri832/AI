import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
data = {
"Outlook": ["Sunny","Sunny","Overcast","Rain","Rain","Rain","Overcast","Sunny"],
"Temperature": ["Hot","Hot","Hot","Mild","Cool","Cool","Mild","Hot"],
"Humidity": ["High","High","High","High","Normal","Normal","Normal","High"],
"Play": ["No","No","Yes","Yes","Yes","No","Yes","No"]
}

df=pd.DataFrame(data)
print(df)
encoder=LabelEncoder()
df["Outlook"]=encoder.fit_transform(df["Outlook"])
df["Temperature"]=encoder.fit_transform(df["Temperature"])
df["Humidity"]=encoder.fit_transform(df["Humidity"])
df["Play"]=encoder.fit_transform(df["Play"])

X=df[["Outlook","Temperature","Humidity"]]
y=df["Play"]
model=RandomForestClassifier(n_estimators=10,criterion="entropy")
model.fit(X,y)
res=model.predict([[1,0,1]])
print(res[0])