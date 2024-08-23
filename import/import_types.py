# Подключение import стороних бибилиотек(модулей) к нашему одному текущему файлу
# Типы Импортов import


# подключаем весь модуль со всем функционалом
import my_module

# подключаем сразу несколько модулей
import my_module1, my_module2

# подключаем модуль и даем ему новое название, нужно обращаться по новому названию
import my_module as new_name_module

# подключаем несколько модулей и сразу даем им новые названия
import my_module1 as new_name_module1, my_module2 as new_name_module2

# подключаем все функции из указнаго модуля
from my_module import *

# подключаем только одну функцию из указаного модуля, все остальные функции недоступные
from my_module1 import my_function

# подключаем одну фнукцию и сразу даем ей новое название, к функции нужно обращаться по новому названию
from my_module import my_fucntion as new_name_function
