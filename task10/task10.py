#Предварительно установить модуль:
#pip install requests   - установка модуля requests
#Я пользуюсь vscode, поэтому вызов модуля requests происходит так
import pip._vendor.requests                                     #импортируем модуль requests

with open("dataset_3378_2.txt", 'r') as inf:                    #открываем файл на чтение
    url = inf.readline().strip()                                #считываем строку из файла, удаляя лишние символы переноса на след. строку
print(len(pip._vendor.requests.get(url).text.splitlines()))     #получаем по ссылке файл, считаем количество строк файла, разделяя текст

#Пояснения
"""
requests.get(url) - получает файл по ссылке
requests.get(url).text - получаем текст файла в виде строки
requests.get(url).text.splitlines() - разбиваем строку на список строк по переводам строк
"""