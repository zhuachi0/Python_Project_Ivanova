n = int(input('Введите число: '))
factor = 1
s = 0

for i in range(1, n + 1):
    factor = factor * i
    s += factor
print(f'Сумма факториалов от 1 до {n}: {s}')