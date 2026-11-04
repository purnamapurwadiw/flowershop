# === Stage 2: Проверка полей ===
# Project: FlowerShop
from datetime import datetime


class FlowerValidationError(Exception):
    pass


def normalize_text(value):
    if value is None:
        return ""
    return str(value).strip()


def normalize_price(value):
    if value is None or value == "":
        return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        raise FlowerValidationError("Цена должна быть числом.")


def validate_name(value):
    name = normalize_text(value)
    if not name:
        raise FlowerValidationError("Название букета не может быть пустым.")
    if len(name) > 100:
        raise FlowerValidationError("Название букета слишком длинное.")
    return name


def validate_composition(value):
    composition = normalize_text(value)
    if not composition:
        raise FlowerValidationError("Состав букета не может быть пустым.")
    if len(composition) > 500:
        raise FlowerValidationError("Состав букета слишком длинный.")
    return composition


def validate_price(value):
    price = normalize_price(value)
    if price < 0:
        raise FlowerValidationError("Цена не может быть отрицательной.")
    return price


def validate_assembly_date(value):
    date_str = normalize_text(value)
    if not date_str:
        raise FlowerValidationError("Дата сборки не может быть пустой.")
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        raise FlowerValidationError("Дата сборки должна быть в формате ГГГГ-ММ-ДД.")


def normalize_bouquet_data(raw):
    data = {
        "name": None,
        "composition": None,
        "price": None,
        "assembly_date": None,
    }
    if raw.get("name") is not None:
        data["name"] = validate_name(raw["name"])
    if raw.get("composition") is not None:
        data["composition"] = validate_composition(raw["composition"])
    if raw.get("price") is not None:
        data["price"] = validate_price(raw["price"])
    if raw.get("assembly_date") is not None:
        data["assembly_date"] = validate_assembly_date(raw["assembly_date"])
    return data
