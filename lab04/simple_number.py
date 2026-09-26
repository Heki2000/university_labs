number = int(input("Введите число: "))

for i in range(2, int(number**0.5)+1):
    if number%i==0:
        print("Число составное.")
        break
else:
    print("Число простое.")