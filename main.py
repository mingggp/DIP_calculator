import tkinter as tk    

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="heheheheh", font=("Arial", 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="Click here")
        self.button.place(x=20, y=80)
        self.button.pack()


        self.root.mainloop()

MyCalculator()