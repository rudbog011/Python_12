def count_days(number):
    if number in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif number in [4, 6, 9, 11]:
        return 30
    elif number == 2:
        return 28
    else:
        return 0
print('Введите номер месяца:')
number = int(input())
print(count_days(number))

