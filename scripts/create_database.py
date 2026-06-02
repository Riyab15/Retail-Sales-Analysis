import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_retail_data.csv")

# Create SQLite database
conn = sqlite3.connect("../database/retail_sales.db")

# Save table
df.to_sql("retail_sales", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("Database Created Successfully!")