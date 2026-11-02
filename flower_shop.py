# === Stage 1: Каркас модуля ===
# Project: FlowerShop
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Bouquet:
    name: str
    composition: list
    price: float
    assembled: date


def make_demo_bouquets() -> list:
    bouquets = [
        Bouquet(
            name="Весенний микс",
            composition=["Розы", "Тюльпаны", "Гиацинты"],
            price=2500.0,
            assembled=date(2024, 4, 10),
        ),
        Bouquet(
            name="Белая нежность",
            composition=["Пионы", "Лилии", "Розы"],
            price=3800.0,
            assembled=date(2024, 5, 22),
        ),
        Bouquet(
            name="Полевой шик",
            composition=["Мак", "Коровий цикорий", "Лаванда"],
            price=1900.0,
            assembled=date(2024, 6, 15),
        ),
    ]
    return bouquets


def main() -> None:
    for bouquet in make_demo_bouquets():
        print(bouquet.name)
        print(bouquet.composition)
        print(bouquet.price)
        print(bouquet.assembled)
        print()


if __name__ == "__main__":
    main()
