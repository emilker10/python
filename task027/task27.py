from simplecrypt import decrypt                     #импортируем библиотеку

with open("encrypted.bin", "rb") as inp:            #открываем бинарный файл на чтение
    encrypted = inp.read()                          #читаем файл

with open("passwords.txt", 'r') as inf:             #открываем текстовый файл на чтение 
    for line in inf:                                #для каждой строки из файла
        line = line[:-1]                            #убираем лишний символ переноса строки
        try:
            plaintext = decrypt(line, encrypted)    #пытаемся раскодировать файл
        except Exception:
            pass
        else:
            print(plaintext)
