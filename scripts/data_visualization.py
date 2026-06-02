import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/cleaned_retail_data.csv")

monthly_sales = df.groupby('Month')['TotalSales'].sum()

monthly_sales.plot(kind='bar')

plt.title("Monthly Sales")

plt.show()