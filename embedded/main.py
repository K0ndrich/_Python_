# функция main являеться точкой входа в програму , внутри ее именно
# начинанеться выполнение кода нашей программы
def main():
    print("Hello World")


# if __name__ == "__main__" спользуеться для того, чтоб определить
# выполняеться етот файл как основной срипт или он был импортирован в другой файл в качестве модуля
if __name__ == "__main__":
    main()


# переменная __name__ хранит название текущего файла
# если ми запускаем файл не как основной,
# тогда место __main__ будет возвращаться название myFile.py етого НЕ основного файла, который тоже запустился
__name__  # -> __main__
