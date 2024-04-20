import requests as req
import re

url = input()                           #считаем ссылку со стандартного ввода

site = req.get(url)                     #получаем текст страницы по ссылке

all_sites = []                          #результирующий список всех сайтов
links = re.findall(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|(\.\.)|)(.*?)(\/|:|\"|')(.*)", site.text)    #поиск нужной части html-ссылки 
for link in links:                      #для каждого элемента списка ссылок, найденых по регулярному выражению
    need_link = link[8]                 #нас интересует восьмая позиция элемента (это будет нужная нам часть ссылки)
    if need_link not in all_sites:      #если нужной ссылки еще нет в списке всех сайтов, то
        all_sites.append(need_link)     #добавляем ее в список

all_sites.sort()                        #сортировка списка

for site in all_sites:                  #вывод списка на экран
    print(site)