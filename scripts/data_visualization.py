import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_retail_data.csv")

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['TotalSales'] = df['Quantity'] * df['UnitPrice']
df['Month'] = df['InvoiceDate'].dt.month

# Monthly Sales
monthly_sales = df.groupby('Month')['TotalSales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.tight_layout()
plt.show()

# Top Products
top_products = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,5))
top_products.plot(kind='bar')
plt.title("Top 10 Products")
plt.tight_layout()
plt.show()

# Top Countries
top_countries = (
    df.groupby('Country')['TotalSales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,5))
top_countries.plot(kind='bar')
plt.title("Top Countries by Sales")
plt.tight_layout()
plt.show()

print("All Visualizations Generated Successfully!")