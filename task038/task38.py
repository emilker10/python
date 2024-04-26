import json

#str = input()
str = "[{\"name\": \"A\", \"parents\": []}, {\"name\": \"B\", \"parents\": [\"A\", \"C\"]}, {\"name\": \"C\", \"parents\": [\"A\"]}]"

data = json.loads(str)

with_children = {element['name']: [] for element in data}   #создаем словарь, в котором ключ будет узел графа, а значение - его наследники

#Заполняем словарь данными
for el in data:                                             #построчно смотрим json
    for el_ch in with_children:                             #для каждого элемента name в json
        if el_ch in el['parents']:                          #проверяем его наличие в элементе parents, если есть, то
            with_children[el_ch].append(el['name'])         #дополняем словарь: записываем какие наследники имеются для каждого из родителя

#Преобразуем значение каждого ключа словаря во множество
for element in with_children:
    with_children[element] = set(with_children[element])

#Рекурсивно проходим по графу для того, чтобы понять наследование элементов 
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

#В сортированном виде выводим на печать
for element in sorted(with_children.keys()):
    print(element, ':', len(dfs(with_children, element)))