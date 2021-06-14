def count_number(number):
    cnt = 0
    while number > 0:
        number = number // 10
        cnt += 1
    return cnt
print('Введите числа:')
num1 = int(input())
num2 = int(input())
num1 = count_number(num1)
num2 = count_number(num2)
print(num1*num2)