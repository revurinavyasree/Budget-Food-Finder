import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

keyword = input("Enter food keyword: ").lower()

results = df[
    df["Menu_Item"]
    .str.lower()
    .str.contains(keyword, na=False)
]

results["Score"] = results["Menu_Item"].str.len()

results = results.sort_values(
    by="Score",
    ascending=False
)

if results.empty:
    print("No matching items found.")
else:
    print(results)
    