kol = int(input('Введите количество чисел: '))
summa = 0

for i in range(1, kol+1):
    i = int(input('Введите число: '))
    if i == 0:
        summa += 1
print(f'Количество чисел: {kol} \nИз них нулей: {summa}')