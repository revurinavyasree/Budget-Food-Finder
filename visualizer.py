import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_data.csv")

# -----------------------------
# 1. CATEGORY DISTRIBUTION
# -----------------------------
category_counts = df["Category"].value_counts()

plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar")

plt.title("Menu Items by Category")
plt.xlabel("Category")
plt.ylabel("Number of Items")

plt.tight_layout()
plt.savefig("charts/category_distribution.png")
plt.close()

print("Saved: category_distribution.png")


# -----------------------------
# 2. TOP 10 EXPENSIVE ITEMS
# -----------------------------
top_expensive = df.sort_values(by="Price", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_expensive["Menu_Item"], top_expensive["Price"])

plt.title("Top 10 Expensive Menu Items")
plt.xlabel("Price (₹)")
plt.ylabel("Menu Item")

plt.gca().invert_yaxis()  # highest on top

plt.tight_layout()
plt.savefig("charts/top_expensive_items.png")
plt.close()

print("Saved: top_expensive_items.png")