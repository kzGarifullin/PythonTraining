class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.data = []
    def add(self, *a):
        # добавить следующую часть последовательности
        for x in a:
            self.data.append(x)
        summ = 0
        count = len(self.data) //5
        for i in range(0,count):
            if len(self.data) >= 5:
                summ = sum(self.data[:5])
                self.data = self.data[5:]
                print(summ)
    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были     
        # добавлены
        return(self.data)
        #print(self.data)   
 

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
