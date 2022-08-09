a = 200
b = 100


class MyClass():
    a = 20
    b = 10


    def add(self, a, b):
     print(a+b)
     print(globals()['a']+globals()['b'])
     print(self.a+self.b)


    def mul(self, a, b):
     print(a*b)
     print(globals()['a']+globals()['b'])
     print(self.a*self.b)


c = MyClass()
c.add(3, 3)
c.mul(4, 4)


#.......OUTPUT..........
'''
6
300
30 
16 
300
200
'''
