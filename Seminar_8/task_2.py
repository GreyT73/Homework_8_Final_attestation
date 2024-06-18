import json
from pathlib import Path


def input_user(path: Path) -> None:
    unique_id = set()
    if not path.is_file():
        data = {str(level): {} for level in range(1, 8)}
    else:
        with open(path, 'r', encoding='utf-8') as f_read:
            data = json.load(f_read)
            #unique_id = {id for id_name in data.values() for id in id_name.keys()}
            for id_name in data.values():
                unique_id.update(id_name.keys())

    while name := input("Введите имя пользователя: "):
        level = input("Введите уровени доступа от 1 до 7 ")
        user_id = input("Введите id пользователя: ")
        if user_id not in unique_id:
            unique_id.add(user_id)
            data[level].update({user_id: name})
            with open(path, 'w', encoding='UTF-8') as f_write:
                json.dump(data, f_write, indent=4, ensure_ascii=False)
        else:
            print("Такой user ID уже существует")



if __name__ == '__main__':
    input_user(Path("users.json"))