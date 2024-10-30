# Менеджер Контеста With
# With хранит внутри себя все работы с указаным файлом
# With берет на себя также закрытие файла, не нужно приписывать my_file.close(), он зделает ето сам (более безопасно)

import json

with open("work_with_files/files/my_data.json", "r") as my_file:

    my_data = json.load(my_file)

    my_data  # -> {'name': 'Mike', 'age': 30, 'city': 'New York'}


# -----   Реализация Класса с Которым можна работать в Менеджере Контекста   -------------------------------------------------------------------------------------------------------------------


class Connection:

    # метод __enter__ реализовывает вход в контекст
    # открытые файла, подключеные к базе данных
    def __enter__(self):
        print("ENTER")
        self.connection = 1

    # метод __exit__ выполняеться при закрытии контекста или при вознекновения икслючения(exception)
    # exc_type хранит тип ошибки, исключения
    # exc_val хранит значение ошибки, исключения
    # exc_tb хранит действия по обработке ошибки, исключения
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("EXIT")
        self.connection = 0


# создаем екземпляр класса Connection и заходим внутрь его
with Connection() as my_object:
    print("SOME")

    raise Exception("VAL")
