# Создание Своего Исключения (Ошибки)

# Нужен для получения больше информации при появлении нашей исключения(ошибки)


class MyException(Exception):
    def __init__(self, value, message="My Text Message"):
        self.value = value
        self.message = message
        super().__init__(self.message)


raise MyException("text")  # -> MyException: My Text Message
