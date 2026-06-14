# cleaner.py

import pandas as pd

df = pd.read_csv("data/raw_data.csv")

categories = {
    "Wraps": [],
    "Bowls": [],
    "Salads": [],
    "Drinks": [],
    "Dessert": [],
    "Sides": []
}

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

df.to_csv("data/cleaned_data.csv", index=False)

print("Data cleaned successfully")