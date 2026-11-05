# Найти и вывести на экран квадраты и кубы чисел от 2 до 5.

kvadr = []
kub = []
i = 1

while i <= 5:
    kvadr.append(i ** 2)
    kub.append(i ** 3)
    
    i += 1

print(f'Квадраты чисел от 2 до 5: {kvadr}\nКубы чисел от 2 до 5: {kub}')