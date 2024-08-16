# Области Видимости переменных в функциях


# 1) Пример
# local_var нельзя вызвать вне области функции
def my_function():

    local_var = "1"
    print(local_var)  # -> 1


# my_function()


# 2) Пример
variable = "1"


def my_function():
    # variable значение изменять только внутри функции, вне функции значение остаеться прежним
    variable = "2"
    print(variable)


my_function()  # -> 2
print(variable)  # -> 1
