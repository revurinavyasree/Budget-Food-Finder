def categorize(item):
    item = item.lower()

    score = {
        "Bowls": 0,
        "Salads": 0,
        "Protein Plates": 0,
        "Drinks": 0,
        "Desserts": 0
    }

    if "bowl" in item:
        score["Bowls"] += 3
    if "salad" in item:
        score["Salads"] += 3
    if any(x in item for x in ["chicken", "steak", "salmon", "protein"]):
        score["Protein Plates"] += 3
    if any(x in item for x in ["tea", "water", "soda", "juice", "kombucha", "lemonade"]):
        score["Drinks"] += 3
    if any(x in item for x in ["dessert", "chocolate", "treat", "cookie"]):
        score["Desserts"] += 3

    # pick best match
    return max(score, key=score.get)