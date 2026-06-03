import pandas as pd

df = pd.read_csv("../data/cleaned_retail_data.csv")

top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

print(top_products)
print("\nData Analysis Completed Successfully!")