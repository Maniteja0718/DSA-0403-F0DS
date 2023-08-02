import pandas as pd
data={
    'product_name':['A','B','C','D','E','F','G','H','I','J'],
    'sales':[35,67,4,53,67,45,32,34,87,38]
    }
df=pd.DataFrame(data)
print(df)
sorted_df=df.sort_values(by='sales',ascending=False)
top_5_products=sorted_df.head(5)
print(top_5_products)
