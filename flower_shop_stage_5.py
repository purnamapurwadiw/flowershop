# === Stage 5: Удаление и восстановление ===
# Project: FlowerShop
from datetime import datetime

class Bouquet:
    def __init__(self, bouquet_id, name, flowers, price, assembled_at):
        self.bouquet_id = bouquet_id
        self.name = name
        self.flowers = flowers
        self.price = price
        self.assembled_at = assembled_at

    def to_dict(self):
        return {
            "bouquet_id": self.bouquet_id,
            "name": self.name,
            "flowers": self.flowers,
            "price": self.price,
            "assembled_at": self.assembled_at,
        }


class SoftDeletedBouquet(Bouquet):
    def __init__(self, bouquet_id, name, flowers, price, assembled_at, deleted_at, reason):
        super().__init__(bouquet_id, name, flowers, price, assembled_at)
        self.deleted_at = deleted_at
        self.reason = reason

    def to_dict(self):
        data = self.to_dict()
        data["deleted"] = True
        data["deleted_at"] = self.deleted_at
        data["reason"] = self.reason
        return data


class BouquetRepository:
    def __init__(self):
        self._items = {}

    def add(self, bouquet):
        self._items[bouquet.bouquet_id] = bouquet

    def get(self, bouquet_id):
        return self._items.get(bouquet_id)

    def remove(self, bouquet_id, reason="user request"):
        bouquet = self._items.get(bouquet_id)
        if bouquet is None:
            return None
        deleted = SoftDeletedBouquet(
            bouquet.bouquet_id,
            bouquet.name,
            bouquet.flowers,
            bouquet.price,
            bouquet.assembled_at,
            deleted_at=datetime.now().isoformat(),
            reason=reason,
        )
        del self._items[bouquet_id]
        return deleted

    def restore(self, bouquet_id):
        deleted = self._soft_deleted.get(bouquet_id)
        if deleted is None:
            return None
        bouquet = Bouquet(
            deleted.bouquet_id,
            deleted.name,
            deleted.flowers,
            deleted.price,
            deleted.assembled_at,
        )
        self._items[bouquet.bouquet_id] = bouquet
        self._soft_deleted.pop(bouquet_id, None)
        return bouquet


class SoftDeletedBouquetRepository:
    def __init__(self, source):
        self._source = source

    def list(self):
        return list(self._source._soft_deleted.values())


BouquetRepository._soft_deleted = {}
