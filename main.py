import tkinter as tk
from tkinter import font as tkfont
from Pages import *


class Faktury(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.frames = {}
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Expenses, MainPage, Settings):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="news")

        self.showFrame("MainPage")

    def showFrame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def addExpense(self):
        pass

    def addIncome(self):
        pass


if __name__ == "__main__":
    app = Faktury()
    app.mainloop()
