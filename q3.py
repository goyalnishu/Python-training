a_var = 10
b_var = 15
e_var = 25
d_var = 100


def a_func(a_var):
 print("in a_funca_var =", a_var)
b_var = 100 + a_var
d_var = 2 * a_var
print("in a_funcb_var =", b_var)
print("in a_funcd_var =", d_var)
print("in a_funce_var =", e_var)

c_var = a_func(b_var)
print("a_var =", a_var)
print("b_var =", b_var)
print("c_var =", c_var)
print("d_var =", d_var)

#.......OUTPUT..........
'''.vscode\in a_funcb_var = 110
in a_funcd_var = 20 
in a_funce_var = 25 
in a_funca_var = 110
a_var = 10
b_var = 110
c_var = None        
d_var = 20
'''
