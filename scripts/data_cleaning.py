import pandas as pd

df = pd.read_csv("../data/online_retail.csv")

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("../data/cleaned_retail_data.csv", index=False)

print("Data Cleaning Completed Successfully!")
print(df.isnull().sum())