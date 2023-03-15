class Base:
    _b = 20
    __c = 30

    def __init__(self):
        self.a = 10

    def display(self):
        print("a: ",self.a)
        print("b: ",self._b)
        print("c: ",self.__c)

class Derived(Base):
    def __init__(self):
        super().__init__()

    def display(self):
        print("a: ",self.a)
        print("b: ",self._b)
        #print("c: ",self.__c)
'''
b1= Base()
b1.display()
#print(">>>>>",b1.__c) #Error
print("b1.b>>>>>",b1._b) #NoError
print("b1.a>>>>>",b1.a) #NoError
'''


d1= Derived()
d1.display()
#print(">>>>>",d1.__c) #Error
print("d1.b>>>>>",d1._b) #NoError
print("d1.a>>>>>",d1.a) #NoError

