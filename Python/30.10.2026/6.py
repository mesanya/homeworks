n = int(input("Введите размер клетки: "))

for i in range(n * 8):
    for j in range(n * 8):
        if (i // n + j // n) % 2 == 0:
            print("*", end="")
        else:
            print("-", end="")
    print()