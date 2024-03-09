import time

#Класс логирования сообщения с добавлением времени
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

#Класс логирования нового элемента списка с добавлением времени
class LoggableList(list, Loggable):                     #наследуем класс от стандартного list и класса Loggable
    def append(self, element):
        super(LoggableList, self).append(element)       #вызываем append у list для класса LoggableList, ассоциируем метод с self
        return self.log(element)                        #возвращаем лог, используя функцию из класса Loggable
    
ll = LoggableList()
ll.append('Hello!')
ll.append('Good bye!')   