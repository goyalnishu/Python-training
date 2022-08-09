

s = "madam"
sl =s[::-1]
print(sl)

if sl==s:
   print("Yes")
else:
   print("No")
num = int(input("Enter a value:"))
temp = num
rev = 0

while (num > 0):
  dignum % 10
  rev = rev * 10 + dig
  num = num // 10

if (temp == rev):
 print("This value is a palindrome number!")
else:
 print("This value is not a palindrome number!")




# ..........LIST........
l1 = [1, 2, 3, 4, 5, 6, 7]
l1.append(33)
print(l1[0])
print(l1[:])

# ..........TUPLE........
T = 10, 20, 30, 40, 50
print(T)
print(type(T))

# ..........SET........
s = {1, 2, 3, 4, 5, 6}
print(s)
print(type(s))

# ..........DICTIONARY........
D = {1: 'Anish',
     2: 'Manish',
     3: 'Rajnish', }
print(D)
print(type(D))


# ..........FUNCTION........
def square(num):
    return num**2


object_ = square(9)
print("The square of the number is: ", object_)
