# Менеджер Контеста With
# With хранит внутри себя все работы с указаным файлом
# With берет на себя также закрытие файла, не нужно приписывать my_file.close(), он зделает ето сам (более безопасно)

import json

with open("work_with_files/files/my_data.json", "r") as my_file:

    my_data = json.load(my_file)

    my_data  # -> {'name': 'Mike', 'age': 30, 'city': 'New York'}
