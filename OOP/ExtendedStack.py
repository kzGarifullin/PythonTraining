class ExtendedStack(list):
    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())
    def sub(self):
        # операция вычитания
        self.append(self.pop()- self.pop())
    def mul(self):
        # операция умножения
        self.append(self.pop()* self.pop())
    def div(self):
        # операция целочисленного деления
        self.append(self.pop()// self.pop())

x = ExtendedStack()
print(x)
x.append(1)
x.append(2)
x.append(3)
x.append(4)
x.append(5)
x.sum()
print(x)

