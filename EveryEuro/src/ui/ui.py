from tkinter import Tk, ttk, constants, StringVar
import entities.month
import tkinter as tk

class UI:
    """ Application User Interface """

    def __init__(self, root):
        self._root = root
        #self._current_view = None  # Welcome View addition
        self._left_to_budget = None

    def start(self):
        #self._show_welcome_view()  # Welcome View

        # top row in the window that shows button links for all months
        top_months_frame = tk.Frame(master=self._root, relief=tk.RAISED, borderwidth=1)
        button_jan = tk.Button(master=top_months_frame, text="JAN")
        button_feb = tk.Button(master=top_months_frame, text="FEB")
        button_mar = tk.Button(master=top_months_frame, text="MAR")
        button_jan.grid(row=0, column=0)
        button_feb.grid(row=0, column=1)
        button_mar.grid(row=0, column=2)
        # add months Apr->Dec when Jan-Mar implemented and function properly
        top_months_frame.grid(row=0, column=0)

        # frame displaying chosen month
        frame_chosen_month = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        label_chosen_month = tk.Label(master=frame_chosen_month, text="chosen month")
        label_chosen_month.grid(row=1, column=0, sticky='w')
        frame_chosen_month.grid(row=1, column=0)

        # frame displaying left to budget
        frame_left_to_budget = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        frame_left_to_budget.grid(row=2, column=0)
        number_left_to_budget = StringVar()
        text_left_to_budget = StringVar()
        #number_left_to_budget = 0 #self.left_to_budget
        combined = "Left to budget: " + str(self._left_to_budget.get())
        #str(number_left_to_budget)
        text_left_to_budget.set(combined)
        label_left_to_budget = tk.Label(master=frame_left_to_budget,
                                        textvariable=text_left_to_budget)
        label_left_to_budget.grid(row=2, column=0, sticky='w')

        # main window frame displaying budgeting items
        frame_main = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        frame_main.grid(row=3, column=1)
        text_item_type = StringVar()
        text_item_type.set("TYPE")
        label_item_type = tk.Label(master=frame_main, textvariable=text_item_type)
        label_item_type.grid(row=3, column=0)
        text_planned_column = StringVar()
        text_planned_column.set("PLANNED")
        label_planned_column = tk.Label(master=frame_main, textvariable=text_planned_column)
        label_planned_column.grid(row=3, column=1)
        text_actual_column = StringVar()
        text_actual_column.set("ACTUAL")
        label_actual_column = tk.Label(master=frame_main, textvariable=text_actual_column)
        label_actual_column.grid(row=3, column=2)

        # TYPE column texts
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

        # PLANNED entry fields
        width_entry_field = 17
        number_planned_income = ttk.Entry(master=frame_main, width=width_entry_field)
        number_planned_bills = ttk.Entry(master=frame_main, width=width_entry_field)
        number_planned_spending = ttk.Entry(master=frame_main, width=width_entry_field)
        number_planned_debt = ttk.Entry(master=frame_main, width=width_entry_field)
        number_planned_income.grid(row=4, column=1, sticky="e")
        number_planned_bills.grid(row=5, column=1, sticky="e")
        number_planned_spending.grid(row=6, column=1, sticky="e")
        number_planned_debt.grid(row=7, column=1, sticky="e")
        button_calculate_balance = tk.Button(
            master=frame_main,
            text="Calculate balance",
            command=self.update_view(number_planned_income.get(), number_planned_bills.get(),
                                     number_planned_spending.get(), number_planned_debt.get())
        )
        button_calculate_balance.grid(row=8, column=1)

        # ACTUAL entry fields
        number_actual_income = tk.Entry(master=frame_main, width=width_entry_field)
        number_actual_bills = tk.Entry(master=frame_main, width=width_entry_field)
        number_actual_spending = tk.Entry(master=frame_main, width=width_entry_field)
        number_actual_debt = tk.Entry(master=frame_main, width=width_entry_field)
        number_actual_income.grid(row=4, column=2, sticky="e")
        number_actual_bills.grid(row=5, column=2, sticky="e")
        number_actual_spending.grid(row=6, column=2, sticky="e")
        number_actual_debt.grid(row=7, column=2, sticky="e")

    def update_view(self, income, bills, spending, debt):
        self.update_left_to_budget(entities.month.calculate_budget_balance(income, bills, spending, debt))

    def update_left_to_budget(self, budget_balance):
        #self.left_to_budget.set(str(budget_balance))
        self._left_to_budget = budget_balance

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
