# === Stage 10: Поиск по нескольким словам ===
# Project: FlowerShop
def search_bouquets(bouquets, query):
    """Поиск букетов по нескольким словам с поддержкой исключений через префикс '-'.

    Искать в названии и составе букета. Слово с префиксом '-' исключает
    букеты, содержащие это слово. Поиск регистронезависимый. Возвращает
    список найденных объектов.
    """
    query = query.strip()
    tokens = query.split()
    positive = [tok for tok in tokens if not tok.startswith('-')]
    negative = [tok.lstrip('-') for tok in tokens if tok.startswith('-')]

    if not positive:
        return []

    query_words = [w.lower() for w in positive]
    exclude_words = [w.lower() for w in negative]

    results = []
    for bouquet in bouquets:
        name = (bouquet.get('name') or '').lower()
        composition = ' '.join(bouquet.get('composition') or [])
        haystack = name + ' ' + composition

        if not any(word in haystack for word in query_words):
            continue
        if any(word in haystack for word in exclude_words):
            continue
        results.append(bouquet)

    return results


if __name__ == '__main__':
    demo = [
        {'name': 'Весенний', 'composition': ['ромашка', 'тюльпан'], 'price': 1500, 'date': '2024-01-01'},
        {'name': 'Полевой', 'composition': ['ромашка', 'мак'], 'price': 1200, 'date': '2024-01-02'},
        {'name': 'Летний', 'composition': ['роза', 'лилия'], 'price': 2300, 'date': '2024-01-03'},
        {'name': 'Тюльпанный', 'composition': ['тюльпан'], 'price': 900, 'date': '2024-01-04'},
    ]

    print('ромашка:', search_bouquets(demo, 'ромашка'))
    print('ромашка -мак:', search_bouquets(demo, 'ромашка -мак'))
    print('роза тюльпан:', search_bouquets(demo, 'роза тюльпан'))
    print('роза -роза:', search_bouquets(demo, 'роза -роза'))
