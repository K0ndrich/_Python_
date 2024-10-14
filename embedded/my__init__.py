# Если в папке присуцвует файл __init__py то ета папка являеться пакетом,
# который можна импортировать в другие файлы в виде
# одной функции из пакета или целого пакета со всеми функциями в нем


import my_package
from package import *
from package.my_name import my_function
