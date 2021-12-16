# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
# Примечание: В сумму не включаем пустую строку и строку целиком
def task_1():
    import hashlib

    text = input('Введите строку: ')
    no_space_text = text.replace(' ', '')
    hash_set = set()
    for i in range(len(no_space_text)):
        for x in range(len(no_space_text), i, -1):
            hash_str = hashlib.sha1(no_space_text[i:x].encode('utf-8')).hexdigest()
            hash_set.add(hash_str)

    print(len(hash_set) - 1)


task_1()