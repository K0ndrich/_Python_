# Типы Строк


# простая строка
my_string = str("abc")
my_short_string = "Hello World"


# строка содержит большое количество текста, отступы при етом сохраняютсья
my_long_string = """Text Text Text 
Text Text Text Text Text Text
                    Text Text Text"""


first_name = "Max"
last_name = "Kondrich"
# конкатонация строк, обьединение строк в одну
full_name = first_name + " " + last_name


# len функция возвращает длину строки
lenght_string = len(my_long_string)


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
# укороченая форма записи
f"{name=}"  # -> name='Kondrich'

# .format позволяет вставлять внутрь строки оперделенные указаные значения
my_string = "hello {my_value}".format(my_value="123")  # -> "hello 123"
my_string = "hello {0} {1}".format("max", "kondrich")  # -> "hello max kondrich"
my_string = "hello {:%}".format(123.3)  # -> "hello 12330.000000%"
