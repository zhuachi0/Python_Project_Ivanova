# Дана строка. Подсчитать количество содержащихся в ней цифр.

stroka = input('Введите строку: ')

count = 0
for i in stroka:
    if i.isdigit():
        count += 1

print(count)        