n = int(input('Введите число: '))

for i in range(1, n+1):
    res = 2 ** i
    if res > n:
        break
    print(res)