# Найти и вывести на экран S=1!+2!+3!+4!+...+n! (n>1).

n = int(input('Введите число: '))
factor = 1
s = 0
i = 1

while i <= n:
    factor *= i
    s += factor
    
    i += 1
print(f'Сумма факториалов от 1 до {n}: {s}')