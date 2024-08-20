# Методы Словарей


my_dict = {"my_key1": "my_value1", "my_key2": "my_value2"}

# бем значение из словаря по ключу, при ненахождении ключа не выдает ошибку
my_dict.get("my_key1")  # -> my_value1
my_dict.get("abc")  # -> None
