class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.buffer = []
        
    def add(self, *a):
        # добавить следующую часть последовательности
        self.buffer += a                                #добавляем список к имеющемуся
        length = 0
        if len(self.buffer)>=5:                         #если длина буффера больше 5, то
            while(len(self.buffer)>=5):                 #пока она больше 5
                length = 5
                sum = 0
                for i in range(length):                 #считаем сумму
                    sum += self.buffer[i]
                self.buffer = self.buffer[length:]      #обновляем список (буффер)
                print(sum)
        else:                                           #если длина буффера меньше 5, то
            self.buffer = self.buffer[length:]          #обновляем список (буффер)

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        return self.buffer
        
buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part()) # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part()) # вернуть [1]    
buf.add(1,3) # Ничего не выводит
print(buf.get_current_part()) # вернуть [1, 1, 3]
buf.add(2,4) # Вывод print(11)
print(buf.get_current_part()) # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1) # Вывод print(5)
print(buf.get_current_part()) # вернуть [1, 1, 1]