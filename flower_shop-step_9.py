# === Stage 9: Текстовый поиск ===
# Project: FlowerShop
from difflib import SequenceMatcher


def find_bouquets_by_text(bouquets, query):
    """Поиск букетов по текстовым полям без учёта регистра.

    Ищет совпадения по названию и составу. Для каждой найденной
    строки выводит её с подсветкой совпавших символов из запроса.
    """
    query = query.strip().lower()
    if not query:
        return

    for bouquet in bouquets:
        name = str(bouquet.get("name", "")).lower()
        composition = str(bouquet.get("composition", "")).lower()

        if not (query in name or query in composition):
            continue

        name_highlighted = _highlight(name, query)
        composition_highlighted = _highlight(composition, query)

        print(f"Название: {name_highlighted}")
        print(f"Состав:   {composition_highlighted}")
        print(f"Цена:     {bouquet.get('price', '—')}")
        print(f"Собран:   {bouquet.get('assembled_at', '—')}")
        print("-" * 40)


def _highlight(text, query):
    """Подсвечивает символы, совпадающие с запросом, звёздочками."""
    result = list(text)
    query_len = len(query)

    for start in range(len(result)):
        if query_len == 0:
            break
        if start + query_len > len(result):
            break
        if "".join(result[start:start + query_len]) == query:
            for index in range(start, start + query_len):
                result[index] = "*"
            start += query_len - 1

    return "".join(result)


if __name__ == "__main__":
    sample = [
        {
            "name": "Весенний микс",
            "composition": "Розы, тюльпаны, нарциссы",
            "price": 1200,
            "assembled_at": "2025-01-15",
        },
        {
            "name": "Полевые краски",
            "composition": "Мак, василёк, ромашка",
            "price": 800,
            "assembled_at": "2025-01-16",
        },
        {
            "name": "Розовая классика",
            "composition": "Пионы, розы, эвкалипт",
            "price": 2500,
            "assembled_at": "2025-01-17",
        },
    ]

    print("Поиск: розы")
    find_bouquets_by_text(sample, "розы")

    print("Поиск: НАРЦИССЫ")
    find_bouquets_by_text(sample, "НАРЦИССЫ")

    print("Поиск: пион")
    find_bouquets_by_text(sample, "пион")
