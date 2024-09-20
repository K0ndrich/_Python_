# Работа с Файлами

import json

data = {"name": "Mike", "age": 30, "city": "New York"}

# открываем указаный файла в папке files для дальнейшей работы
# "w" указывает для чего открываем файл, w - для записи
my_file = open("work_with_files/files/my_data.json", "w")


# записывает указанные данные в указаный файл
# indent указывает отступы в нашем файле
json.dump(data, my_file, indent=4)

# остановка выполнения файла после его работы
my_file.close()
