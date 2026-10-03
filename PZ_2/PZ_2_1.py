# Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа

num = input('Введите двузначное число: ')

while type(num) != int:
    try:
        num = int(num)
        if 10 <= num <= 99:
            break
        else:
            print('Число должно быть от 10 до 99')
            num = input('Введите двузначное число: ')

    except ValueError:
        print('Попробуйте еще раз')
        num = input('Введите двузначное число: ')

ed = num%10
des = num//10

res = ed * 10 + des

print(f'Старое число: {num}\nРезультат: {res}')

