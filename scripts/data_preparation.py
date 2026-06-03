import pandas as pd

df = pd.read_csv("../data/cleaned_retail_data.csv")

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

df['TotalSales'] = df['Quantity'] * df['UnitPrice']

df['Month'] = df['InvoiceDate'].dt.month

df['Year'] = df['InvoiceDate'].dt.year

df.to_csv("../data/prepared_retail_data.csv", index=False)

print("Data Preparation Completed Successfully!")