# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
       # 0  1  2  3   4   5  6  7   8   9  10 11  12 13 14  15  16 17  18  19
# list1= [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list2 = []
# for i in range(len(list1)):
#     if list1[i] >= 7 and list1[i] < 11:
#         list2.append(i)
# print(list2) 


# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент (a1), разность(d) и количество
# элементов(n) нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d
# Каждое число вводится с новой строки.

n = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите шаг прогрессии: '))
c = int(input('Введите кол-во эл-ов: '))
for i in range(n):
    print(f'Арифметическая прогрессия по введеным элементам: ', n + i * d)



