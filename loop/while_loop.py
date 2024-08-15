# Цикл While


# while 10 > i:
#     i+=1


# i ето итератор, по которому будем определяеть количество итераций цикла
my_value = 10
i = 0
sum = 0
while my_value > i:
    sum += i  # -> 45
    i += 1


# другой пример
my_value = 10
i = 0
sum = 0
while i < my_value and i <= 50:
    sum += i  # -> 45
    i += 1
