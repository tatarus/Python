# **********************************************************************************************************************
# Списки - структура данных, которая содержит упорядоченный набор элементов. Список это изменяемый тип данных
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Проверка наличия элемента в последовательности
print('a' in list2)  # True
print('***')

# Добавление значений в конец списка
list1.append(4)
print(list1)  # [1, 2, 3, 4]
print('***')

# Добавление элемента по индексу
list1.insert(0, 5)
print(list1)  # [5, 1, 2, 3, 4]
print('***')

# Сортировка списка (возможна конструкция list3 = sorted(list1))
list1.sort()
print(list1)  # [1, 2, 3, 4, 5]
print('***')

# Обратный порядок элементов
list1.reverse()
print(list1)  # [5, 4, 3, 2, 1]
print('***')

# Добавление последовательности в конец
list1.extend(list2)
print(list1)  # [5, 4, 3, 2, 1, 'a', 'b', 'c']
print('***')

# Удаление первого вхождения значения
list1.remove(5)
print(list1)  # [4, 3, 2, 1, 'a', 'b', 'c']
print('***')

# Удаление элемента по индексу
del list1[6]
print(list1)  # [4, 3, 2, 1, 'a', 'b']
print('***')

# Удаление значение по индексу и возвращение его
l1 = list1.pop(0)
print(list1)  # [3, 2, 1, 'a', 'b']
print(l1)  # 4
print('***')

# Определяем количество элементов
print(len(list1))  # 5
print('***')

# Подсчет количества вхождений элемента
print(list1.count('a'))  # 1
print('***')

# Определяем позицию элемента
print(list1.index('a'))  # 3
print('***')
# **********************************************************************************************************************
# Генераторы списков служат для создания новых списков на основе существующих

list3 = [2, 3, 4, 5, 6, 7]
list4 = [i * i for i in list3 if (i >= 3) and (i <= 6)]
print(list4)  # [9, 16, 25, 36]
# **********************************************************************************************************************