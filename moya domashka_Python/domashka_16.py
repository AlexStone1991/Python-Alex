# - Уровни знаний:

# - Начальный уровень: 1, 2, 3
# - Средний уровень: 4, 5, 6
# - Достаточный уровень: 7, 8, 9
# - Высокий уровень: 10, 11, 12

level_min = 1, 2, 3
level_low = 4, 5, 6
level_midle = 7, 8, 9
level_max = 10, 11, 12

a = "Начальный"
b = "Средний"
c = "Достаточный"
d = "Высокий"

name_stydent = input("Введите имя студента: ")
level_student = input("Введите уровень знаний студента от 1 до 12: ")

if level_student.isdigit():
    level_stud = int(level_student)
    if level_stud in level_min:
        print(f"{name_stydent}, твой уровень знаний {a}")
    elif level_stud in level_low:
        print(f"{name_stydent}, твой уровень знаний {b}")
    elif level_stud in level_midle:
        print(f"{name_stydent}, твой уровень знаний {c}")
    elif level_stud in level_max:
        print(f"{name_stydent}, твой уровень знаний {d}")
    else:
        print("Введена не коректная оценка, пожалуйста введите от 1 до 12")
