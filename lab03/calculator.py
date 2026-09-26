first_number, second_number, operation = float(input("Type first number: ")), float(input('Type second number: ')), input('Type operation symble: ')
if operation=='/' and second_number == 0:
    print('Деление на ноль запрещено')
elif operation not in "+*/-":
    print("Неизвестная операция")
else:
    print('Result is ')
    if operation=='+':
        print(f'{first_number+second_number:.2f}')
    elif operation=='*':
        print(f'{first_number*second_number:.2f}')
    elif operation=='/':
        print(f'{first_number/second_number:.2f}')
    else:
        print(f'{first_number-second_number:.2f}')