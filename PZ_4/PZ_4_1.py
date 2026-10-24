a = input('Введите вещественное число: ')
n = input('Введите целое число: ')

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print('Нужно ввести число')
        a = input('Введите вещественное число:')
while type(n) != int:
    try:
        n = int(n)

        if n > 0:
            break
        else:
            print('Число должно быть больше 0')
            n = input()

    except ValueError:
        print('Нужно ввести целое число')
        n = input('Введите целое число: ')

stepen = a ** n

print(stepen)