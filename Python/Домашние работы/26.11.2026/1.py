import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

print("Первый список:", list1)
print("Второй список:", list2)

comb = list1 + list2
print("Элементы обоих списков:", comb)

no_dup = list(set(list1 + list2))
print("Без повторений:", no_dup)

common = list(set(list1) & set(list2))
print("Общие элементы:", common)

unique = list(set(list1) ^ set(list2))
print("Уникальные элементы каждого списка:", unique)

min_max = [min(list1), max(list1), min(list2), max(list2)]
print("Мин и макс значения:", min_max)
