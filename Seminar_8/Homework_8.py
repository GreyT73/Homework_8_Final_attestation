import json
import os
from pathlib import Path
from task_5 import json_to_pickle
import csv


def rec_search(path: str | Path = os.curdir, list_of_files: list = [] ) -> None:
    for i in os.listdir(path):
        sub_i = path + '\\' + i
        if Path(sub_i).is_dir():
            fsize = 0
            for file in Path(sub_i).rglob('*'):
                if os.path.isfile(file):
                    fsize += os.path.getsize(file) / 1024
        dic = {"Название": i, "Тип": "Folder" if os.path.isdir(sub_i) else "File", "Местонахождение": path,
               "Размер": f'{fsize:.1f} KB' if Path(sub_i).is_dir() else f'{os.path.getsize(sub_i) / 1024:.1f} KB'}
        if os.path.isdir(sub_i):
            rec_search(sub_i, list_of_files)
        list_of_files.append(dic)
    with open('files.json', 'w', encoding='utf-8') as f:
        json.dump(list_of_files, f, ensure_ascii=False, indent=4)
    with open("files.csv", 'w', encoding='utf-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=list_of_files[0].keys(), dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(list_of_files)

if __name__ == '__main__':
    path = os.curdir
    rec_search(path)
    json_to_pickle(Path(path))

