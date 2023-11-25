word_container_num = int(input("Number: "))                             #считываем со стандартного ввода количество известных слов
word_container = []                                                     #список известных слов

#Считываем со стандартного ввода указанное количество строк
while word_container_num>0:
    word_container += input("Word: ").lower().strip().split(" ")        #строку приводим к одному регистру, удаляем символы перевода но новую строку, разделяем слова по пробелам
    word_container_num -= 1

new_word_container_num = int(input("Number: "))                         #считываем со стандартного ввода количество слов для проверки
new_word_container = []                                                 #список неизвестных слов

#Считываем со стандартного ввода указанное количество строк
while new_word_container_num>0:
    new_word_container += input("Word: ").lower().strip().split(" ")    #строку приводим к одному регистру, удаляем символы перевода но новую строку, разделяем слова по пробелам
    new_word_container_num -= 1

bad_words = set()                                                       #создаем множетсво плохих слов

#Проверяем новые слова на наличие ошибок
for new_word in new_word_container:                                     #для каждого новго (неизвестного) слова из своего списка
    equal = False
    for word in word_container:                                         #перебираем каждое изместное слово из своего списка
        if new_word == word:                                            #если они совпадают, то
            equal = True                                                #они равны, переключаем флаг
            break                                                       #выходим из цикла
    if equal==False:                                                    #если равных в процессе перебора не было, то
        if new_word not in bad_words:                                   #проверяем наличие неизвестного слова во множестве ошибочных слов
            bad_words.add(new_word)                                     #если нет такого слова - добавляем
            print(new_word)                                             #печатаем его
