a1 = 1
d = 3
n = int(input('Введите количество членов прогрессии: '))

for i in range(1, n + 1):
    delen = a1 / 2
    res = round(delen)
    print(res, end=' ')
    a1 += d