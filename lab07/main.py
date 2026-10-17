from functions import average, sum_digits, normalize_text, select_numbers

number = int(input("Введите целое число для подсчёта суммы цифр: "))
print(f"Сумма цифр равна: {sum_digits(number)}")

numbers = [int(number) for number in input("Введите числа через пробел: ").split()]
print(f'Среднее значение: {average(numbers)}' if (average(numbers)) else "Нет данных")

text = input("Введите текст: ")
print('Нормализованный текст - ', normalize_text(text))

numbers = [int(number) for number in input("Введите чилса через пробел: ").split()]
threshold = int(input("Введите пороговое число: "))
print(f'Результат: {select_numbers(numbers, threshold)}')