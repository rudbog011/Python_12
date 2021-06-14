print('Введите количества товара:')
number = int(input())
def cost(number):
    summa = 0
    if number > 0:
        summa = 100 + (number - 1) * 50
    return summa
print(cost(number))