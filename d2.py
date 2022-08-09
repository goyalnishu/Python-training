
a=44
b=64
c=26

print("Arithmetic", a+b, a-b, a*b, a/b, a//b, a%b, a**b)

print("Relational", a>b, a<b, a>=b, a<=b, a==b, a!=b)

print("logical", a>b and b>c, a>b or b>c, not(a>b and b>c))

print("Bitwise", a&b, a|b, a^b, ~a, ~b, ~c)

a+=2 

b+=7

print("Assignment", a, b)
if(a>b):
    print("Condition", a)
else:
    print("Condition", b)
print("Looping")


#pattern problem

for x in range (4):

   for y in range(4):

     print('*',end='')
   print()

for x in range(10):

  if x == 5:

    continue
  print(x)


  i = 1

while i < 6:

  print(i)
  
  i += 1

def pypart(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")


n = 5
pypart(n)
