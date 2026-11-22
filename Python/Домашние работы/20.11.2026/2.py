try:
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
    print(a / b)
except ValueError:
    print("Нужно ввести два целых числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")
