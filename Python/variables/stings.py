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


# -----   Методы Строк   -------------------------------------------------------------------------------------------------------------------------------
my_string = "text"

# .upper() метод возвращает значение строки в верхнем регистре
my_string.upper()

# .lower() метод возвращает значение строки в нижнем регистре
my_string.lower()

# .strip() убирате пробели до и после текста, тем самым уменьшает длину строки
my_string = "    text    ---  "
my_string.strip()

# .replace("old_text" , "new_text") изменяет указаную часть текста на новую
my_string = "hello world"
my_string.replace("world", "max")

# .count() возвращет количество указаных символом в строке
my_string = "text text text"
my_string.count("t")
