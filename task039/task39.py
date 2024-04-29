import requests

with open("dataset_24476_3.txt") as inf:            #открываем файл на чтение
    for line in inf:                                #для каждой строки из этого файла
        num = line.rstrip()                         #удалим символ переноса строки в конце строки
        
        api_url = "http://numbersapi.com/"          #API-ссылка на ресурс
        api_url = api_url+num+"/math"               #формируем правильный запрос
        params = {                                  #формируем параметры запроса
            "json": "true"
        }
        res = requests.get(api_url, params=params)  #отправляем запрос на ресурс
        data = res.json()                           #получаем результат в виде json

        if data["found"]:                           #проверяем результат логического значения, определяющего, существовал ли факт для запрошенного номера
            print("Interesting")
        else:
            print("Boring")
