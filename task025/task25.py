#Новый класс для обозначения о неположительном значении, унаследованный от Exception
class NonPositiveError(Exception):
    pass

#Новый класс, обрабатывающий добавление элемента к списку, унаследованный от list
class PositiveList(list):
    def append(self, x):
        if x>0:                                             #если число положительное, то
            super(PositiveList, self).append(x)             #использовать метод append, имющийся в классе list
        else:                                               #иначе
            raise NonPositiveError("NonPositiveError")      #выбросить ошибку NonPositiveError
        
ll = PositiveList([1,2,3])
ll.append(4)
ll.append(0)
ll.append(-1)
