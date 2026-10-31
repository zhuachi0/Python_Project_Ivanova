a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
summa = 0

for i in range(a, b + 1):
    summa += i
print(f'Сумма чисел: {summa}') 
    