# -----   Разница между Except и Except Exception   ----------------------------------------------------------------------------------------------------------------

try:
    # raise ValueError  # -> Simple Exception
    raise GeneratorExit  # -> Base Exception


# ловит указаный тип ошибки Exception
# Exception приоритет имеет ниже чем BaseException
except Exception:
    print("Simple Exception")

# ловит по-умолчания тип ошибки BaseException
except:
    print("Base Exception")


# -----   Переподнимаем Исключение или reraise Exception   ----------------------------------------------------------------------------------------------------------------

try:  # -> INNER
    try:
        raise ValueError(1)
    except Exception:
        print("INNER")

except Exception:
    print("OUTHER")


try:  # -> INNER , OUTHER
    try:
        raise ValueError(1)
    except Exception:
        print("INNER")
        raise

except Exception:
    print("OUTHER")


# 1) -----   ПРИМЕР   ----------------------------------------------------------------------------------------------------------------


def find_averange(*, numbers: list):
    return sum(numbers) / len(numbers)


try:
    my_value = find_averange(numbers=[])  # -> ZeroDivisionError

except:
    my_value = 111

my_value  # -> 111
