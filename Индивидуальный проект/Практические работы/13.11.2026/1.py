"""Задание 1. Найти количество чётных чисел в диапазоне от 1 до 100.
Решение: count = 0 → цикл i от 1 до 100: если i % 2 = 0, то count = count+1 →
вывод count"""


count = 0
for i in range(1, 101):
    if i % 2 == 0:
        count = count + 1
print(count)
