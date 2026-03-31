import pandas as pd
#TransactionEncoder is used to convert the transaction data as true or false or 1 or 0

from mlxtend.preprocessing import TransactionEncoder
#apriori is used to know frequency
# association _rules used to form the rules
from mlxtend.frequent_patterns import apriori, association_rules

#step 1
transactions=[
    ["Milk","Bread"],
    ["Milk","Butter"],
    ["Bread","Butter"],
    ["Milk","Bread"],
    ["Milk","Bread","Butter"]
]

#Step 2: Convert to Dataframe
te=TransactionEncoder()
te_data=te.fit(transactions).transform(transactions)
df=pd.DataFrame(te_data,columns=te.columns_)

print("Dataset:\n",df)

#Step 3:
frequest_items=apriori(df,min_support=0.6,use_colnames=True)
#print("\nFrequest Itemsets:\n",frequest_items)

#step4: Generate rules
rules=association_rules(frequest_items,metric="confidence",min_threshold=0.7)
print("\n Association Rules:\n",rules)