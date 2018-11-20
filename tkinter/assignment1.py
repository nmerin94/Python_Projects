from tkinter import *

window = Tk()

def comp_val() :
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)
    try :
        km = float(e1_value.get())
        t1.insert(END, km*1000)
        t2.insert(END, km*2.20462)
        t3.insert(END, km*35.274)
    except ValueError :
        t1.insert(INSERT, "Invalid Input")


l1_var = StringVar()
l1_var.set("km :")
e1_value = StringVar()

l1 = Label(window, textvariable = l1_var)
b1 = Button(window, text = "convert", command = comp_val)
t1 = Text(window, height = 1, width = 20)
t2 = Text(window, height = 1, width = 20)
t3 = Text(window, height = 1, width = 20)
e1 = Entry(window, textvariable = e1_value)



l1.grid(row = 0, column = 0)
e1.grid(row = 0, column = 1)
b1.grid(row = 0, column = 2)
t1.grid(row = 1, column = 0)
t2.grid(row = 1, column = 1)
t3.grid(row = 1, column = 2)



window.mainloop()
