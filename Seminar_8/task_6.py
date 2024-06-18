from pathlib import Path
import pickle
import csv

def pickle_to_csv(path: Path) -> None:
    with open(path, 'rb') as f_read:
        data = pickle.load(f_read)
    headers = list(data[0].keys())
    with open(path.stem + '.csv', 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)



if __name__ == '__main__':
    pickle_to_csv(Path('new_users.pickle'))