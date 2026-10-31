n = int(input("Введите число: "))

lenght = len(str(abs(n)))
total = sum(int(x) for x in str(abs(n)))
zeros = str(abs(n)).count("0")
average = total / lenght

while True:
    print("1. Количество цифр")
    print("2. Сумма цифр")
    print("3. Среднее арифметическое")
    print("4. Количество нулей")
    print("5. Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print(lenght)
    elif choice == "2":
        print(total)
    elif choice == "3":
        print(average)
    elif choice == "4":
        print(zeros)
    elif choice == "5":
        break
    else:
        print("Неверный пункт")