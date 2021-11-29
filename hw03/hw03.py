from random import randint


# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def task_1():
    for i in range(2, 100):
        for x in range(2, 10):
            if i % x == 0:
                print(f'{i} делится на {x}')
        [print(f'{i} делаится на {x}') for x in range(2, 10) if i % x == 0]


# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

def task_2():
    my_list = [8, 3, 15, 6, 4, 2, 5, 2, 33, 8, 9]
    print([x for x, y in enumerate(my_list) if y % 2 == 0])


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


def task_3():
    rand_list = [randint(1, 100) for x in range(10)]
    print(rand_list)
    idx_max = rand_list.index(max(rand_list))
    idx_min = rand_list.index(min(rand_list))
    rand_list[idx_max], rand_list[idx_min] = rand_list[idx_min], rand_list[idx_max]
    print(rand_list)


# 4. Определить, какое число в массиве встречается чаще всего.
from collections import Counter


def task_4():
    my_list = [randint(1, 3) for x in range(10)]
    print(my_list)
    # print(f'Чаще всего встречается число: {list(Counter(my_list)[0])}')
    cnt = Counter(my_list)
    print(cnt)
    print(f'Больше всего встречается значение: {cnt.most_common(1)[0][0]}')


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

def task_5():
    my_list = [randint(-19, 10) for x in range(10)]
    min_list = []
    print(my_list)
    for i in my_list:
        if i < 0:
            min_list.append(i)
    print(f'Число {max(min_list)} под индексом {my_list.index(max(min_list))}')


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
def task_6():
    my_list = [randint(-10, 10) for x in range(10)]

    min_idx = my_list.index(min(my_list))
    max_idx = my_list.index(max(my_list))
    print(my_list)
    print(min_idx, max_idx)
    direction = 1 if max_idx > min_idx else -1
    print(sum(my_list[min_idx:max_idx:direction]) - my_list[min_idx])


# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def task_7():
    my_list = [randint(-10, 10) for x in range(10)]
    print(my_list)
    print(min(my_list))
    my_list.remove(min(my_list))
    print(min(my_list))


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
def task_8_9():
    matrix = [[randint(0, 10) for x in range(4)] for _ in range(4)]

    for item in matrix:
        item += [sum(item)]

    str_out = '\n'.join(['\t'.join(map(str, item)) for item in matrix])
    print(str_out)
    print(matrix)

    # 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

    min_matrix_list = []
    for i in matrix:
        min_matrix_list.append(min(i))
    print(min_matrix_list)
    print(max(min_matrix_list))