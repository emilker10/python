n = int(input())                                                            #считываем данные со стандартного ввода
#Создаем словарь в котором:
#'global' - это пространство имён (namespace), значение которого состоит из словоря с ключами:
#'funcs' - список пространство имён, в котором находится сама функция
#'vars' - список значений, содержащихся в данном пространстве
scopes = {'global': {'funcs': [], 'vars': []}}                              

#Функция добавления пространства имен
def add(scopes, current_namespace, what):
    if current_namespace not in scopes:                                     #если пространство имен не содержится в словаре, то
        scopes[current_namespace] = {}                                      #создаем ключ нового элемента словаря                          
        scopes[current_namespace]['vars'] = []                              #создаем значение списка значений нового элемента словаря
        scopes[current_namespace]['vars'].append(what)                      #добавляем значение в список значений нового нового элемента словаря
    else:                                                                   #если пространство имен содержится в словаре, то
        if 'vars' not in scopes[current_namespace]:                         #если пространство значений содержится в словаре, то
            scopes[current_namespace]['vars'] = []                          #создаем значение списка значений нового элемента словаря
            scopes[current_namespace]['vars'].append(what)                  #добавляем значение в список значений нового нового элемента словаря
        else:                                                               #если значение уже имеется в списке значений, то
            scopes[current_namespace]['vars'].append(what)                  #добавляем значение в список значений нового нового элемента словаря

#Функция создания пространства имен
def create(scopes, current_namespace, parent_namespace):
    if current_namespace not in scopes:                                     #если пространство имен не содержится в словаре, то
        scopes[current_namespace] = {}                                      #создаем ключ нового элемента словаря
        scopes[current_namespace]['funcs'] = []                             #создаем значение списка функций нового элемента словаря
        scopes[current_namespace]['vars'] = []                              #создаем значение списка значений нового элемента словаря
        #Добавляем новый элемент в словарь
        scopes[parent_namespace]['funcs'].append(current_namespace)
        scopes[current_namespace]['parent'] = parent_namespace
    else:                                                                   #если пространство имен содержится в словаре, то
        if 'funcs' not in scopes[current_namespace]:                        #если функция не имеется в списке функций, то
            scopes[current_namespace]['funcs'] = []                         #создаем значение списка функций нового элемента словаря
            #Добавляем новый элемент в словарь
            scopes[current_namespace]['parent'] = parent_namespace
            scopes[parent_namespace]['funcs'].append(current_namespace)
        else:                                                               #если функция уже имеется в списке функций, то
            #Добавляем новый элемент в словарь
            scopes[current_namespace]['funcs'].append(current_namespace)
            scopes[parent_namespace]['funcs'].append(current_namespace)

#Функция поиска значения
def search(scopes, namespace, what):
    if what in scopes[namespace]['vars']:                                   #если искомое значение есть в списке значений, то
        return namespace                                                    #возвращаем имя пространство имен
    else:                                                                   #если искомого значения нет в списке значений, то
        try:
            upper_namespace = scopes[namespace]['parent']                   #пытаемся зайти в подгруппу имен, чтобы найти в ней
        except KeyError:
            return None                                                     #возвращаем None если выпала ошибка - значит такого значения нет
        return search(scopes, upper_namespace, what)                        #рекусивно вызываем функцию поиска, но уже в подгруппе имен

#Основная программа, выполняющие действия в зависимоти от входных значений
for i in range(n):
    command = input().split()
    if command[0] == 'add':
        add(scopes, command[1], command[2])
    elif command[0] == 'create':
        create(scopes, command[1], command[2])
    elif command[0] == 'get':
        print(search(scopes, command[1], command[2]))
