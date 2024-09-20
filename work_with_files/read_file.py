# Работа с Файлами

import json

# открытие файла только для чтения
my_file = open("work_with_files/files/my_data.json", "r")

# превращение json данных в простой словарь
loaded_data = json.load(my_file)

# закрытие файла после работы
my_file.close()

loaded_data  # -> {'name': 'Mike', 'age': 30, 'city': 'New York'}
