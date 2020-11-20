import tkinter as tk
from tkinter import font as tkfont
from Pages import *
import sqlite3


class Faktury(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.frames = {}
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1280x720")
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.categories = {}
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

        self.connectDataBase()
        self.getCategories()

    def showFrame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def addExpense(self):
        pass

    def addIncome(self):
        pass

    def connectDataBase(self):
        self.mydb = sqlite3.connect("db.db")
        self.cursor = self.mydb.cursor()
        self.cursor.execute('''CREATE TABLE if not exists expenses 
                               (price real, title text, category integer, date text)''')

        self.cursor.execute('''CREATE TABLE if not exists categories 
                                       (cat text)''')

        self.cursor.execute('SELECT * FROM categories')
        try:
            self.cursor.fetchall()[0][0]
        except:
            self.cursor.execute("INSERT INTO categories VALUES ('1-none')")
        self.cursor.execute('SELECT * FROM expenses')
        self.mydb.commit()
        return self.mydb

    def getCategories(self):
        self.cursor.execute('SELECT * FROM categories')
        categories = self.cursor.fetchall()
        for item in categories:
            names = item[0].split("-")
            self.categories[names[0]] = names[1]
        return self.categories


if __name__ == "__main__":
    app = Faktury()
    app.mainloop()
