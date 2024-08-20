# Методы Словарей


my_dict = {"my_key1": "my_value1", "my_key2": "my_value2"}

# бем значение из словаря по ключу, при ненахождении ключа не выдает ошибку
my_dict.get("my_key1")  # -> my_value1
my_dict.get("abc")  # -> None
my_dict.get("abc", "default_value")  # -> default_value

# возвращает только названия ключей в словаре
my_dict.keys()  # -> dict_keys(['my_key1', 'my_key2'])

# возвращает только значение ключей в словаре
my_dict.values()  # -> dict_values(['my_value1', 'my_value2'])

# возвращает все елементы словаря парами кортежей ключ-значение
my_dict.items()  # -> dict_items([('my_key1', 'my_value1'), ('my_key2', 'my_value2')])
print(my_dict.items())
