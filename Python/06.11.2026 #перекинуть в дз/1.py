"""Задание 1
В списке целых, заполненном случайными числами
вычислить:
■ Сумму отрицательных чисел;
■ Сумму четных чисел;
■ Сумму нечетных чисел;
■ Произведение элементов с индексами кратными 3;
■ Произведение элементов между минимальным и
максимальным элементом;
■ Сумму элементов, находящихся между первым и последним положительными элементами."""

import random


rand_list = [random.randint(-100, 100) for _ in range(10)]

print(f"случайно сгенерированный список: {rand_list}")

# сумма отрицательных
count = 0
for i in rand_list:
    if i < 0:
        count += i
print(f"сумма отрицательных чисел: {count}")

# сумма четных
count = 0
for i in rand_list:
    if i % 2 == 0:
        count += i
print(f"сумма четных чисел: {count} ")

# сумма нечетных
count = 0
for i in rand_list:
    if i % 2 != 0:
        count += i
print(f"сумма нечетных чисел: {count} ")

# произв элементов с индексами кратными 3

idx3 = 1
for i in rand_list[::3]:
    idx3 *= i
print(f"произведение элементов с индексами кратными 3: {idx3}")


# произведение элементов между минимальным и максимальным элементом

minimum = min(rand_list)
maximum = max(rand_list)

print(f"произведение элементов между минимальным и максимальным элементом: {minimum * maximum}")

# сумма элементов находящихся между первым и последним положительными элементами

first_idx = -1
for i in range(len(rand_list)):
    if rand_list[i] > 0:
        first_pos_idx = i
        break
last_idx = -1
for i in reversed(range(len(rand_list))):
    if rand_list[i] > 0:
        last_pos_idx = i
        break

print(f"сумма между первым и последним положительным элементом: {first_idx + last_idx}")