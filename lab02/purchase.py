price = int(input("Введите стоимость одной тетради в рублях: "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите внесённую стоимость в рублях: "))
print(f"Стоимость: {price*count} руб.\nСдача: {paid%(price*count)} руб." if price*count!=0 else f"Стоимость: 0 руб. \nСдача: {paid} руб.")