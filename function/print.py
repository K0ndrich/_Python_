# Функция PRINT


# по-умолчанию
# print(*values: object , sep: str | None = " " , end: str | None = "\n" , file: SupportsWrite[str] | None = None , flush: Literal[False] = False)


# print(1, 2, 3)  # -> 1 2 3


# sep указывает разделитель мужду указаными значениями внутри указаного текущего одного print
# print(1, 2, 3, sep="-")  # -> 1-2-3


# end указывает нужно ли переводить на новую строку возвращаемое значение слудующего print
# или разделение первой строки от второй
# print(1, 2, 3, end=" - ")
# print(4, 5, 6)  # -> 1 2 3 - 4 5 6


# # создаеться файл test.txt внутрь которого записываеться наше значение из print
# my_file = open("test.txt", "w")
# # file указывает в какой файл будем записывать наше значение из print
# print("kondrich", file=my_file)

