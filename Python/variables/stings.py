# простая строка
my_string1 = "Hello World"


# строка содержит большое количество текста, отступы при етом сохраняютсья
my_string2 = """Text Text Text 
Text Text Text Text Text Text
                    Text Text Text"""


first_name = "Max"
last_name = "Kondrich"
# конкатонация строк, обьединение строк в одну
full_name = first_name + " " + last_name


# len функция возвращает длину строки
lenght_string = len(my_string1)


my_first_string = "Max Kondrich"
my_last_string = "Max"
# in позволяет проверить являеться ли вторая строка подстрокой для первой, регист емеет значение
"Max" in my_first_string
my_last_string in my_first_string


# f-строки , внутри их можно вставлять переменные
name = "Kondrich"
age = 25
number = 10
f"-- hello {name} -> {age} --"  # -> -- hello Kondrich -> 25 --
f"-- {age*number} --"  # -> -- 250 --


# .format позволяет вставлять внутрь строки оперделенные указаные значения
my_string = "hello {my_value}".format(my_value="123")  # -> "hello 123"
my_string = "hello {0} {1}".format("max", "kondrich")  # -> "hello max kondrich"
my_string = "hello {:%}".format(123.3)  # -> "hello 12330.000000%"


# -----   Методы Строк   -------------------------------------------------------------------------------------------------------------------------------
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
