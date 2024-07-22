def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {num}")
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        summ, incorrect_data = personal_sum(numbers)
        return summ/(len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать


# Некорректный тип данных для подсчёта суммы - 1
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 2
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 3
# Результат 1: 0
# Некорректный тип данных для подсчёта суммы - Строка
# Некорректный тип данных для подсчёта суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5
