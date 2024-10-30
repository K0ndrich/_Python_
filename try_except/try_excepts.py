# Обработчик Исключений (Ошибок)


# try ожидает ошибку в своем блоке кода
try:
    print("try")


# except при словленном try ошибке будет выполнять код внутри себя
# обрабатывает все ошибки
except Exception:
    pass


# обрабатываеть только указанные несколько типов ошибки
except (ValueError, NameError):
    pass


# обрабатывает все ошибки
# второй(текущий) exсept выполянеться если возникла ошибка в первом except
# try -> except Exception -> except(current)
except:
    pass


# else выполняеться, если полностью выполнился try без ошибок
# try -> else
else:
    pass


# finally выполняеться в любом случае в конце выполнение верхних блоков кода
# try -> finally
# try -> else -> finally 
finally:
    pass


# можно также указывать только один тип ошибки, который будем обрабатывать
# as my_name позволяет обращаться к ошибке внутри кода
# except ZeroDivisionError as error:
#     pass
