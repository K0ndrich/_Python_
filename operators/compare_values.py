# сравнения чисел
x = 10
y = 9

# bool -> 1 , -1 , 3.2 , True , "Text" , [1,2] , {"key": "yes"}       -> True (правдивое значение)
# bool -> 0 , 0.0 , False , "" , [] , {} , None , set() , range(0,0)  -> False (ложное значение)
# функция конвертирует указаное значение в логическое
bool()

# == равно
x == y
# != не равно
x != y
# > больше
x > y
# < больше
x < y
# >= больше или равно
x >= y
# <= меньше или равно
x <= y


# NOT
not True  # -> False
not False  # -> True
not 3  # -> False
not -1  # -> False
not 0  # -> True


# AND
True and True  # -> True
False and True  # -> False
False and False  # -> False
5 > 3 and 1 < 2  # -> True
3 > 5 and 1 < 2  # -> False


# OR
True or True  # -> True
True or False  # -> True
False or False  # -> False
