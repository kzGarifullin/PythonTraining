class MoneyBox:
    def __init__(self, capacity, money=0):
        self.capacity = capacity  # конструктор с аргументом – вместимость копилки
        self.money = money
    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if (self.capacity - self.money) >= v:
            return True
        else:
            return False
    def add(self, v):
        # положить v монет в копилку
        self.money += v

a = MoneyBox(10)
b = MoneyBox(10,8)

a.can_add(2)
b.can_add(2)
b.add(1)
b.can_add(2)
print(b.money)
