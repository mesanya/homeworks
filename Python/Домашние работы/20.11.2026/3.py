days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

try:
    day_number = int(input("Введите номер дня недели (от 1 до 7): "))
    if day_number < 1 or day_number > 7:
        raise IndexError
    print(days[day_number - 1])
except ValueError:
    print("Введите номер дня")
except IndexError:
    print("Нет такого дня")
finally:
    print("Проверка завершена")
