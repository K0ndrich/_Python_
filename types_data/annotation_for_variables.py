# Что такое Анотация Типов Данных ?

# Ето способ явно указать ожидаемый тип данных для Переменных

name: str = "Kondrich"
age: int = 25
price: float = 17.3
is_active: bool = True
data: None = None
numbers: list[int] = [1, 2, 3]
my_list: list[float:str] = [1.3, "Hello"]
my_tuple: tuple[int, float] = (10, 15.3)
my_dict: dict[str, str | int] = {"name": "Kondrich", "age": 27}
my_mix_dict: dict[str, list[int]] = {"value1": [1, 2], "value2": [3, 4]}

# Ето способ явно указать ожидаемый тип данных для Аргументов, которые передаться в Функцию

# Ето способ явно указать ожидаемый тип данных для Возращаемых Значения из Функции
