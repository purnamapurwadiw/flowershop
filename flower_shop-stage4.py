# === Stage 4: Редактирование записей ===
# Project: FlowerShop
import datetime

ALLOWED_FIELDS = ("name", "composition", "price", "assembly_date")


def _validate_value(field, value):
    if field == "name":
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name должен быть непустой строкой")
    elif field == "composition":
        if not isinstance(value, (list, tuple)):
            raise ValueError("composition должен быть списком или кортежем")
        for item in value:
            if not isinstance(item, str) or not item.strip():
                raise ValueError("каждый элемент composition должен быть непустой строкой")
    elif field == "price":
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("price должен быть числом")
        if value <= 0:
            raise ValueError("price должен быть положительным")
    elif field == "assembly_date":
        if not isinstance(value, datetime.date):
            raise ValueError("assembly_date должен быть объектом datetime.date")


def edit_bouquet(bouquet_id, changes):
    updated = dict(changes)
    for field, value in updated.items():
        if field not in ALLOWED_FIELDS:
            raise ValueError(f"поле {field} нельзя изменять")
    _validate_value(field, value)
    return updated
