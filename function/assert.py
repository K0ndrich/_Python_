# Простое тестирование с инструкцией ASSERT


def my_fn(number):
    # если условие assert возвращает False, тогда функция возвращает ошибку с указаным текстом
    assert number > 5, "Too Small Number"
    assert number % 2 == 0, "Must be Even Number"
    assert isinstance(number, int), "Must be Integer Number"


# my_fn(4)  # -> AssertionError: Too Small Number


# -----   Функция Проверяет Надежность Пароля   -------------------------------------------------------------------------------------------------------------------

import string


# функция проверяет надежность пароля
def password_strength(value: str) -> str:
    
    # digits храни все возможные цифры
    digits = string.digits
    # lowers хранит все буквы нижнего регистра
    lowers = string.ascii_lowercase
    # uppers хранит все букты верхнего регистра
    uppers = lowers.upper()

    # ПРОВЕРКА "Too Weak"
    if len(value) < 8:
        return "Too Weak"


    # ПРОВЕКА "Weak"
    # функция all() возвращаеть елси все елементы последовательности True, в любом другом случае возвращаеться False
    # for e in value -> e in digits идет выполнение кода
    if (
        all(symbol in digits for symbol in value)
        or all(symbol in lowers for symbol in value)
        or all(symbol in uppers for symbol in value)
    ):
        return "Weak"

    # ПРВОЕРКА "Very Good"
    # фнукция any() возвращает True если хотяб один елемент True, в остальных сучаяш возвращает False
    if (
        any(symbol in digits for symbol in value)
        and any(symbol in lowers for symbol in value)
        and any(symbol in uppers for symbol in value)
    ):
        return "Very Good"

    # ПРОВЕРКА "Good"
    if (
        (
            any(symbol in digits for symbol in value)
            and any(symbol in lowers for symbol in value)
        )
        or (
            any(symbol in digits for symbol in value)
            and any(symbol in uppers for symbol in value)
        )
        or (
            any(symbol in lowers for symbol in value)
            and any(symbol in uppers for symbol in value)
        )
    ):
        return "Good"
    # возвращаем False
    return ""


if __name__ == "__main__":

    assert password_strength("") == "Too Weak"
    assert password_strength("1234567") == "Too Weak"
    assert password_strength("gazwsxe") == "Too Weak"
    assert password_strength("QAZWSXE") == "Too Weak"
    assert password_strength("QAaal") == "Too Weak"
    assert password_strength("12345678") == "Weak"
    assert password_strength("123456788990") == "Weak"
    assert password_strength("aqzwsxed") == "Weak"
    assert password_strength("aqzwsxedwed") == "Weak"
    assert password_strength("QAZWSXEDRFT") == "Weak"
    assert password_strength("QAZWSXED") == "Weak"
    assert password_strength("1234gazw") == "Good"
    assert password_strength("1234gazwws") == "Good"
    assert password_strength("1234QAZW") == "Good"
    assert password_strength("1234QAZWQW") == "Good"
    assert password_strength("aszxQAZW") == "Good"
    assert password_strength("aszxasQAZW") == "Good"
    assert password_strength("123qazQAZ") == "Very Good"
    assert password_strength("12334556Zz") == "Very Good"
    assert password_strength("gazwsxedZ1") == "Very Good"
    assert password_strength("QAZWSXEDCZ1a") == "Very Good"
