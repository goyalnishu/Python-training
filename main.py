

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
