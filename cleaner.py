import pandas as pd

df = pd.read_csv("data/raw_data.csv")

df = df.drop_duplicates()

df = df.dropna()

df.to_csv("data/cleaned_data.csv", index=False)

print("Data cleaned successfully")