# === Stage 3: Хранилище в памяти ===
# Project: FlowerShop
"""Хранилище букетов в памяти.

Модуль FlowerShop. Этап 3 из 57.
Самодостаточный модуль: только стандартная библиотека.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Type


@dataclass
class Bouquet:
    """Букет: название, состав, цена, дата сборки."""

    name: str
    composition: List[str]
    price: float
    assembly_date: str

    def __post_init__(self):
        self.name = self.name.strip()
        self.composition = list(self.composition)
        self.price = float(self.price)


class BouquetStore:
    """Хранилище букетов в памяти.

    Поддерживает добавление, получение по идентификатору
    и получение списка всех букетов.
    """

    def __init__(self):
        self._store: Dict[str, Bouquet] = {}
        self._counter = 0

    def add(self, bouquet: Bouquet) -> str:
        """Добавить букет и вернуть его идентификатор."""

        self._counter += 1
        bouquet_id = f"bouquet-{self._counter}"
        self._store[bouquet_id] = bouquet
        return bouquet_id

    def get(self, bouquet_id: str) -> Optional[Bouquet]:
        """Вернуть букет по идентификатору или None."""

        return self._store.get(bouquet_id)

    def exists(self, bouquet_id: str) -> bool:
        """Проверить наличие букета по идентификатору."""

        return bouquet_id in self._store

    def list_bouquets(self) -> List[Bouquet]:
        """Вернуть список всех букетов в порядке добавления."""

        return list(self._store.values())

    def __len__(self):
        return len(self._store)

    def __contains__(self, bouquet_id: str) -> bool:
        return bouquet_id in self._store
