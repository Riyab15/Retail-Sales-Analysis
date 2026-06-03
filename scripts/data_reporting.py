import pandas as pd

df = pd.read_csv("../data/prepared_retail_data.csv")

print("================================")
print("RETAIL SALES ANALYSIS REPORT")
print("================================")

print("\nTotal Records:")
print(len(df))

print("\nTotal Sales:")
print(df['TotalSales'].sum())

print("\nTop 5 Countries:")
print(df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head())

print("\nReport Generated Successfully!")