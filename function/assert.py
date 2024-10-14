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
def password_strength_1(value: str) -> str:

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
    # функция all() возвращаеть если все елементы последовательности True, в любом другом случае возвращаеться False
    # for e in value -> e in digits идет выполнение кода
    if (
        all(symbol in digits for symbol in value)
        or all(symbol in lowers for symbol in value)
        or all(symbol in uppers for symbol in value)
    ):
        return "Weak"

    # ПРВОЕРКА "Very Good"
    # функция any() возвращает True если хотяб один елемент True, в остальных сучаяш возвращает False
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


# ДРУГАЯ РЕАЛИЗАЦИЯ ФУНКЦИИ ПРОВЕРКАИ ПАРОЛЯ
def password_strength_2(value: str) -> str:
    # ПРОВЕРКА "Too Weak"
    if len(value) < 8:
        return "Too Weak"
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    # count хранит счетчик силы пароля
    count = 0

    for my_symbols in (digits, lowers, uppers):
        if any(symbol in my_symbols for symbol in value):
            # повишаем счетчик силы пароля
            count += 1
            # используем continue чтоб не повишать count на каждый символ
            continue

    if count == 3:
        return "Very Good"
    
    return "Weak" if count == 1 else "Good"


if __name__ == "__main__":

    assert password_strength_1("") == "Too Weak"
    assert password_strength_1("1234567") == "Too Weak"
    assert password_strength_1("gazwsxe") == "Too Weak"
    assert password_strength_1("QAZWSXE") == "Too Weak"
    assert password_strength_1("QAaal") == "Too Weak"
    assert password_strength_1("12345678") == "Weak"
    assert password_strength_1("123456788990") == "Weak"
    assert password_strength_1("aqzwsxed") == "Weak"
    assert password_strength_1("aqzwsxedwed") == "Weak"
    assert password_strength_1("QAZWSXEDRFT") == "Weak"
    assert password_strength_1("QAZWSXED") == "Weak"
    assert password_strength_1("1234gazw") == "Good"
    assert password_strength_1("1234gazwws") == "Good"
    assert password_strength_1("1234QAZW") == "Good"
    assert password_strength_1("1234QAZWQW") == "Good"
    assert password_strength_1("aszxQAZW") == "Good"
    assert password_strength_1("aszxasQAZW") == "Good"
    assert password_strength_1("123qazQAZ") == "Very Good"
    assert password_strength_1("12334556Zz") == "Very Good"
    assert password_strength_1("gazwsxedZ1") == "Very Good"
    assert password_strength_1("QAZWSXEDCZ1a") == "Very Good"
