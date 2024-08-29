# 1) -----   ПРИМЕР   ----------------------------------------------------------------------------------------------------------------


def find_averange(*, numbers: list):
    return sum(numbers) / len(numbers)


try:
    my_value = find_averange(numbers=[])  # -> ZeroDivisionError

except:
    my_value = 111

my_value  # -> 111
