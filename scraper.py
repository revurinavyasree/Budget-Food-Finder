import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.sweetgreen.com/menu"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

menu_items = []

for heading in soup.find_all(["h2", "h3"]):
    text = heading.get_text(strip=True)

    if text:
        menu_items.append(text)

df = pd.DataFrame(menu_items, columns=["Menu_Item"])

df.to_csv("data/raw_data.csv", index=False)

print(f"Saved {len(df)} menu items to data/raw_data.csv")