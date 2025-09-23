# Вариант импорта №1
# import lesson_15

# Вариант импорта №2
# from lesson_15 import *

# Вариант импорта №3
# from lesson_15 import all_param_func

# Вариант 3.1 - псевдоним
from My_lesson.lesson_15 import all_param_func as apf

# вызов функции по варианту №1
# lesson_15.all_param_func(1, 2, 3, 4, five=5)

# Вызов функции по варианту №2
# all_param_func(1, 2, 3, 4, five=5)

# Вызов функции по варианту №3.1
apf(1, 2, 3, 4, five=5)

# Ипорт модуля из пакета
from marvel import full_dict
print(full_dict)
