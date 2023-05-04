# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

n = int(input('Введите количество элементов для списка: '))
the_list = [randint(-9, 9) for i in range(n)]
print(the_list)

min_num = int(input('\nВведите минимальное число диапазона: '))
max_num = int(input('Введите максимальное число диапазона: '))
indexes = []

for i in range(n):
    if min_num <= the_list[i] <= max_num:
        indexes.append(i)

print(f'\nИндексы элементов, значения которых принадлежат заданному диапазону: {indexes}')