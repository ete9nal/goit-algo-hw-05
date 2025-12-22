def get_numbers(x):
    numbers = []
    for i in range(x):
        num = i ** 2
        if not num % 2:
            numbers.append(num)
    print(numbers)


def get_numbers_short(x):
    numbers = {f'{i}^2': i ** 2 for i in range(x) if not i % 2}
    print(numbers, type(numbers))


get_numbers(20)
get_numbers_short(20)