"""Registration Form"""

from tkinter import *
from tkinter import messagebox
from mysql import connector

def database():
    conn = connector.connect(
       user='root',

       password='kali',

       host='127.0.0.1',

       port='3306',

       database='college')
    mycursor = conn.cursor()
    mycursor.execute("insert into reg values(%s,%s,%s,%s,%s,%s)",
                    (sr_no.get(), name.get(), roll_no.get(), address.get(), branch.get(), gender.get()))
    messagebox.showinfo("Info","Submitted")
    conn.commit()



ab=Tk()
ab.title("Registration form")

l_0 = Label(ab,text="Registration form",width=20,font=("bold", 20))
l_0.place(x=90,y=53)


l_1 = Label(ab,text="SR NO:",width=20,font=("bold", 10))
l_1.place(x=90,y=130)

sr_no = Entry(ab)
sr_no.place(x=210,y=130)

l_2 = Label(ab,text="NAME:",width=20,font=("bold", 10))
l_2.place(x=85,y=180)

name = Entry(ab)
name.place(x=210,y=180)

l_3= Label(ab,text="ROLL NO:",width=20,font=("bold",10))
l_3.place(x=82,y=230)
roll_no=Entry(ab)
roll_no.place(x=210,y=230)

l_4=Label(ab,text="ADDRESS:",width=20,font=("bold", 10))
l_4.place(x=80,y=280)

address=Entry(ab)
address.place(x=210,y=280)
branch=Label(ab,text="BRANCH:",width=20,font=("bold", 10))
branch.place(x=80,y=330)
branch= StringVar(ab)
branch.set("Select one")

dd= OptionMenu(ab,branch,"CSE","IT","ECE","ME","EE")
dd.pack()
dd.place(x=210,y=325)

l_6 = Label(ab,text="Gender:",width=20,font=("bold", 10))
l_6.place(x=75,y=380)
gender = StringVar()
Radiobutton(ab,text="Male",padx = 5, variable=gender, value=1).place(x=200,y=380)
Radiobutton(ab,text="Female",padx = 20, variable=gender, value=2).place(x=270,y=380)

Button(ab,text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=440)
ab.mainloop()
print("registration form  seccussfully created...")
