from tkinter import *

ab=Tk()
a = Label(ab ,text = "First Name").place(x = 0,y = 0)
b = Label(ab ,text = "Branch").place(x = 0,y = 20)
c = Label(ab ,text = "Email Id").place(x = 0,y = 40)
d = Label(ab ,text = "Contact Number").place(x = 0,y = 60)
a1 = Entry(ab).place(x = 100,y = 0)
b1 = Entry(ab).place(x = 100,y = 20)
c1 = Entry(ab).place(x = 100,y = 40)
d1 = Entry(ab).place(x = 100,y = 60)
e=Button(ab,text="Click Here",fg="black",bg="grey").place(x=100,y=80)
ab.mainloop()