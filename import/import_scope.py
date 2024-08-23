# Область видимости наший импортов import


# показываем какие обьекты лежат в области видимости нашего файла
# подключенные модули тоже показывает
globals().keys()  # -> dict_keys([ 'my_module', '__name__', '__doc__', '__package__', '__loader__' ])

import random

my_list = [1, 2, 3]

print(random.choice(my_list))
