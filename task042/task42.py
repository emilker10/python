from functools import cmp_to_key
from typing import List

#Пользовательский компаратор: сравнивает, какая комбинация двух строк дает большее число
def compare(x, y):
    if x + y > y + x:
        return -1                                           #x должен идти перед y
    elif x + y < y + x:
        return 1                                            #y должен идти перед x
    else:
        return 0                                            #они равны в порядке

def largestNumber(nums: List[int]) -> str:
    num_strs = list(map(str, nums))                         #преобразуем числа в строки для конкатенации
    num_strs.sort(key=cmp_to_key(compare))                  #сортируем список с использованием пользовательского компаратора
    largest_num = ''.join(num_strs)                         #объединяем отсортированные строки в самое большое число

    # Крайний случай: если самое большое число начинается с '0', возвращаем '0', иначе - само число
    return '0' if largest_num[0] == '0' else largest_num

nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))