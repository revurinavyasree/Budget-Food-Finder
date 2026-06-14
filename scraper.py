import requests
from bs4 import BeautifulSoup

url = "https://www.sweetgreen.com/menu"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

print("HEADINGS FOUND:\n")

for heading in soup.find_all(["h1", "h2", "h3"]):
    text = heading.get_text(strip=True)

    if text:
        print(text)