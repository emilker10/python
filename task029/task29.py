import itertools

#Функция, определяющая является ли число простым
def isSimple(num):
    if num == 2: return True        #если число равно двум, то оно простое
    if num % 2 == 0: return False   #если остаток от деления числа на два равно нулю, то оно не является простым
    for i in range(3, num, 2):      #в цикле от 3 до нужного числа с шагом 2 (чтобы итерироваться только по нечетным числам)
        if num % i == 0:            #проверяем остаток от деления
            return False
    return True

#Функция-генератор простых числел, начиная с числа 2
def primes():
    num = 2
    while True:
        if isSimple(num):
            yield num
        num += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]