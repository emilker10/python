import datetime                 #импортируем модуль 

curDate = input().split()       #считываем со стандартного ввода дату
#Для удобства разделим дату на переменные
year = int(curDate[0])
month = int(curDate[1])
day = int(curDate[2])

delta = int(input())            #считываем со стандартного ввода дельту-интервал в днях

#Используя модуль, сложим дату с интервалом и получим необходимое число
res = datetime.date(year, month, day) + datetime.timedelta(days=delta)
#Выведем результат, разделяя его через пробелы
print(res.year, res.month, res.day)