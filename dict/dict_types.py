# Типы Словарей

# Ключи словарей всегда Уникальные

# создание словарей
my_dict = {}  # -> { }
my_dict = {"my_key1": "my_value1", "my_key2": 777}
my_dict = {"name": "Max", "age": 5, "city": "New York"}


# измение значения указаного ключа словаря
my_dict["age"] = 666  # -> {'name': 'Max', 'age': 666, 'city': 'New York'}

# добавление ключ + значение к словарю
my_dict["new"] = (
    "new"  # -> {'name': 'Max', 'age': 666, 'city': 'New York', 'new': 'new'}
)


# логическое значение словаря
bool({})  # -> False
bool({"my_key1": 777})  # -> True
