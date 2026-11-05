# Вывести первые N (N>=3) чисел Фибоначчи и посчитать количество четных чисел.

n = int(input('Введите число (>= 3): '))

chet = 0
num1 = 0
num2 = 1
i = 1

while i <= n:
    print(num1, end=' ')
    if num1 % 2 == 0:
        chet += 1
    num1, num2 = num2, num1 + num2
    
    i += 1

print()
print(f'Количество четных чисел: {chet}')

