class A:
    def f1(self):
        print("A")
class B(A):
    def f2(self):
        print("B")
d = B()
d.f1()
d.f2()

#........Multilevel.......

class A:
    def f1(self):
        print("A")
class B(A):
    def f2(self):
        print("B")
class C(B):
    def f3(self):
        print("C")
d = C()
d.f1()
d.f2()
d.f3()

#.........Hierarchical.........
class A:
    def f1(self):
        print("A")
class B(A):
    def f2(self):
        print("B")
class C(A):
    def f3(self):
        print("C")
d = C()
d1=B()
d.f3()
d1.f2()

#..........super keyword......
class A:
 a=10
 b=20
 def __init__ (self): 
      print('a')
 def ml (self): 
    print ('ml')
class b (A):
 a=4
 b=5
 def m2 (self):
  print (self.a, self.b)
  print (super().a, super().b)

ob=b()
ob.ml ()
ob.m2 ()

#........polymorphism..........
def add(x, y, z = 0):
    return x + y+z
 
print(add(2, 3))
print(add(2, 3, 4))


#......maths module.....
from math import *  
     
print( "Calculating square root: ", sqrt(25) )  
print( "Calculating tangent of an angle: ", tan(pi/6) ) 
