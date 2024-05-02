import requests
import json

#Пара идентификторов, полученных с проекта Artsy
client_id = '3e022917e0d532eb5824'
client_secret = '5c80ef00f80fdef045c62e576a54ebac'

#Получаем токен доступа к API
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",    #инициируем запрос на получение токена
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)                                              #разбираем ответ сервера
token = j["token"]                                                  #достаем токен


dict = {}                                                           #словарь, в котором ключ - имя артиста, а значение - год рождения

#Выполняем запрос к серверу и разбираем его ответ
headers = {"X-Xapp-Token" : token}                                  #создаем заголовок, содержащий наш токен
with open("dataset_24476_4.txt") as inf:                            #открываем файл на чтение
    for line in inf:                                                #для каждой строки из этого файла
        num = line.rstrip()                                         #удалим символ переноса строки в конце строки
        api_url = "https://api.artsy.net/api/artists/"              #API-ссылка на ресурс
        api_url = api_url+num                                       #формируем правильный запрос
        r = requests.get(api_url, headers=headers)                  #инициируем запрос с заголовком
        j = json.loads(r.text)                                      #разбираем ответ сервера

        if j["sortable_name"] not in dict:                          #если имени артиста нет в словаре, то
            dict[j["sortable_name"]] = j["birthday"]                #добавляем его в словарь с его годом рождения

sortedArt = sorted(dict.items(), key=lambda x: (x[1], x[0]))        #сортируем словарь, на выходе получаем list из кортежей

for item in sortedArt:
    print(item[0])
