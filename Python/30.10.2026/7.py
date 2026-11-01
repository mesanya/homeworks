import random

level = int(input("Выберите уровень (1-3): "))

if level == 1:
    n = 5
elif level == 2:
    n = 10
else:
    n = 15

score = 0

for i in range(n):
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    ans = int(input(f"{a} * {b} = "))

    if ans == a * b:
        score += 1

print("Правильных ответов:", score)
print("Оценка:", round(score / n * 5, 1))