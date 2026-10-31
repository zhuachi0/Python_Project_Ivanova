a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
count = 0

for i in range(b, a - 1, -1):
    print(i, end=' ')
    count += 1
print()
print(f'Количество чисел: {count}')