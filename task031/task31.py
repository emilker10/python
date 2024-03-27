import os

mylist = []

for current_dir, dirs, files in os.walk("."):                   #пройдемся по содержанию текущей директории 
    for file in files:                                          #для каждого имени файла в списке имен файлов
        if file.endswith(".py"):                                #если файл оканчивается с расширением .py, то
            current_dir = current_dir.lstrip('./')              #удалить начало строки
            if current_dir not in mylist and current_dir!="":   #если такого файла нет в новом списке, то
                mylist.append(current_dir)                      #добавить его

mylist.sort()                                                   #отсортировать список в лексикографическом порядке
contents = "\n".join(mylist[::])                                #соединим содержимое списка в строку, разделив элементы символом переноса строки

with open("out.txt", "w") as ouf:                               #открыть файл на запись
    ouf.write(contents)                                         #записать строку