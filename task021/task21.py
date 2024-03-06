classes = {}

#Функция добавления класса в словарь
def add_class(classes, class_name, parents):
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].extend(parents)
    for parent in parents:
        if parent not in classes:
            classes[parent] = []

#Функция поиска пути
def found_path(classes, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in classes:
        return None
    for node in classes[start]:
        if node not in path:
            newpath = found_path(classes, node, end, path)
            if newpath: return newpath
    return None

def answer(classes, parent, child):
    if not(parent or child) in classes or not found_path(classes, child, parent):
        return 'No'
    return 'Yes'

n = int(input())                                    #считываем со стандартного ввода число классов
for _ in range(n):                                  #для следующих классов
    class_description = input().split()             #считываем их со стандартного ввода
    class_name = class_description[0]               #имя класса
    class_parents = class_description[2:]           #родители класса
    add_class(classes, class_name, class_parents)   #вызываем функцию добавления классов в словарь 

q = int(input())                                    #считываем со стандартного ввода число запросов
for _ in range(q):                                  #для каждого из запросов
    question = input().split()                      #считываем их со стандартного ввода
    parent = question[0]                            #запоминаем родителя
    child = question[1]                             #запоминаем наследника
    print(answer(classes, parent, child))