def f():
 x = 42
def g():
 global x
x = 43
print("Before calling g: ",x)
g()
print("After calling g: ",x)

f()
print("x in main: " ,x)


#.......OUTPUT..........
'''
Before calling g:  43
After calling g:  43 
x in main:  43 
'''
