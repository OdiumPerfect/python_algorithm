# 1 Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num_1 = list(input('Введите трехзначное число '))
sum_1 = 0
multiply_1 = 1
for i in num_1:
    sum_1 = sum_1 + int(i)
    multiply_1 = multiply_1 * int(i)
print(sum_1)
print(multiply_1)

# 2 Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.


print(5 & 6, 5 | 6)
print(5 >> 2, 5 << 2)

# 3  По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1 = int(input('Введите значение по координате x первой точки '))
y1 = int(input('Введите значение по координате y первой точки '))
x2 = int(input('Введите значение по координате x второй точки '))
y2 = int(input('Введите значение по координате y второй точки '))


k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
sign = '+' if b > 0 else '-'
print(f'y = {k} * x {sign} {abs(b)}')

# 4 Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from random import *

integer_1 = int(input('Введите целое число начала диапазона: '))
integer_2 = int(input('Введите целое число конца диапазона: '))
fractional_num_1 = float(input('Введите дробное число начала диапазона: '))
fractional_num_2 = float(input('Введите дробное число конца диапазона: '))
letter_1 = input('Введите букву начала диапазона: ')
letter_2 = input('Введите букву конца диапазона: ')


print(f'Случайное целое число: {randint(integer_1, integer_2)}')
print(f'Случайное вещественное число: {round(uniform(fractional_num_1, fractional_num_2), 2)}')
print(f'Случайный символ: {choice([chr(i) for i in range(ord(letter_1),ord(letter_2))])}')


# 5 Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')
first_letter_position = ord(first_letter) - ord("a") + 1
second_letter_position = ord(second_letter) - ord("a") + 1
sign_5 = -1 if (second_letter_position - first_letter_position) > 0 else 1

print(
    f'Первая буква '
    f'{first_letter_position} в алфавите, вторая буква {second_letter_position} в алфавите. '
    f'Между ними {(second_letter_position - first_letter_position) + sign_5} букв')


# 6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_position = int(input('Введите номер буквы в алфавите: '))
print(f'Ваша буква {chr(letter_position + 96)}')


# 7 По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует,
# то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Сторона a в см: '))
b = int(input('Сторона b в см: '))
c = int(input('Сторона c в см: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    if (a == b and a != c) or (a == c and a != b) or (c == b and c != a):
        print('Треугольник равнобедренный')
    elif a == b == c:
        print('Треугольник равносторонний')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник составить невозможно')

# 8 Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год: '))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Год високосный')
else:
    print('Год не високосный')

# 9 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

result = sorted([num_1, num_2, num_3])

print(f'Средним числом является {num_2}')
