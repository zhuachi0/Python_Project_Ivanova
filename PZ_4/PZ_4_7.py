# Ввести N чисел. Найти и вывести их среднее арифметическое.

kol = int(input('Введите количество чисел: '))
summa = 0
i = 1

while i <= kol:
    n = int(input(f'Введите {i}-е число: '))
    summa += n
    
    i += 1

arifm = summa / kol
print(f'Количество чисел: {kol}\nИх среднее арифметическое: {arifm}')