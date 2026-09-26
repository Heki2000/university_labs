n=int(input("Введите n: "))
cnt=1
suma=0
count_poz=0
maxi=0
for _ in range(n):
    number = int(input(f'Введите число [{cnt}/{n}]: '))
    suma+=number
    if number>0:
        count_poz+=1
    if cnt==1:
        maxi=number
    else:
        if number>maxi:
            maxi=number
    cnt+=1
print(f"Сумма: {suma} | Положительных: {count_poz} | Максимум: {maxi}")