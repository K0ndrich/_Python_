# Область видимости наший импортов import


# показываем какие обьекты лежат в области видимости нашего файла
# подключенные модули тоже показывает
globals().keys()  # -> dict_keys([ 'my_module', '__name__', '__doc__', '__package__', '__loader__' ])

import random

# dir(my_module) возвращает методы которыми можна пользоваться из указаного модуля
dir(
    random
)  # -> [ _index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random' ]

