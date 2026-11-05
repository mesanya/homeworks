"""Задание 2
Есть список целых, заполненный случайными числами.
На основании данных этого массива нужно:
■ Создать список целых, содержащий только четные
числа из первого списка;
■ Создать список целых, содержащий только нечетные
числа из первого списка;
■ Создать список целых, содержащий только отрицательные числа из первого списка;
■ Создать список целых, содержащий только положительные числа из первого списка."""

import random

original_list = [random.randint(-100, 100) for _ in range(15)]
print(f"Исходный список: {original_list}\n")

# четные числа
even_list = [num for num in original_list if num % 2 == 0]

# нечетные числа
odd_list = [num for num in original_list if num % 2 != 0]

# отрицательные числа
negative_list = [num for num in original_list if num < 0]

# положительные числа
positive_list = [num for num in original_list if num > 0]

print(f"только четные числа: {even_list}")
print(f"только нечетные числа: {odd_list}")
print(f"только отрицательные числа: {negative_list}")
print(f"только положительные числа: {positive_list}")
