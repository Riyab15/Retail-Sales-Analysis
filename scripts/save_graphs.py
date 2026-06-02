import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv("../data/cleaned_retail_data.csv")

# Create TotalSales
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Convert Date
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# -------------------------
# Monthly Sales
# -------------------------

df['Month'] = df['InvoiceDate'].dt.month

monthly_sales = df.groupby('Month')['TotalSales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.savefig("../visualizations/monthly_sales.png")
plt.close()

# -------------------------
# Top Products
# -------------------------

top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,5))
top_products.plot(kind='bar')
plt.title("Top 10 Products")
plt.savefig("../visualizations/top_products.png")
plt.close()

# -------------------------
# Country Sales
# -------------------------

top_countries = df.groupby('Country')['TotalSales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,5))
top_countries.plot(kind='bar')
plt.title("Country Sales")
plt.savefig("../visualizations/country_sales.png")
plt.close()

# -------------------------
# Heatmap
# -------------------------

plt.figure(figsize=(8,5))
sns.heatmap(
    df[['Quantity','UnitPrice','TotalSales']].corr(),
    annot=True
)
plt.title("Heatmap")
plt.savefig("../visualizations/heatmap.png")
plt.close()

# -------------------------
# Time Series
# -------------------------

daily_sales = df.groupby(df['InvoiceDate'].dt.date)['TotalSales'].sum()

plt.figure(figsize=(14,6))
daily_sales.plot()
plt.title("Time Series Sales Trend")
plt.savefig("../visualizations/time_series_sales.png")
plt.close()
# -------------------------
# Sales Distribution
# -------------------------

plt.figure(figsize=(10,5))

plt.hist(df['TotalSales'], bins=50)

plt.title("Sales Distribution")

plt.xlabel("Sales Amount")

plt.ylabel("Frequency")

plt.savefig("../visualizations/sales_distribution.png")

plt.close()
# -------------------------
# Monthly Orders
# -------------------------

monthly_orders = df.groupby('Month')['InvoiceNo'].nunique()

plt.figure(figsize=(10,5))

monthly_orders.plot(kind='bar')

plt.title("Monthly Orders")

plt.xlabel("Month")

plt.ylabel("Number of Orders")

plt.savefig("../visualizations/monthly_orders.png")

plt.close()
# -------------------------
# Top Customers
# -------------------------

top_customers = (
    df.groupby('CustomerID')['TotalSales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))

top_customers.plot(kind='bar')

plt.title("Top 10 Customers")

plt.xlabel("Customer ID")

plt.ylabel("Revenue")

plt.savefig("../visualizations/top_customers.png")

plt.close()

print("All Graphs Saved Successfully!")