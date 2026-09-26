number = int(input("Type number: ")) # 9 var
need_more=list(range(0,15))
normaly=list(range(15,60))
huge=list(range(60,101))
if number in need_more:
    print("Пополнить")
elif number in normaly:
    print("Достаточно")
elif number in huge:
    print("Большой запас")
else:
    print("Ошибка диапазона")
