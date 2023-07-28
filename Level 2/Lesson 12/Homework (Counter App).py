# Write a Tkinter app that has a button and a label. The label will show a number that shows how many times you clicked the button.
from tkinter import *
window=Tk()

counter = 0

def count():
    global counter
    counter = counter + 1
    label1.config(text=counter)

# add widgets here
button1 = Button(window,text="Click", command=count)
button1.place(x=120,y=100)

label1 = Label(window,text=counter)
label1.place(x=120, y=70)
window.title('Hello Python')
window.geometry("300x200+555+220")
window.mainloop()
