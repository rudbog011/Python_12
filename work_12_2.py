def max_number():
    print('Введите список чисел:')
    spisok = input()
    s = spisok.split()
    return(max(s))

max_n1 = max_number()
max_n2 = max_number()

print(int(max_n1)*int(max_n2))


