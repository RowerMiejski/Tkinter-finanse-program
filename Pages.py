import tkinter as tk


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

    def packNewChanges(self):
        pass


class Expenses(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #new expenses data
        self.newExpenseCategory = tk.IntVar()
        self.newExpenseName = tk.StringVar()
        self.newExpenseDate = tk.StringVar()


        #looks
        label = tk.Label(self, text="Dodaj Finanse", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Wroc do strony startowej",
                           command=lambda: controller.showFrame("MainPage"))
        expenseButton = tk.Button(self, text="Dodaj nowy wydatek: ",
                           command=self.popupWindow)
        expenseShowLabel = tk.Label(self, textvariable = self.newExpenseName)
        button.pack()
        expenseButton.pack()
        expenseShowLabel.pack()

    def addExpense(self):
        self.controller.showFrame("MainPage")

    def addIncome(self):
        pass

    def showExpenses(self):
        pass

    def popupWindow(self):
        EntryForm(self, self.newExpenseName, self.newExpenseCategory, self.newExpenseDate)


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
    def __init__(self, master, exName, exCat, exDate):
        super().__init__(master)
        #recalls
        self.exName = exName
        self.exCat = exCat
        self.exDate = exDate

        self.geometry("300x300")
        label = tk.Label(self, text="Podaj nazwe wydatku: ")
        label.pack()
        self.nameEntry = tk.Entry(self)
        self.nameEntry.pack()

        tk.Button(self, text="submit", command=self.submit).pack()


    def submit(self):
        name = self.nameEntry.get()
        print(name)
        self.exName.set(name)
        self.destroy()
