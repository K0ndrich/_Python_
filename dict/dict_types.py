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


# итерация происходит по ключу в словаре
for my_key in my_dict:
    my_key  # -> name , age , city , new


# берем названия ключей и их значения по другому
for my_pair in my_dict.items():

    # разпаковуем полученый набор кортежей
    my_key, my_value = my_pair

    type(my_pair)  # -> <class 'tuple'>
    my_pair  # -> ('name', 'Max') , ('age', 666) , ('city', 'New York') , ('new', 'new')

    my_key  # -> name , age , city , new
    my_value  # -> Max , 666 , New York , new


# берем названия ключей и их значения по другому
for my_key, my_value in my_dict.items():
    my_key  # -> name , age , city , new
    my_value  # -> Max , 666 , New York , new
