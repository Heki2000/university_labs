first_room=input("Введите название первой аудитории: ")
second_room=input("Введите название второй аудитории: ")
print(f"До манипуляций:\nПервая аудитория: {first_room}\nВторая аудитория: {second_room}")
swap=first_room
first_room=second_room
second_room=swap
print(f"После манипуляций:\nПервая аудитория: {first_room}\nВторая аудитория: {second_room}")