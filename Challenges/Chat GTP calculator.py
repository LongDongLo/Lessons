import tkinter as tk
from math import *

def evaluateExpression(expression):
    try:
        result = eval(expression)
    except:
        result = "Error"
    return result

def buttonPress(number):
    global expression
    expression = expression + str(number)
    equation.set(expression)

def equalPress():
    global expression
    result = evaluateExpression(expression)
    equation.set(result)
    expression = ""

def clearPress():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def sinPress():
    global expression
    expression = expression + "sin("
    equation.set(expression)

def cosPress():
    global expression
    expression = expression + "cos("
    equation.set(expression)

def tanPress():
    global expression
    expression = expression + "tan("
    equation.set(expression)

def logPress():
    global expression
    expression = expression + "log("
    equation.set(expression)

def sqrtPress():
    global expression
    expression = expression + "sqrt("
    equation.set(expression)

def piPress():
    global expression
    expression = expression + "pi"
    equation.set(expression)

def ePress():
    global expression
    expression = expression + "e"
    equation.set(expression)

def powerPress():
    global expression
    expression = expression + "**"
    equation.set(expression)

def factPress():
    global expression
    expression = expression + "!"
    equation.set(expression)

def modPress():
    global expression
    expression = expression + "%"
    equation.set(expression)

def leftPress():
    global expression
    expression = expression + "("
    equation.set(expression)

def rightPress():
    global expression
    expression = expression + ")"
    equation.set(expression)

def lnPress():
    global expression
    expression = expression + "log("
    equation.set(expression)

def expPress():
    global expression
    expression = expression + "exp("
    equation.set(expression)

# Tkinter GUI
root = tk.Tk()
root.title("Scientific Calculator")
root.configure(background="white")

expression = ""
equation = tk.StringVar()

calculation = tk.Entry(root, textvariable=equation, bg="white")
calculation.grid(columnspan=4, ipadx=70, pady=10, padx=10)

button1 = tk.Button(root, text="1", fg="black", bg="white", command=lambda: buttonPress(1), height=2, width=7)
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="2", fg="black", bg="white", command=lambda: buttonPress(2), height=2, width=7)
button2.grid(row=2, column=0)

root.geometry("300x300+555+220")
root.mainloop()
