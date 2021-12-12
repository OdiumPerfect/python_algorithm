# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import *


def task_1(task1_list):
    a = task1_list
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j - 1] < v) and (j > 0):
            a[j] = a[j - 1]
            j = j - 1
        a[j] = v
    return a


task1_list = [randint(-100, 100) for x in range(20)]
print(task1_list)
print(task_1(task1_list))


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


def merge_sort(a):
    if len(a) < 2:
        return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:len(a)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a[k] = right[j]
        j = j + 1
        k = k + 1
    return a


array = [uniform(0, 50) for i in range(20)]
print(array)
print(merge_sort(array))


# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

# Данную задачу самому решить не получилось

def get_median(sub, pivot_fn=choice):
    return subpart(sub, len(sub) // 2, pivot_fn)


def subpart(sub, k, pivot_fn):
    pivot = pivot_fn(sub)
    lows = [x for x in sub if x < pivot]
    highs = [x for x in sub if x > pivot]
    pivots = [x for x in sub if x == pivot]
    if k < len(lows):
        return subpart(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return subpart(highs, k - len(lows) - len(pivots), pivot_fn)


array = [round(50 * random(), 2) for _ in range(2 * 10 + 1)]
print(array)
print(sorted(array))
print(get_median(array))
