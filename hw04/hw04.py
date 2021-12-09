# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Задание 1 из 3 урока.
import cProfile
from math import log


def task_1_1():
    for i in range(2, 1000):
        for x in range(2, 100):
            if i % x == 0:
                print(f'{i} делится на {x}')
        [print(f'{i} делаится на {x}') for x in range(2, 100) if i % x == 0]


def task_1_2():
    init_list = [i for i in range(2, 1000)]
    for item in range(2, 100):
        print(f'{item} - {len(list(filter(lambda x: x % item == 0, init_list)))}')


def task_1():
    task_1_1()
    task_1_2()


# cProfile.run('task_1()')

'''
         107251 function calls in 0.149 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.149    0.149 <string>:1(<module>)
      998    0.012    0.000    0.067    0.000 lesson4.py:14(<listcomp>)
        1    0.019    0.019    0.034    0.034 lesson4.py:17(task_1_2)
        1    0.000    0.000    0.000    0.000 lesson4.py:18(<listcomp>)
    97804    0.013    0.000    0.013    0.000 lesson4.py:20(<lambda>)
        1    0.000    0.000    0.149    0.149 lesson4.py:23(task_1)
        1    0.014    0.014    0.115    0.115 lesson4.py:9(task_1_1)
        1    0.000    0.000    0.149    0.149 {built-in method builtins.exec}
       98    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     8344    0.090    0.000    0.090    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''


# Реализация task_1_2 работает в 3 раза быстрее, чем task_1_1


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Используя алгоритм «Решето Эратосфена» (считает до 30 числа)


def task_2_1(i):
    a = [x for x in range(i * 4)]
    a[1] = 0
    m = 2
    while m < i * 4:
        if a[m] != 0:
            j = m * 2
            while j < i * 4:
                a[j] = 0
                j = j + m
        m += 1
    b = [x for x in a if x != 0]
    return b[i - 1]


# Без использования «Решета Эратосфена»;

def task_2_2(i):
    lst = []
    k = 0
    for i in range(2, i * 4):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0

    return lst.pop()


def task_2():
    print(task_2_1(30))
    print(task_2_2(30))


# cProfile.run('task_2()')

'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 lesson4.py:54(task_2_1)
        1    0.000    0.000    0.000    0.000 lesson4.py:55(<listcomp>)
        1    0.000    0.000    0.000    0.000 lesson4.py:65(<listcomp>)
        1    0.001    0.001    0.001    0.001 lesson4.py:71(task_2_2)
        1    0.000    0.000    0.001    0.001 lesson4.py:86(task_2)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
'''
# Не хватило времени до конца разобраться в решете Эратосфена, что бы поработать с большой последовательностью.
# И показать наглядную разницу в производительности.
# Сложно понять как откалибровать разные подходы рассчета к одному результату.
# Прошу строго не судить гуманитария)