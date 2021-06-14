print('Введите дату:')
date = input()
def star_date(date):
    d = date.split('.')
    n1 = int(d[0]) * int(d[1])
    n2 = int(d[2]) % 100
    if n1 == n2:
        return 'True'
    else:
        return 'False'
print(star_date(date))
    