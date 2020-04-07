# Program for simple calculator
from math import *
from tkinter import *

expression = ""


def error():
    global expression
    equation.set("Syntax Error")
    expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def backclear():
    global expression
    expression = expression[:len(expression) - 1]
    equation.set(expression)


def PressEqual():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except ZeroDivisionError:
        equation.set("Divide by 0 Error")
        expression = ""
    except Exception:
        error()


def Sqrt():
    try:
        global expression
        equation.set(sqrt(int(equation.get())))
        expression = ""
    except:
        error()


def Square():
    try:
        global expression
        equation.set(int(pow(int(equation.get()), 2)))
        expression = ""
    except:
        error()


def Press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


if __name__ == "__main__":
    root = Tk()
    root.geometry("200x182")
    root.title("Cal")
    root["bg"] = "Grey"
    equation = StringVar()
    root.resizable(0, 0)
    InputField = Entry(root, width=33, textvar=equation).grid(columnspan=4, row=1)
    Button(root, text="x \N{SUPERSCRIPT TWO}", width=2, font=("bold", 11), command=lambda: Square()).grid(row=2,
                                                                                                          column=0,
                                                                                                          ipadx=8,
                                                                                                          pady=3)
    Button(root, text="Sqrt", width=2, font=("bold", 11), command=lambda: Sqrt()).grid(row=2, column=1, ipadx=8, pady=3)
    Button(root, text=" CE ", width=2, bg="red", fg="white", font=("bold", 11), command=lambda: backclear()).grid(row=2,
                                                                                                                  column=3,
                                                                                                                  ipadx=8,
                                                                                                                  pady=3)
    Button(root, text=" C ", width=2, bg="red", fg="white", font=("bold", 11), command=lambda: clear()).grid(row=2,
                                                                                                             column=2,
                                                                                                             ipadx=8,
                                                                                                             pady=3)
    Button(root, text=" 1 ", width=2, command=lambda: Press(1)).grid(row=3, column=0, ipadx=11, pady=3)
    Button(root, text=" 2 ", width=2, command=lambda: Press(2)).grid(row=3, column=1, ipadx=11)
    Button(root, text=" 3 ", width=2, command=lambda: Press(3)).grid(row=3, column=2, ipadx=11)
    Button(root, text=" + ", width=2, command=lambda: Press(" + ")).grid(row=3, column=3, ipadx=11)
    Button(root, text=" 4 ", width=2, command=lambda: Press(4)).grid(row=4, column=0, ipadx=11, pady=3)
    Button(root, text=" 5 ", width=2, command=lambda: Press(5)).grid(row=4, column=1, ipadx=11)
    Button(root, text=" 6 ", width=2, command=lambda: Press(6)).grid(row=4, column=2, ipadx=11)
    Button(root, text=" - ", width=2, command=lambda: Press(" - ")).grid(row=4, column=3, ipadx=11)
    Button(root, text=" 7 ", width=2, command=lambda: Press(7)).grid(row=5, column=0, ipadx=11, pady=3)
    Button(root, text=" 8 ", width=2, command=lambda: Press(8)).grid(row=5, column=1, ipadx=11)
    Button(root, text=" 9 ", width=2, command=lambda: Press(9)).grid(row=5, column=2, ipadx=11)
    Button(root, text=" x ", width=2, command=lambda: Press(" * ")).grid(row=5, column=3, ipadx=11)
    Button(root, text=" / ", width=2, command=lambda: Press(" / ")).grid(row=6, column=0, ipadx=11, pady=3)
    Button(root, text=" 0 ", width=2, command=lambda: Press(0)).grid(row=6, column=1, ipadx=11)
    Button(root, text=" . ", width=2, command=lambda: Press(" . ")).grid(row=6, column=2, ipadx=11)
    Button(root, text=" = ", width=2, command=lambda: PressEqual()).grid(row=6, column=3, ipadx=11)
root.mainloop()
