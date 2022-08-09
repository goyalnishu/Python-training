def outer():
    s = "Ludhiana"

    def inner1():
        s = "punjab"
        inner1()
        print(s)

    def inner2():
            nonlocal s
            s = "Chandigarh"
    inner2()
    print(s)

    def inner3():
        global s
        s = "Haryana"
        print(s)
    inner3()
    print(s)


outer()
print(s)


#.......OUTPUT..........
'''
Chandigarh
Haryana   
Chandigarh
Haryana
'''
