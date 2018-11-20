from tkinter import *

window = Tk()

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l1 = Label(window, text = "Author")
l1.grid(row = 0, column = 2)

l1 = Label(window, text = "Year")
l1.grid(row = 1, column = 0)

l1 = Label(window, text = "ISBN")
l1.grid(row = 1, column = 2)

text_title = StringVar()
e1 = Entry(window, textvariable = text_title)
e1.grid(row = 0, column = 1)

text_author = StringVar()
e1 = Entry(window, textvariable = text_author)
e1.grid(row = 0, column = 3)

text_year = StringVar()
e1 = Entry(window, textvariable = text_year)
e1.grid(row = 1, column = 1)

text_isbn = StringVar()
e1 = Entry(window, textvariable = text_isbn)
e1.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 7, columnspan= 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 7, columnspan = 1)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "View all", width = 12)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 12)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 12)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12)
b6.grid(row = 7, column = 3)


window.mainloop()
