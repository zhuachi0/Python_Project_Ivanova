# Ввести число. Если оно чётное,
# разделить его на 4, если нечётное — умножить на 5.

n = input('Введите число: ')

while type(n) != float:
    try:
        n = float(n)
    except ValueError:
        print('Нужно ввести число')
        n = input('Введите число: ')

if (n % 2) == 0:
    chet = (n // 4)
    print(f'Число четное. Результат действия: {chet}')
else:
    nechet = (n * 5)
    print(f'Число нечетное. Результат действия: {nechet}')