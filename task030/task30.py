mylist = []

with open("dataset_24465_4.txt") as inf:    #открываем файл на чтение
    for line in inf:                        #для каждой строки из этого файла
        line = line.rstrip()                #удалим символ переноса строки в конце строки и
        mylist.append(line)                 #запишем результат в список

contents = "\n".join(mylist[::-1])          #соединим содержимое списка в строку в обратном порядке, разделив элементы символом переноса строки

with open("out.txt", "w") as ouf:           #откроем файл на запись
    ouf.write(contents)                     #запишем строку в файл
