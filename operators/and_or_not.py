# Логические Операторы AND , OR , NOT

# Созданы для обьединение проверки различных условий в коде

# -----   AND (И) оператор   -----------------------------------------------------------------------------------------------------------------------------------

# True + True = True
# True + False = False

# оба значения True поетому возращаеться последнее True значение 2
1 and 2  # -> 2
bool(1 and 2)  # -> True

# одно значение False поетому возвращаеться ето False значение 0
1 and 0  # -> 0
bool(1 and 0)  # -> False


# -----   OR (ИЛИ) оператор   -----------------------------------------------------------------------------------------------------------------------------------

# True + True = True
# True + False = True
# False + False = False

# оба значния True поетому возвращаеться первое True значение 1
1 or 2  # -> 1
bool(1 or 2)  # -> True

# одно значение True поетому возвращаеться ето значение True значение 1
1 or 0  # -> 1
bool(1 or 0)  # -> True

# одно значение True поетому возвращаеться ето значение True значение 1
0 or 1  # -> 1
bool(0 or 1)  # -> True

0 or 0  # -> 0
bool(0 or 0)  # -> False


# -----   NOT (НЕ) оператор   -----------------------------------------------------------------------------------------------------------------------------------

not True  # -> False
not False  # -> True

not 0  # -> True
not 1  # -> False
not -1  # -> False