first_ob, second_ob = input("Введите первый предмет: "), input('Введите второй предмет: ')
first_cnt, second_cnt = int(input(f"Введите кол-во занятий по предмету '{first_ob}': ")), int(
    input(f"Введите кол-во занятий по предмету '{second_ob}': "))
first_time, second_time = int(input(f"Введите время одного занятия по предмету '{first_ob} в минутах: ")), int(
    input(f"Введите время одного занятия по предмету '{second_ob}' в минутах: "))
all_time = int(input("Введите доступное время на неделю в часах: "))
print(f"Для предмета '{first_ob}':\nОбщее время занятий: {first_time * first_cnt} минут")
print(f"Для предмета '{second_ob}':\nОбщее время занятий: {second_time * second_cnt} минут")
print(f"Общая нагрузка за неделю: {first_time*first_cnt+second_cnt*second_time} минут или {(first_time*first_cnt+second_cnt*second_time)/60:.2f} час(а/ов)"
      f"\nОстаток свободного времени: {all_time-(first_time*first_cnt+second_cnt*second_time)/60:.2f}\nЗа 4 недели общая нагрузка: {(first_time*first_cnt+second_cnt*second_time)/60*4:.2f}")

