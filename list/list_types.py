# Типы Списков

# создание списков
my_list = ["apple", "bananas", "cherry"]  # -> ['apple', 'bananas', 'cherry']
my_list = ["yes", "3.5", "True", [1, 2, 3]]  # -> ["yes", "3.5", "True", [1, 2, 3]]
my_list = list("abcdf")  # -> ['a', 'b', 'c', 'd', 'f']

# создаем список с помощью переменных
a = "apple"
b = "bananas"
c = "cherry"
my_list = [a, b, c]  # -> ['apple', 'bananas', 'cherry']

# len(my_list) возвращает длину списка
len(my_list)  # -> 5

# сравнение списков ,
my_list1 = [1, 2, 3]
my_list2 = [3, 2, 1]
my_list1 == my_list2  # сравниваеться и значение и разположение -> False
my_list1 > my_list2  # сравниваються только значнеия -> False
my_list1 < my_list2  # -> True

bool([])  # -> False
bool([1])  # -> True

# узнаем есть ли указаные значение в списке
my_list = ["a", "b", "c"]
"a" in my_list  # -> True
my_list = [1, 3, 3]
3 in my_list  # -> True


my_list1 = [1, 2, 3]
my_list2 = [3, 4, 5, 6]
my_list1 + my_list2  # -> [1, 2, 3, 3, 4, 5, 6]
