from tkinter import *
import tkinter as tk

def clear():
    global expression
    global label_show
    result="0"
    expression=" "
    label_show.set(result)

def press(number):
    global expression
    global label_show
    expression=expression+number
    label_show.set(expression)

def equal():
    try:
        global expression
        global label_show
        result=str(eval(expression))
        label_show.set(result)
    except:
        result="ERROR"
        expression=" "
    label_show.set(result)

root = tk.Tk()
root.title("Calculator 1.0")
root.option_add("*Font", "tahoma 25")
root.resizable(0, 0)

label_show=tk.StringVar()
expression=""
label_show.set(expression)
label_show.set(0)

tk.Label(root, text="   ", bg="mediumturquoise", width=7).grid(row=0, column=0, columnspan=4, sticky="NEWS", padx=20, pady=(20, 10), ipadx=20, ipady=10)
tk.Button(root, text="Clear", bg="tomato", width=3, command=clear).grid(row=1, columnspan=2, sticky="NEWS", padx=20, pady=(10, 10))

tk.Button(root, text=".", bg="powderblue", width=4, command=lambda: press(".")).grid(row=5, column=0, sticky="NEWS", padx=(20, 0))
tk.Button(root, text="0", bg="powderblue", width=4, command=lambda: press("0")).grid(row=5, column=1, sticky="NEWS")
tk.Button(root, text="00", bg="powderblue", width=4, command=lambda: press("00")).grid(row=5, column=2, sticky="NEWS")
tk.Button(root, text="1", bg="powderblue", width=4, command=lambda: press("1")).grid(row=4, column=0, sticky="NEWS", padx=(20, 0))
tk.Button(root, text="2", bg="powderblue", width=4, command=lambda: press("2")).grid(row=4, column=1, sticky="NEWS")
tk.Button(root, text="3", bg="powderblue", width=4, command=lambda: press("3")).grid(row=4, column=2, sticky="NEWS")
tk.Button(root, text="4", bg="powderblue", width=4, command=lambda: press("4")).grid(row=3, column=0, sticky="NEWS", padx=(20, 0))
tk.Button(root, text="5", bg="powderblue", width=4, command=lambda: press("5")).grid(row=3, column=1, sticky="NEWS")
tk.Button(root, text="6", bg="powderblue", width=4, command=lambda: press("6")).grid(row=3, column=2, sticky="NEWS")
tk.Button(root, text="7", bg="powderblue", width=4, command=lambda: press("7")).grid(row=2, column=0, sticky="NEWS", padx=(20, 0))
tk.Button(root, text="8", bg="powderblue", width=4, command=lambda: press("8")).grid(row=2, column=1, sticky="NEWS")
tk.Button(root, text="9", bg="powderblue", width=4, command=lambda: press("9")).grid(row=2, column=2, sticky="NEWS")

tk.Button(root, text="+", bg="gold", width=4, command=lambda: press("+")).grid(row=2, column=3, sticky="NEWS", padx=(0, 20))
tk.Button(root, text="-", bg="gold", width=4, command=lambda: press("-")).grid(row=3, column=3, sticky="NEWS", padx=(0, 20))
tk.Button(root, text="x", bg="gold", width=4, command=lambda: press("x")).grid(row=4, column=3, sticky="NEWS", padx=(0, 20))
tk.Button(root, text="%", bg="gold", width=4, command=lambda: press("%")).grid(row=5, column=3, sticky="NEWS", padx=(0, 20))
tk.Button(root, text="=", bg="lawngreen", width=3, command=equal).grid(row=6, columnspan=4, sticky="NEWS", padx=(20, 20), pady=(0, 20))

root.mainloop()