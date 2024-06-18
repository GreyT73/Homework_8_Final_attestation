import csv
import json
from pathlib import Path


def csv_to_json(old: Path, new: Path) -> None:
    result = []
    with open(old, 'r', encoding='UTF-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel-tab')
        for i, row in enumerate(csv_read):
            if i != 0:
                level, id, name = row
                data = {
                    "level": int(level),
                    'id': f'{int(id):010}',
                    'name': name.title(),
                    'hash': hash(f'{id}{name.title()}')
                }
                result.append(data)
    with open(new, 'w', encoding='utf-8') as f_write:
        json.dump(result, f_write, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    csv_to_json(Path('users.csv'), Path('new_users.json'))
