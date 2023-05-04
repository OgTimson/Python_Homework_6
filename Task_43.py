# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках. 
# Ввод: 1 2 3 2 3    Вывод: 2

from random import randint

def pair_count(the_list, n):
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if the_list[i] == the_list[j]:
                count += 1
    return count

n = int(input('Введите количество чисел, которое будет в списке: '))
the_list = [randint(1, 5) for i in range(n)]
print(the_list)
print(f'Количество пар элементов равных друг другу: {pair_count(the_list, n)}')