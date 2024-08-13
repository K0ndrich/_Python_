# Цыкл For
# Итерация - один проход цикла


my_symbols = ["a", "b", "c", "b", "b", "g"]
my_count = 0

# for елемент in последовательность: цикл будет выполняться пока елементы в последовательности не закончаться
for symbol in my_symbols:
    if symbol == "b":
        my_count += 1


# вложенные цыкли
my_students = ["Max", "Oleg", "Sana", "Slavik"]
for student in my_students:
    for symbol in student:
        print(symbol)
