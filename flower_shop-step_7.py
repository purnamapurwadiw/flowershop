# === Stage 7: Генерация идентификаторов ===
# Project: FlowerShop
import uuid
from datetime import datetime


def generate_project_id(prefix: str) -> str:
    """Генерация уникального идентификатора с префиксом проекта."""
    unique_id = uuid.uuid4().hex
    return f"{prefix}_{unique_id}"


class IDRegistry:
    """Регистр идентификаторов с проверкой коллизий."""

    def __init__(self, prefix: str) -> None:
        self.prefix = prefix
        self._used = set()

    def generate(self) -> str:
        """Генерация уникального идентификатора без коллизий."""
        while True:
            candidate = generate_project_id(self.prefix)
            if candidate not in self._used:
                self._used.add(candidate)
                return candidate

    def is_available(self, candidate: str) -> bool:
        """Проверка доступности идентификатора."""
        return candidate not in self._used


def create_bouquet_id(registry: IDRegistry) -> str:
    """Создание идентификатора для букета."""
    return registry.generate()


def create_flower_id(registry: IDRegistry) -> str:
    """Создание идентификатора для цветка."""
    return registry.generate()


if __name__ == "__main__":
    bouquet_registry = IDRegistry("bouquet")
    flower_registry = IDRegistry("flower")

    bouquet_1 = create_bouquet_id(bouquet_registry)
    bouquet_2 = create_bouquet_id(bouquet_registry)
    flower_1 = create_flower_id(flower_registry)

    print(f"Букет 1: {bouquet_1}")
    print(f"Букет 2: {bouquet_2}")
    print(f"Цветок 1: {flower_1}")
    print(f"Уникальность букетов: {bouquet_1 != bouquet_2}")
    print(f"Букет и цветок из разных регистров: {bouquet_1.split('_')[0] != flower_1.split('_')[0]}")
