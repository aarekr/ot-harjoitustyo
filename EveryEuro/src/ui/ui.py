from tkinter import Tk, ttk, constants, StringVar
import entities.month
import tkinter as tk
from datetime import datetime

class UI:
    """ Application User Interface """

    def __init__(self, root):
        self._root = root
        #self._current_view = None  # Welcome View addition

        # these values are retrieved and shown in the window when month buttons are clicked
        self._chosen_month = None
        self._chosen_month_left_to_budget = None
        self._chosen_month_planned_income = None
        self._chosen_month_planned_bills = None
        self._chosen_month_planned_spending = None
        self._chosen_month_planned_debt = None

        # creating months march and april
        self.march = self.create_month_march("MARCH", 3003, 1003, 303, 333)
        self.april = self.create_month_april("APRIL", 4004, 1004, 404, 444)
        # testing: creating all months together
        """table_all_months = []
        income = 2000
        bills = 800
        spending = 500
        debt = 600
        for i in range(1, 13):
            if i == 3 or i == 4:
                continue
            month_name = self.get_current_month(i)
            created_month = entities.month.Month(month_name, income+i, bills+i, spending+i, debt+i)
            table_all_months.append(created_month)"""

    def start(self):
        #self._show_welcome_view()  # Welcome View

        self._root.rowconfigure(4, weight=1)  # minsize=600
        self._root.columnconfigure(2, weight=1)

        # top row that shows button links for all months (navigation bar)
        frame_months_row = tk.Frame(master=self._root, relief=tk.RAISED, borderwidth=1)
        button_jan = tk.Button(master=frame_months_row, text="JAN", command=self.change_chosen_month)
        button_feb = tk.Button(master=frame_months_row, text="FEB")
        button_mar = tk.Button(master=frame_months_row, text="MAR", command=self.get_march_data)
        button_apr = tk.Button(master=frame_months_row, text="APR", command=self.get_april_data)
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

        # frame (top left) displaying chosen month
        frame_chosen_month = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        self._chosen_month = StringVar()
        self._chosen_month.set(self.get_current_month(datetime.now().month))  # e.g. 12 = December
        label_chosen_month = tk.Label(master=frame_chosen_month, textvariable=self._chosen_month)
        label_chosen_month.grid(row=1, column=0)
        frame_chosen_month.grid(row=1, column=0, sticky='w', padx=10)

        # frame (top left) displaying 'left to budget'
        frame_left_to_budget = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        frame_left_to_budget.grid(row=2, column=0)
        self._chosen_month_left_to_budget = StringVar()
        text_left_to_budget = StringVar()
        self._chosen_month_left_to_budget.set("0")
        text_left_to_budget.set("Left to budget:")
        label_text_left_to_budget = tk.Label(master=frame_left_to_budget,
                                        textvariable=text_left_to_budget)
        label_number_left_to_budget = tk.Label(master=frame_left_to_budget,
                                        textvariable=self._chosen_month_left_to_budget)
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
        self._chosen_month_planned_income = ttk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_bills = ttk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_spending = ttk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_debt = ttk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_income.grid(row=4, column=1, sticky="e")
        self._chosen_month_planned_bills.grid(row=5, column=1, sticky="e")
        self._chosen_month_planned_spending.grid(row=6, column=1, sticky="e")
        self._chosen_month_planned_debt.grid(row=7, column=1, sticky="e")
        # this button is needed when entering numbers for a new month
        button_calculate_balance = ttk.Button(
            master=frame_main,
            text="Calculate balance",
            command=self.update_left_to_budget
        )
        button_calculate_balance.grid(row=8, column=1)
        button_quit = ttk.Button(
            master=frame_main,
            text="Quit",
            command=self._root.quit
        )
        button_quit.grid(row=9, column=2)

        # RECEIVED / SPENT column entry fields
        entry_receivedspent_income = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_bills = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_spending = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_debt = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_income.grid(row=4, column=2, sticky="e")
        entry_receivedspent_bills.grid(row=5, column=2, sticky="e")
        entry_receivedspent_spending.grid(row=6, column=2, sticky="e")
        entry_receivedspent_debt.grid(row=7, column=2, sticky="e")

    def update_left_to_budget(self):
        print("updating _chosen_month_left_to_budget")
        # fix this so that it calculates correct left_to_budget
        self._chosen_month_left_to_budget.set(str(123))

    def get_chosen_month(self):
        return self._chosen_month

    def change_chosen_month(self):
        print("changing month to JAN from:", self._chosen_month.get())
        self._chosen_month.set("JANUARY")
        print("self._chosen_month is now:", self._chosen_month.get())

    def get_current_month(self, current_month):
        all_months = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                        "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        return all_months[current_month]

    # March and April below are hard coded but should be handled in the same functions
    def create_month_march(self, month_name, income, bills, spending, debt):
        march = entities.month.Month(month_name, income, bills, spending, debt)
        return march

    def create_month_april(self, month_name, income, bills, spending, debt):
        april = entities.month.Month(month_name, income, bills, spending, debt)
        return april

    def get_march_data(self):
        self._chosen_month.set("MARCH")
        income = self.march.get_income()
        bills = self.march.get_bills()
        spending = self.march.get_spending()
        debt = self.march.get_debt()
        budget_balance = entities.month.calculate_budget_balance(income, bills, spending, debt)
        self._chosen_month_left_to_budget.set(budget_balance)
        self._chosen_month_planned_income.delete(0, tk.END)
        self._chosen_month_planned_income.insert(0, income)
        self._chosen_month_planned_bills.delete(0, tk.END)
        self._chosen_month_planned_bills.insert(0, bills)
        self._chosen_month_planned_spending.delete(0, tk.END)
        self._chosen_month_planned_spending.insert(0, spending)
        self._chosen_month_planned_debt.delete(0, tk.END)
        self._chosen_month_planned_debt.insert(0, debt)

    def get_april_data(self):
        self._chosen_month.set("APRIL")
        income = self.april.get_income()
        bills = self.april.get_bills()
        spending = self.april.get_spending()
        debt = self.april.get_debt()
        budget_balance = entities.month.calculate_budget_balance(income, bills, spending, debt)
        self._chosen_month_left_to_budget.set(budget_balance)
        self._chosen_month_planned_income.delete(0, tk.END)
        self._chosen_month_planned_income.insert(0, income)
        self._chosen_month_planned_bills.delete(0, tk.END)
        self._chosen_month_planned_bills.insert(0, bills)
        self._chosen_month_planned_spending.delete(0, tk.END)
        self._chosen_month_planned_spending.insert(0, spending)
        self._chosen_month_planned_debt.delete(0, tk.END)
        self._chosen_month_planned_debt.insert(0, debt)
