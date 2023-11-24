alph = input("Alph: ")                          #алфавит
code = input("Code: ")                          #код
text_to_code = input("Text to code: ")          #текст, который необходимо зашифровать
text_to_alph = input("Text to alph: ")          #текст, который необходимо расшифровать

alph_code = {}                                  #словарь с алфавитом и кодом
count = 0                                       #количество обработанных символов

#Создаем словарь
for symbol in alph:
    alph_code[symbol] = code[count]             #в словаре ключ - алфавит, а значение - код
    count += 1

#Зашифровываем текст в символы кода
for symbol in text_to_code:                     #для каждого символа в тексте
    if symbol in alph:                          #если он существует в алфавите
        print(alph_code[symbol], end="")        #найдем значение по ключам и выведем
print()

#Расшифровываем текст в символы алфавита
for symbol in text_to_alph:                     #для каждого символа в тексте
    if symbol in code:                          #если он существует в коде
        for key, value in alph_code.items():    #пройдемся по словарю
            if symbol == value:                 #если символ равен одному из значений словаря, то
                print(key, end="")              #напечатаем его ключ
                break                           #выйдем из цикла, чтобы не обходить лишние элементы
print()                