class ExtendedStack(list):
    def sum(self):
        # операция сложения
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1+top2)

    def sub(self):
        # операция вычитания
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1-top2)

    def mul(self):
        # операция умножения
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1*top2)

    def div(self):
        # операция целочисленного деления
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1//top2)


stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
stack.sum()
print(stack)
stack.sub()
print(stack)
stack.mul()
print(stack)
stack.div()
print(stack)