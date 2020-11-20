import tkinter as tk
from tkinter import ttk
import sqlite3

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Finanse", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Dodaj fakture",
                            command=lambda: controller.showFrame("Expenses"))
        button2 = tk.Button(self, text="Ustawienia",
                            command=lambda: controller.showFrame("Settings"))
        button1.pack()
        button2.pack()
        myData = tk.LabelFrame(self, text = "Wydatki, dochody")
        myData.pack(fill = "both", expand = "yes", padx=20,pady=10)
        trv = ttk.Treeview(myData, columns = (1,2,3,4), show = "headings", height = "6")
        trv.pack()
        trv.heading(1, text= "Wartość")
        trv.heading(2, text= "Tytuł")
        trv.heading(3, text= "Kategoria")
        trv.heading(4, text= "Data")
        self.db = sqlite3.connect("db.db")
        self.cursor = self.db.cursor()

    def packNewChanges(self):
        pass


class Expenses(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.db = self.controller.connectDataBase()
        self.cursor = self.db.cursor()
        #new expenses data
        self.newExpenseCategory = tk.StringVar()
        self.newExpenseName = tk.StringVar()
        self.newExpenseDate = tk.StringVar()
        self.newExpensePrice = tk.IntVar()

        #looks
        label = tk.Label(self, text="Dodaj Finanse", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Wroc do strony startowej",
                           command=lambda: controller.showFrame("MainPage"))
        expenseButton = tk.Button(self, text="Dodaj nowy wydatek: ",
                           command=self.popupWindow)
        expenseShowLabel = tk.Label(self, textvariable = self.newExpensePrice)
        button.pack()
        expenseButton.pack()
        expenseShowLabel.pack()

    def addExpense(self):
        self.cursor.execute("INSERT INTO expenses VALUES (?,?,?,?)", (self.newExpensePrice.get(), self.newExpenseName.get(), self.newExpenseCategory.get(), self.newExpenseDate.get()))
        self.db.commit()

    def addIncome(self):
        pass

    def showExpenses(self):
        pass

    def popupWindow(self):
        EntryForm(self,self.newExpensePrice, self.newExpenseName, self.newExpenseCategory, self.newExpenseDate)


class Settings(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Ustawienia", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Strona startowa",
                           command=lambda: controller.showFrame("MainPage"))
        button.pack()



class EntryForm(tk.Toplevel):
    def __init__(self, master,exPrice, exName, exCat, exDate):
        super().__init__(master)
        self.dict = {}
        self.dict = self.master.controller.getCategories()
        #recalls
        self.exName = exName
        self.exCat = exCat
        self.exDate = exDate
        self.exPrice = exPrice
        self.geometry("300x300")
        #looks
        self.getEntries()
        tk.Button(self, text="submit", command=self.submit).pack()

    def getEntries(self):
        nameLabel = tk.Label(self, text="Podaj nazwe wydatku: ")
        nameLabel.pack()
        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()

        costLabel = tk.Label(self, text="Podaj koszt wydatku: ")
        costLabel.pack()
        self.costEntry = tk.Entry(self)
        self.costEntry.pack()

        catLabel = tk.Label(self, text="Podaj kategorie wydatku: ")
        catLabel.pack()
        self.catEntry = ttk.Combobox(self, textvariable = self.exCat)
        self.catEntry['values'] = list(self.dict.values())
        self.catEntry.current(0)
        self.catEntry.pack()

        dateLabel = tk.Label(self, text="Podaj date wydatku: ")
        dateLabel.pack()
        self.dateEntry = tk.Entry(self)
        self.dateEntry.pack()

    def submit(self):
        self.exName.set(self.nameEntry.get())
        self.exPrice.set(self.costEntry.get())
        self.exCat.set(self.catEntry.get())
        self.exDate.set(self.dateEntry.get())
        self.master.addExpense()
        self.destroy()
