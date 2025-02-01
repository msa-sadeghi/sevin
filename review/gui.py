from tkinter import *

def my_function():
    my_label.config(text=username_sting.get())
    file = open("file", "a", encoding="UTF-8")
    file.write(username_sting.get())

def move_cursor_to_end(event= None):
    
    username.icursor(0)

window = Tk()
window.geometry("300x300")

username_sting = StringVar()

my_label = Label(window, text="نام کاربری")
my_label.pack()
username = Entry(window, textvariable=username_sting, width=30, justify="right")
username.bind("<KeyPress>", move_cursor_to_end)

username.pack()

my_button = Button(window, text="کلیک کنید", command=my_function)
my_button.pack()
move_cursor_to_end()
window.mainloop()