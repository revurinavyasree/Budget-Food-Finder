import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_data.csv")

top_items = (
    df["Menu_Item"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(8,5))
top_items.plot(kind="bar")

plt.title("Top Menu Items")
plt.tight_layout()

plt.savefig("charts/top_menu_items.png")

print("Chart saved.")