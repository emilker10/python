class MoneyBox:
    def __init__(self, capacity, val = 0):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.val = val

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if (self.val + v <= self.capacity):
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        self.val = self.val + v

mb = MoneyBox(10)
print(mb.can_add(12))
if mb.can_add(12):
    mb.add(12)
print(mb.can_add(6))
if mb.can_add(6):
    mb.add(6)