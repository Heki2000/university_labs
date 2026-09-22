second_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
town = input("Введите город: ")
age = int(input("Введите возраст: "))
fav_obj = input("Введите любимый предмет: ")
hours_in_week = float(input("Введите кол-во часов подготовки в неделю: "))

print(f'\n\tКарточка студента\n1) {first_name} {second_name}\n2) Возраст через четыре года - {age + 4}\n3)'
      f' Время подготовки за 4 недели - {hours_in_week * 4:.2f}\n4) Среднее время подготовки в день - {hours_in_week / 7:.2f}')
