try:
    number = int(input("Введите целое число: "))
    print(number ** 2)
except ValueError:
    print("Введите целое число")
