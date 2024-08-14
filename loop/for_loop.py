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
        # print(symbol)
        pass


# continue пропуская одну итерацию цикла
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in my_numbers:
    if number % 2 == 0:  # -> True если число четное
        continue
    # print(number)
    pass


# break полностью выходит из цикла
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in my_numbers:
    if number == 7:  # -> True если число четное
        break
    # print(number)
    pass


# изменяем значение елемнетов списка по их индексу
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(len(my_numbers)):  # index -> [0, 1, 2, 3, 4, 5, 6, 7, 8]
    my_numbers[index] *= 2

my_numbers  # -> [2, 4, 6, 8, 10, 12, 14, 16, 18]


# подсчитываем количество и индексы указаного значения в строке
my_string = "Hello - world"
indexes = []
count = 0
for i in range(len(my_string)):
    if my_string[i] == "o":
        count += 1
        indexes.append(i)

print(count)
print(indexes)
