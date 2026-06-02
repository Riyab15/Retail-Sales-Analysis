import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

df = df.dropna()

df = df.drop_duplicates()

print(df.isnull().sum())