from tkinter import Tk,ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        month = ttk.Label(master=self._root, text="November 2023")
        income_field = ttk.Label(master=self._root, text="Income")
        bills_field = ttk.Label(master=self._root, text="Bills")
        spending_field = ttk.Label(master=self._root, text="Spending")
        debt_field = ttk.Label(master=self._root, text="Debt")

        month.grid(row=0, column=0, columnspan=2)
        month.grid(padx=5, pady=10)
        income_field.grid(row=1, column=1, sticky=constants.W)
        bills_field.grid(row=2, column=1, sticky=constants.W)
        spending_field.grid(row=3, column=1, sticky=constants.W)
        debt_field.grid(row=4, column=1, sticky=constants.W)

window = Tk()
window.geometry("650x500")
window.title("EveryEuro")
ui = UI(window)
ui.start()

window.mainloop()
