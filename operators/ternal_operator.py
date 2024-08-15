# Тернарный Оператор

# my_value1 if my_value1 > my_value2 else my_value2
3 if 3 > 5 else 5  # -> 5

# использование переменных в тернарном операторе
a = 3
b = 5
a if a > b else b  # -> 5


# использование функций в тернарных операторах
a = "text"
b = "upper"
a.upper() if b == "upper" else a.lower()  # -> TEXT

# конкатнация строк
"a - " + ("четное" if 4 % 2 == 0 else "нечетное")  # -> "a - четное"

# сложенные тернарные операторы
(1 if 2 > 1 else 2) if 3 > 2 else (2 if 3 > 2 else 3)  # -> 1
