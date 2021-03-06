# Основы Python
# **********************************************************************************************************************
# Найдите в Интернете и прочитайте руководство по написанию кода PEP8 !!!
# **********************************************************************************************************************
# Комментарии
'''Это также комментарий
только на две строки'''
# **********************************************************************************************************************
# Отступы
# Отступы (пробелы (более предпочтительны) или табуляция) в начале логический строки используются для группировки
# конструкций.
# Строки, строки выполняющиеся вместе (блок), должны иметь одинаковый отступ.
# Не смешивайте пробелы и табуляцию. Либо 4 пробела либо 1 табуляция!
for i in range(0, 10):  # правильно
    print(i)
    i += 1
    print(i)
print('***')
# for i in range(0,10): # неправильно
#     print(i)
#         i+=1
# print(i)
# **********************************************************************************************************************
# Объявление переменной
# Объявление типа переменной не требуется!
# К основным встроенным типам относятся:
# 1. None (неопределенное значение переменной)
# 2. Логические переменные (True и False)
# 3. Числа (int - целое число, float - число с плавающей точкой, complex - комплексное число)
# 4. Списки (list - список, tuple - кортеж, range - диапазон)
# 5. Строки (str)
# 6. Бинарные списки
# 7. Множества (set - множество и frozenset - неизменяемое множество)
# 8. Словари (dict)

# К неизменяемым типам относятся: целые числа и числа с плавающей точкой, комплексные числа, логические переменные,
# кортежи, строки, неизменяемые множества
# К изменяемым типам относятся: списки, множества, словари

x = 5
y = 2

# Как узнать тип переменной
print(type(x))  # <class 'int'>
print('***')
# **********************************************************************************************************************
# Вывод результата
print('значения  x и y = ', x, y)  # значения  x и y =  5 2
print('***')
# **********************************************************************************************************************
# Ввод данных с клавиатуры
# z = int(input('Введите число '))
# **********************************************************************************************************************
# Арифметические операции и немного математики
print('сложение', x + y)  # 7
print('умножение', x * y)  # 10
print('вычитание', x - y)  # 3
print('деление', x / y)  # 2.5
print('возведение в степень', x ** y)  # 25
print('остаток от деления', x % y)  # 1
print('целочисленное деление', x // y)  # 2
print('частное и остаток от деления', divmod(x, y))  # (2,1)
print('округление', round(5.556, 2))  # 5.56
print('число по модулю', abs(-5.5))  # 5.5
print('***')
# **********************************************************************************************************************
# Логические операции
print('проверка на равенство', x == y)  # False
print('проверка на неравенство', x != y)  # True
print('больше', x > y)  # True
print('больше или равно', x >= y)  # True
print('меньше или равно', x <= y)  # False
print('меньше', x < y)  # False
print('***')
# Еще логические операции
print('выражение 1', not True)  # False
print('выражение 2', not False)  # True
print('выражение 3', True and True)  # True
print('выражение 4', True and False)  # False
print('выражение 5', False and True)  # False
print('выражение 6', False and False)  # False
print('выражение 7', True or True)  # True
print('выражение 8', True or False)  # True
print('выражение 9', False or True)  # True
print('выражение 10', False or False)  # False
print('***')
# **********************************************************************************************************************
