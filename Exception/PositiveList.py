class PositiveList(list):
    def append(self,x):
        if x>0:
            super(PositiveList,self).append(x)
        else:
            raise NonPositiveError

class NonPositiveError(Exception):
    pass

a = PositiveList()

a.append(1)
print(a)
a.append(2)
print(a)
a.append(-3)
