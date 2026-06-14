import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

keyword = input("Enter food keyword: ").lower()

results = df[
    df["Menu_Item"]
    .str.lower()
    .str.contains(keyword, na=False)
]

if len(results) == 0:
    print("No matching items found.")
else:
    print("\nRecommendations:\n")
    print(results)