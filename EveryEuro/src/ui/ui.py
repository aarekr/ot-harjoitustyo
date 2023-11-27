from tkinter import Tk, ttk, constants, StringVar
import entities.month
import tkinter as tk

class UI:
    """ Application User Interface """

    def __init__(self, root):
        self._root = root
        #self._current_view = None  # Welcome View addition
        self._left_to_budget = None
        self._chosen_month = None

    def start(self):
        #self._show_welcome_view()  # Welcome View
        self.feb_mo = self.create_month_february("feb", 2456, 811, 567, 325)

        self._root.rowconfigure(4, weight=1)  # minsize=600
        self._root.columnconfigure(2, weight=1)

        # top row that shows button links for all months (navigation bar)
        frame_months_row = tk.Frame(master=self._root, relief=tk.RAISED, borderwidth=1)
        button_jan = tk.Button(master=frame_months_row, text="JAN", command=self.change_chosen_month)
        button_feb = tk.Button(master=frame_months_row, text="FEB")
        button_mar = tk.Button(master=frame_months_row, text="MAR")
        button_apr = tk.Button(master=frame_months_row, text="APR")
        button_may = tk.Button(master=frame_months_row, text="MAY")
        button_jun = tk.Button(master=frame_months_row, text="JUN")
        button_jul = tk.Button(master=frame_months_row, text="JUL")
        button_aug = tk.Button(master=frame_months_row, text="AUG")
        button_sep = tk.Button(master=frame_months_row, text="SEP")
        button_oct = tk.Button(master=frame_months_row, text="OCT")
        button_nov = tk.Button(master=frame_months_row, text="NOV")
        button_dec = tk.Button(master=frame_months_row, text="DEC")
        button_jan.grid(row=0, column=0)
        button_feb.grid(row=0, column=1)
        button_mar.grid(row=0, column=2)
        button_apr.grid(row=0, column=3)
        button_may.grid(row=0, column=4)
        button_jun.grid(row=0, column=5)
        button_jul.grid(row=0, column=6)
        button_aug.grid(row=0, column=7)
        button_sep.grid(row=0, column=8)
        button_oct.grid(row=0, column=9)
        button_nov.grid(row=0, column=10)
        button_dec.grid(row=0, column=11)
        frame_months_row.grid(row=0, column=0, columnspan=4, pady=10)

        # frame displaying chosen month
        frame_chosen_month = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        self._chosen_month = StringVar()
        self._chosen_month.set("NOVEMBER")
        label_chosen_month = tk.Label(master=frame_chosen_month, textvariable=self._chosen_month)
        label_chosen_month.grid(row=1, column=0)
        frame_chosen_month.grid(row=1, column=0, sticky='w', padx=10)

        # frame displaying left to budget
        frame_left_to_budget = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        frame_left_to_budget.grid(row=2, column=0)
        self._left_to_budget = StringVar()
        text_left_to_budget = StringVar()
        self._left_to_budget.set("0")
        text_left_to_budget.set("Left to budget:")
        label_text_left_to_budget = tk.Label(master=frame_left_to_budget,
                                        textvariable=text_left_to_budget)
        label_number_left_to_budget = tk.Label(master=frame_left_to_budget,
                                        textvariable=self._left_to_budget)
        label_text_left_to_budget.grid(row=2, column=0, sticky='w', columnspan=1, padx=10)
        label_number_left_to_budget.grid(row=2, column=1, sticky='e')

        # main window frame displaying budgeting items
        frame_main = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        frame_main.grid(row=3, column=1, padx=10, pady=10)
        text_item_category = StringVar()
        text_item_category.set("CATEGORY")
        label_item_category = tk.Label(master=frame_main, textvariable=text_item_category)
        label_item_category.grid(row=3, column=0, sticky="w")
        text_planned_column = StringVar()
        text_planned_column.set("PLANNED")
        label_planned_column = tk.Label(master=frame_main, textvariable=text_planned_column)
        label_planned_column.grid(row=3, column=1)
        text_receivedspent_column = StringVar()
        text_receivedspent_column.set("RECEIVED / SPENT")
        label_receivedspent_column = tk.Label(master=frame_main, textvariable=text_receivedspent_column)
        label_receivedspent_column.grid(row=3, column=2)

        # CATEGORY column texts
        text_income = StringVar()
        text_bills = StringVar()
        text_spending = StringVar()
        text_debt = StringVar()
        text_income.set("Income")
        text_bills.set("Bills")
        text_spending.set("Spending  ")
        text_debt.set("Debt")
        label_income = tk.Label(master=frame_main, textvariable=text_income)
        label_bills = tk.Label(master=frame_main, textvariable=text_bills)
        label_spending = tk.Label(master=frame_main, textvariable=text_spending)
        label_debt = tk.Label(master=frame_main, textvariable=text_debt)
        label_income.grid(row=4, column=0, sticky="w")
        label_bills.grid(row=5, column=0, sticky="w")
        label_spending.grid(row=6, column=0, sticky="w")
        label_debt.grid(row=7, column=0, sticky="w")

        # PLANNED column entry fields
        width_entry_field = 17
        entry_planned_income = ttk.Entry(master=frame_main, width=width_entry_field)
        entry_planned_bills = ttk.Entry(master=frame_main, width=width_entry_field)
        entry_planned_spending = ttk.Entry(master=frame_main, width=width_entry_field)
        entry_planned_debt = ttk.Entry(master=frame_main, width=width_entry_field)
        entry_planned_income.grid(row=4, column=1, sticky="e")
        entry_planned_bills.grid(row=5, column=1, sticky="e")
        entry_planned_spending.grid(row=6, column=1, sticky="e")
        entry_planned_debt.grid(row=7, column=1, sticky="e")
        button_calculate_balance = ttk.Button(
            master=frame_main,
            text="Calculate balance",
            #command=self.calculate_budget_balance(2000, 800, 500, 300)
            command=self.update_left_to_budget
        )
        button_calculate_balance.grid(row=8, column=1)

        # RECEIVED / SPENT column entry fields
        entry_receivedspent_income = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_bills = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_spending = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_debt = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_income.grid(row=4, column=2, sticky="e")
        entry_receivedspent_bills.grid(row=5, column=2, sticky="e")
        entry_receivedspent_spending.grid(row=6, column=2, sticky="e")
        entry_receivedspent_debt.grid(row=7, column=2, sticky="e")

    def calculate_budget_balance(self, income):
        print("budget balance, income:", income)
    
    def update_left_to_budget(self):
        print("updating left_to_balance")
        self._left_to_budget.set(str(123))

    def change_chosen_month(self):
        print("changing month to JAN:", self._chosen_month.get())
        self._chosen_month.set("JANUARY")
        print("self._chosen_month is now:", self._chosen_month.get())
        print("february:")

    def create_month_february(self, month_name, income, bills, spending, debt):
        feb = entities.month.Month(month_name, income, bills, spending, debt)

    """def _show_welcome_view(self):  # Welcome View
        self._current_view = WelcomeView(self._root)
        self._current_view.pack()"""


"""class WelcomeView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.Y)
    
    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Welcome to EveryEuro budgeting!")
        button = ttk.Button(
            master=self._frame,
            text="Let's start",
            command=self.destroy
        )
        label.grid(row=0, column=0)
        button.grid(row=1, column=0)"""
