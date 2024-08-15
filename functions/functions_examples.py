# Примеры Использования Функций

# 1) Пример
my_numbers1 = [3, 7, 4, 1, 7, 8, 2]
my_numbers2 = [4, 5, 7, 8, 6, 9, 2]


def find_averange(numbers):

    averange = sum(numbers) / len(numbers)

    return int(averange)


averange1 = find_averange(my_numbers1)
averange2 = find_averange(my_numbers2)


# 2) Пример
def count_symbols(string: str):

    symbols = string
    count = 0
    for char in symbols:
        if char == "a":
            count += 1

    return count


# 3) Пример
def custom_greeting(*, name: str, greeting: str = "Hello") -> str:

    return f"{greeting} -> {name}"


a = custom_greeting(name="Max")  # -> Hello -> Max
