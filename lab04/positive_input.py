number = int(input("Введите число: "))
cnt=0
while number<=0:
    cnt+=1
    number = int(input("Введите число: "))
print(f'Квадрат: {number**2} | Отклонено: {cnt}')