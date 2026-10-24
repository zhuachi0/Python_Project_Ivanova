# Дано два числа.
# Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

n1 = input('Введите число: ')
n2 = input('Введите число: ')

while type(n1) != float:
    try:
        n1 = float(n1)
    except ValueError:
        print('Нужно ввести число')
        n1 = input('Введите число: ')
while type(n2) != float:
    try:
        n2 = float(n2)
    except ValueError:
        print('Нужно ввести число')
        n2 = input('Введите число: ')

summa = n1 + n2

if summa // 5:
    kr5 = summa + 1
    print(f'Сумма чисел кратна 5. Результат действия: {kr5}')
else:
    nekr5 = summa - 2
    print(f'Сумма чисел не кратна 5. Результат действия: {nekr5}')