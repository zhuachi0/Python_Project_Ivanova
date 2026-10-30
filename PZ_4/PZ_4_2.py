n = input('Введите целое число: ')

while type(n) != int:
    try:
        n = int(n)

        if n > 1:
            break
        else:
            print('Число должно быть больше 1')
            n = input('Введите целое число: ')
    
    except ValueError:
        print('Нужно ввести целое число')
        n = input('Введите целое число: ')

k = 0
summa = 0

for i in range(1, n + 1):
    k = i
    summa += i
    if summa >= n:
        break
print(k, summa)