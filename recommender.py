import pandas as pd

df = pd.read_csv("data/cleaned_data.csv")

keyword = input("Enter food keyword: ").lower()
budget = int(input("Enter your budget (₹): "))

results = df[df["Menu_Item"].str.lower().str.contains(keyword, na=False)]

# If exact budget match fails → fallback
within_budget = results[results["Price"] <= budget]

if not within_budget.empty:
    print("\n🔥 Items within your budget:\n")
    print(within_budget.sort_values("Price")[["Menu_Item", "Price"]])

else:
    print("\n⚠ No items within budget. Showing closest matches:\n")

    closest = results.sort_values(
        by="Price",
        key=lambda x: abs(x - budget)
    ).head(5)

    print(closest[["Menu_Item", "Price"]])