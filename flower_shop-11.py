# === Stage 11: Группировка ===
# Project: FlowerShop
def group_by_arrangement(bouquets):
    groups = {}
    for bouquet in bouquets:
        key = bouquet.get('состав')
        groups.setdefault(key, []).append(bouquet)
    return groups


def count_by_arrangement(bouquets):
    counts = {}
    for bouquet in bouquets:
        key = bouquet.get('состав')
        counts[key] = counts.get(key, 0) + 1
    return counts


def summarize_arrangements(bouquets):
    counts = count_by_arrangement(bouquets)
    total = sum(counts.values())
    report = []
    for arrangement, quantity in sorted(counts.items()):
        report.append(
            'Состав: {0}, количество: {1}, доля: {2:.1f}%'
            .format(arrangement, quantity, (quantity / total) * 100)
        )
    return report


if __name__ == '__main__':
    sample = [
        {'название': 'Весна', 'состав': 'розы', 'цена': 2000, 'дата': '2024-05-01'},
        {'название': 'Тюльпаны', 'состав': 'тюльпаны', 'цена': 1500, 'дата': '2024-05-02'},
        {'название': 'Ромашки', 'состав': 'ромашки', 'цена': 800, 'дата': '2024-05-03'},
        {'название': 'Весна-2', 'состав': 'розы', 'цена': 2200, 'дата': '2024-05-04'},
    ]
    for line in summarize_arrangements(sample):
        print(line)
