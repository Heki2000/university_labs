total = int(input("Введите количество билетов: "))
capacity = int(input("Введите количество билетом в одной пачке: "))
print(f"Полных пачек билетов: {total//capacity}\nОстаток: {total%capacity}\nПачек: {(total+capacity-1)//capacity}")
