from tkinter import *
from backend import Database

database = Database("book.db")


def clear_entry():
    text_title.set("")
    text_author.set("")
    text_year.set("")
    text_isbn.set("")

def get_selected_row(event):
    try :

        index = list1.curselection()[0]  # list1.curselection() returns (1,), but list1.curselection()[0] returns 1
        global selected_tuple
        selected_tuple =list1.get(index) # will return the whole row displayed as a tuple
        text_title.set(selected_tuple[1])
        text_author.set(selected_tuple[2])
        text_year.set(selected_tuple[3])
        text_isbn.set(selected_tuple[4])
    except IndexError:
        pass
    '''
    Alternately , instead of setting the stringvar with values, we can directly insert INTO
    the entry widget.
    Example :
    e1.delete(0,END)
    e1.insert(END, selected_tuple[1])

    and do it for all entries together
    '''

def view_command() :
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in database.search(text_title.get(), text_author.get(), text_year.get(), text_isbn.get()) :
        list1.insert(END, row)

def add_command():
    database.insert(text_title.get(), text_author.get(),int(text_year.get()), int(text_isbn.get()))
    list1.delete(0, END)
    list1.insert(END, (text_title.get(), text_author.get(),int(text_year.get()), int(text_isbn.get())))

def delete_command():
    database.delete(selected_tuple[0]) # accessing a global variable
    clear_entry()
    list1.delete(0,END)
    list1.insert(END,selected_tuple)

def update_command():
    database.update(selected_tuple[0], text_title.get(), text_author.get(), text_year.get(), text_isbn.get())
    list1.delete(0, END)
    list1.insert(END,(text_title.get(), text_author.get(), text_year.get(), text_isbn.get()))


window = Tk()

window.wm_title("Book Store")

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

list1.bind('<<ListboxSelect>>', get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 7, columnspan = 1)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)


window.mainloop()
