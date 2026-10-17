numbers = [int(number) for number in input('Введите числа через пробел: ').split()]
result=[]
for number in numbers:
    if number!=0:
        result.append(number)
print(f'Список чисел, удовлетворяющих условию (ненулевые числа): {result}\n'
      f'Количество: {len(result)} | Сумма: {sum(result)} | Отсортированная копия: {sorted(result)}')
