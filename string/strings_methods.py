# Методы Строк


my_string = "text"

# .upper() метод возвращает значение строки в верхнем регистре
my_string.upper()  # -> "TEXT"

# .lower() метод возвращает значение строки в нижнем регистре
my_string.lower()  # -> "text"

# .strip() убирате пробели до и после текста, тем самым уменьшает длину строки
my_string = "    text    "
my_string.strip()  # -> "text"


# .replace("old_text" , "new_text") изменяет указаную часть текста на новую
my_string = "hello world"
my_string.replace("world", "max")  # -> "hello max"

# .count() возвращет количество указаных символом в строке
my_string = "text text text"
my_string.count("t")  # -> 6

# .isdigit() возвращает True если строка состоит полность из цифр (нету букв)
my_string = "123"
my_string.isdigit()  # -> True

# .isalpha() возвращает True если строка состоит полностью из букв (нету цифр)
my_string = "abc"
my_string.isalpha()  # -> True

# .format подставляет указаные значение в строку в указаной полседовательности
my_string = "{0},{1},{2}".format("a", "b", "c")  # -> a, b, c
my_string = "{0},{1},{0}".format("a", "b", "c")  # -> a, b, a

# .split("my_symbol") розделяет строку по указаному символу(или пробелу) и возвращает список [] елементов
my_string = "hello - world"
my_string.split()  # -> ['hello', '-', 'world']
my_string.split("-")  # -> ['hello ', ' world']

my_string = "1,2,3,4,5"
my_string.split(",")  # -> ['1', '2', '3', '4', '5']
