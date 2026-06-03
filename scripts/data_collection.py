import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

print("Dataset Loaded Successfully!")
print("\nFirst 5 Records:\n")
print(df.head())

print("\nDataset Shape:", df.shape)