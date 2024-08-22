# Функции могут возвращать сразу несколько возвращаемых значений


# функция модифицирует словарь
def modify_dict(old_dict: dict, **kwargs):  # -> -> tuple[dict, bool]
    # -> возвращает словарь, возвращает изменился ли словарь

    # словарь еще не изменился
    is_modify = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value

            # изменение словря поизошло
            is_modify = True

    return old_dict, is_modify


my_product = {"id": 2, "name": "Laptop", "price": 1000}


type(modify_dict(my_product, city="New York"))  # -> <class 'tuple'>

modify_dict(
    my_product, city="New York"
)  # -> ({'id': 2, 'name': 'Laptop', 'price': 1000, 'city': 'New York'}, True)
modify_dict(
    my_product, name="Laptop"
)  # -> ({'id': 2, 'name': 'Laptop', 'price': 1000, 'city': 'New York'}, False)


# розпаковываем кортеж, который получили из функции
my_product, was_modify = modify_dict(my_product, age="15")
my_product  # -> {'id': 2, 'name': 'Laptop', 'price': 1000, 'city': 'New York', 'age': '15'}
was_modify  # -> True
