from tkinter import *

# Tkinter programm is made up of two main faces
# The window and the widgets

# Create a window
window = Tk()

# Function which is deployed in the GUI
def km_to_miles():
    print(e1_value.get())
        #e1_value.get() generates a string
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)

# Generates button widget
# Passing the function without brackets
b1 = Button(window, text = 'Execute', command = km_to_miles)
# Specifying where to put button
b1.grid(row = 0, column = 0)
# Other possible methode
# b1.pack()

# Adding entry widget
# Entry allows to enter a value
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

# Adding text widget
# Default size of text widget is very large
# Hence, shape is defined
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)



# Always at end of code
window.mainloop()