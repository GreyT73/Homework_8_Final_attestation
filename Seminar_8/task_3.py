import json
from pathlib import Path
import csv


def json_to_csv(path: Path) -> None:
    with open(path, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)
    result = []
    for level, id_name in data.items():
        for id, name in id_name.items():
            result.append({'level': int(level), 'id': int(id), 'name': name})

    with open(path.stem + ".csv", 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(result)
    print(result)
if __name__ == '__main__':
    json_to_csv(Path('users.json'))


