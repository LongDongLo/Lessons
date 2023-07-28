# from tkinter import *
# window=Tk()
# # add widgets here
#
# window.title('Hello Python')
# window.geometry("300x200")
# window.mainloop()




from tkinter import *
window=Tk()

# add widgets here

# Inputs are a class
# Height is lines, width is character
input1 = Text(window,height=1, width=20)
input1.place( x= 80, y = 100)
# input1.get(1.0,'end-1c')

def example1(num):
    print(num)


def example2():
    label1.config(text="Changed")


def example3():
    label1.config(text=int(input1.get(1.0, 'end-1c'))**2)


# Buttons are a class
button1 = Button(window,text="Hello", command=lambda : example1("Hello"))
button1.place(x=80,y=0)

button2 = Button(window,text="Goodbye", command=example2)
button2.place(x=80,y=25)

button3 = Button(window,text="Square", command=example3)
button3.place(x=80,y=150)

# Labels are a class
label1 = Label(window,text="Start")
label1.place( x= 80, y = 50)



window.title('Hello Python')
window.geometry("300x300+555+220")
window.mainloop()



