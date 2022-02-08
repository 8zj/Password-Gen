from tkinter import *
from random import randint
import webbrowser


window = Tk()

window.title('Strong password generator')
window.geometry("400x275")
window.config(bg='black')






def new():
    entry.delete(0, END)
    pw_length = int(my_entry.get())
    password = ''

    for x in range(pw_length):
        password += chr(randint(1, 100))

    entry.insert(0, password)


box = LabelFrame(window, text="How Many Characters?", bg='black', fg='white')
box.pack(pady=10)

box2 = LabelFrame(window, text="Your password!", bg='black', fg='white')
box2.pack(pady=10)


entry = Entry(box2, text='', font=("Helvetica", 20), bd=0, bg="white")
entry.pack(pady=10, padx=10)

frame = Frame(window, bg='black')
frame.pack(pady=5)

my_entry = Entry(box, font=("Consolas", 20),bg='white', fg='black')
my_entry.pack(pady=20, padx=20)

def copy():
    window.clipboard_clear()
    window.clipboard_append(entry.get())


button = Button(frame, text="Generate", bg='black', fg='white',relief=SUNKEN, command=new)
button.grid(row=0, column=0, padx=2)

button1 = Button(frame, text="Copy", bg='black', fg='white',relief=SUNKEN, command=copy)
button1.grid(row=2, column=0, padx=2, pady=2)


window.mainloop()
