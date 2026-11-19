# === Stage 8: Сортировка записей ===
# Project: FlowerShop
from datetime import datetime


def sort_bouquets(bouquets, by="name", reverse=False):
    if by == "name":
        key = lambda b: b["name"].lower()
    elif by == "created":
        key = lambda b: b["created"]
    else:
        raise ValueError("Неподдерживаемое поле для сортировки: " + str(by))
    return sorted(bouquets, key=key, reverse=reverse)


def sort_by_name(bouquets, reverse=False):
    return sort_bouquets(bouquets, by="name", reverse=reverse)


def sort_by_created(bouquets, reverse=False):
    return sort_bouquets(bouquets, by="created", reverse=reverse)


def add_bouquet(bouquets, name, flowers, price, created=None):
    if created is None:
        created = datetime.now()
    bouquet = {
        "name": name,
        "flowers": flowers,
        "price": price,
        "created": created,
    }
    bouquets.append(bouquet)
    return bouquet


def list_bouquets(bouquets, sort_by="name", reverse=False):
    if sort_by == "name":
        return sort_by_name(bouquets, reverse=reverse)
    if sort_by == "created":
        return sort_by_created(bouquets, reverse=reverse)
    return bouquets


def demo():
    bouquets = [
        {"name": "Розы", "flowers": ["роза", "роза"], "price": 1500, "created": datetime(2024, 1, 5)},
        {"name": "Тюльпаны", "flowers": ["тюльпан"], "price": 900, "created": datetime(2024, 1, 3)},
        {"name": "Микс", "flowers": ["роза", "тюльпан"], "price": 1200, "created": datetime(2024, 1, 7)},
    ]
    print("По названию (возр.):")
    for b in sort_by_name(bouquets, reverse=False):
        print(b["name"])
    print("По названию (убыв.):")
    for b in sort_by_name(bouquets, reverse=True):
        print(b["name"])
    print("По дате (возр.):")
    for b in sort_by_created(bouquets, reverse=False):
        print(b["name"])
    print("По дате (убыв.):")
    for b in sort_by_created(bouquets, reverse=True):
        print(b["name"])


if __name__ == "__main__":
    demo()
