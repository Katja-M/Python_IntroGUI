'''
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete entry
Close
'''

# Grid method will be used to pack the widgets

from tkinter import *
from backend_oob import Database

database = Database('books.db')

def get_selected_row(event):
    # Selects the index in the list shown to user
    index = list1.curselection()[0]
    # Gets the full tuple which has the above selected index
    global selected_tuple
    selected_tuple = list1.get(index)
    
    e1.delete(0, END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])



def view_command():
    # Without the following line, this method would only append all database entry to the list
    # whenever the user presses View all
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)
        # END ensures that new rows will be put at the end of the listbox

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        # title_text and all other entries are not plain strings
        # Therefore, the get() method is required to produce a string
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

# Tk() method creates a window
window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text = 'Title')
l1.grid(row = 0 , column = 0)

l2 = Label(window, text = 'Author')
l2.grid(row = 0 , column = 2)

l3 = Label(window, text = 'Year')
l3.grid(row = 1 , column = 0)

l4 = Label(window, text = 'ISSBN')
l4.grid(row = 1 , column = 2)

title_text = StringVar()
# textvariable parameter expects as an argument the value that will be entered by the user
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
# textvariable parameter expects as an argument the value that will be entered by the user
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 4)

year_text = StringVar()
# textvariable parameter expects as an argument the value that will be entered by the user
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
# textvariable parameter expects as an argument the value that will be entered by the user
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 4)

list1 = Listbox(window, height = 6, width = 35)
# Adding rowspan and columnspan as arguments such that the listbox spans over multiple rows and columns
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

# Creating scrollbar which allows the user to scroll the list

# 1. Create scrollbar
sb1 = Scrollbar(window)
sb1.grid(row = 1, column = 2, rowspan = 6)
# 2. Tell the list about the scrollbar
list1.configure(yscrollcommand = sb1.set)
# 3. Tell the scrollbar about the list
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

# Creating buttons
# Command parameters will decide what the button will do
b1 = Button(window, text = 'View all', width = 12, command = view_command)
# view_command is passer without brackets because in that way it will be executed when the user presses the button
b1.grid(row = 2, column = 3)

b2 = Button(window, text = 'Search entry', width = 12, command = search_command)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = 'Add entry', width = 12, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = 'Update selected', width = 12, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = 'Delete selected', width = 12, command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = 'Close', width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

# Wraps up all the widgets which are entered between tk() and mainloop() methods
window.mainloop()

'''
Creating an executable
1) Enter the command in command line
pyinstaller --onefile --windowed gui.py

--onefile ensures that only one file is created
--windowed stops the terminal from opening'''