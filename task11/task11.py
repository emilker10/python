#Предварительно установить модуль:
#pip install requests   - установка модуля requests
#Я пользуюсь vscode, поэтому вызов модуля requests происходит так
import pip._vendor.requests as requests                         #импортируем модуль requests

with open("dataset_3378_3.txt", 'r') as inf:                    #открываем файл на чтение
    url = inf.readline().strip()                                #считываем строку из файла, удаляя лишние символы переноса на след. строку

name = requests.get(url).text
text = ""
new_url = "https://stepik.org/media/attachments/course67/3.6.3/"
count = 0

while True:
    text = requests.get(new_url+name).text                      #обновляем текст - содержание файла
    if text[:2] == "We":                                        #если текст начинается с  "We", то
        with open("result.txt", 'a') as ouf:                    #открываем файл на дозапись
            ouf.write(requests.get(new_url+name).text)          #записываем весь текст в файл
        break                                                   #завершаем цикл
    else:                                                       #иначе
        name = requests.get(new_url+name).text                  #запоминаем текст - содержание файла, оно будет именем для новго файла
        count += 1                                              #итерируем количество файлов
        with open("task11.txt", 'a') as ouf:                    #открываем файл на дозапись
            ouf.write(str(count)+" "+name+"\n")                 #записываем номер файла и его содержание

#Пояснения
"""
requests.get(url) - получает файл по ссылке
requests.get(url).text - получаем текст файла в виде строки
requests.get(url).text.splitlines() - разбиваем строку на список строк по переводам строк
"""