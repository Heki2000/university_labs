n=int(input("Введите число n: "))
count_satisfuing = 0
sum_satisfying=0
count=1
for _ in range(n):
    number = int(input(f"Введите число [{count}/{n}]: "))
    count+=1
    if number !=0:
        count_satisfuing+=1
        sum_satisfying+=number
print(f"Количество удовлетворяющих: {count_satisfuing} | Сумма удовлетворяющих: {sum_satisfying}")