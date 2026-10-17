# Даны три целых числа A, B, C. Проверить истинность высказывания:
# "Хотя бы одно из чисел A, B, C положительно"

A = input('Введите первое число: ')
B = input('Введите второе число: ')
C = input('Введите третье число: ')

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Нужно ввести целое число')
        A = input('Введите второе число: ')

while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print('Нужно ввести целое число')
        B = input('Введите второе число: ')

while type(C) != int:
    try:
        C = int(C)
    except ValueError:
        print('Нужно ввести целое число')
        C = input('Введите второе число: ')

if A > 0 or B > 0 or C > 0:
    print('Высказывание истинно')
else:
    print('Высказывание ложно')


