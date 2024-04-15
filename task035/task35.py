import requests as req
import re

#a = input()
#b = input()

a = "https://stepik.org/media/attachments/lesson/24472/sample0.html".replace('stepic.org', 'stepik.org')
b = "https://stepik.org/media/attachments/lesson/24472/sample2.html".replace('stepic.org', 'stepik.org')

def get_links(url):
    try:
        site = req.get(url)                                     #получаем текст страницы по ссылке
        links = re.findall(r'<a.*href="([^"]*)"', site.text)    #ищем все совпадения с регулярным выражением и формируем список
    except:
        return []
    else:
        return links

def two_steps():
    links1 = get_links(a)           #получаем список ссылок со страницы из ссылки a
    cycle_sites = list(map(lambda x: x.replace('stepic.org', 'stepik.org'), links1))        #заменяем stepic на stepik, формируем новый список

    for link in cycle_sites:        #пройдемся по каждому элементу списка и
        links2 = get_links(link)    #получаем список ссылок со страницы каждого элемента списка
        cycle2_sites = list(map(lambda x: x.replace('stepic.org', 'stepik.org'), links2))   #заменяем stepic на stepik, формируем новый список
        if b in cycle2_sites:       #проверяем  имеется ли ссылка b в списке ссылок со второй страницы
            return True
    return False

if two_steps():
    print("Yes")
else:
    print("No")