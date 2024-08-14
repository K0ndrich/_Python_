# Примеры использования функций

my_numbers1 = [3, 7, 4, 1, 7, 8, 2]
my_numbers2 = [4, 5, 7, 8, 6, 9, 2]


def find_averange(numbers):
    averange = sum(numbers) / len(numbers)
    return int(averange)


averange1 = find_averange(my_numbers1)
averange2 = find_averange(my_numbers2)
