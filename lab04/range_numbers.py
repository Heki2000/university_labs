a,b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)
