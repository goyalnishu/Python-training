# .......local Variable......

def f():
    y = "local"
    print(y)

f()

# .......local Variable......

x = "global"
def foo():
    print("x inside:", x)
foo()
print("x outside:", x)

# .....Both local and Global.....

x = "global "
def f1():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
f1()

# ......nonlocal variable..........

def f2():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
f2()

# ......Class..........
class Employee:    
    id = 10   
    name = "Anish"    
    def display (self):    
        print("ID: %d \nName: %s"%(self.id,self.name))     
emp = Employee()    
emp.display()   


#...........Constructor.......
class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
emp1 = Employee("Anish", 101)  
emp2 = Employee("Nikhil", 102)   
  
emp1.display()  
emp2.display()  
