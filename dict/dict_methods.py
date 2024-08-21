# Методы Словарей

# созданеи словаря
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


my_dict1 = {"name": "Max", "age": 5, "city": "New York"}
my_dict2 = {"job": "software engineer", "married": True, "city": "London"}

# розширение одного словаря свойствами другого, значения свойств могут обновляться значениеми из втрого словаря
my_dict1.update(my_dict2)
my_dict1  # -> {'name': 'Max', 'age': 5, 'city': 'London', 'job': 'software engineer', 'married': True}

# обединение двох словаряей по другому, результат тотже
my_dict1 = my_dict1 | my_dict2
my_dict1  # -> {'name': 'Max', 'age': 5, 'city': 'London', 'job': 'software engineer', 'married': True}
