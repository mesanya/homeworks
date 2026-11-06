"""Задание 1
Пользователь вводит с клавиатуры два числа.
Нужно посчитать отдельно сумму четных, нечетных и чисел, кратных 9 в указанном диапазоне, а
также среднеарифметическое каждой группы."""

a = int(input("введите начало диапазона: "))
b = int(input("введите конец диапазона: "))


count = 0
lenght = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        count += i
        lenght += 1

print(f"сумма четных: {count}, среднее арифметическое: {count / lenght}")


count = 0
lenght = 0
for i in range(a, b + 1):
     if i % 2 != 0:
        count += i
        lenght += 1

print(f"сумма нечетных: {count}, среднее арифметическое: {count / lenght}")


count = 0
lenght = 0
for i in range(a, b + 1):
    if i % 9 == 0:
        count += i
        lenght += 1

print(f"сумма кратных 9: {count}, среднее арифметическое: {count / lenght}")