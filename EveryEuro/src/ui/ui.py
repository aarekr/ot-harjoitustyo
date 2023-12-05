from tkinter import Tk, ttk, constants, StringVar, Menu, Label, Frame
from tkinter.messagebox import *
import entities.month as em
import services.service as service
import tkinter as tk
from datetime import datetime

class UI:
    """ Application User Interface """

    def __init__(self, root):
        self._root = root

        # these values are retrieved and shown in the window when month buttons are clicked
        self._chosen_month = None
        self._chosen_month_left_to_budget = None
        self._chosen_month_planned_income = None
        self._chosen_month_planned_bills = None
        self._chosen_month_planned_spending = None
        self._chosen_month_planned_debt = None

        # testing: creating all months together
        self.table_all_months = ["empty cell"]  # empty cell in index 0
        self.create_all_months_table()

    def start(self):
        self.create_menu_bar()
        self.create_tool_bar()

        self._root.rowconfigure(4, weight=1)  # minsize=600
        self._root.columnconfigure(2, weight=1)

        # top row that shows button links for all months (navigation bar)
        # refactor this part so that it is shorter
        frame_months_row = tk.Frame(master=self._root, relief=tk.RAISED, borderwidth=1)
        button_jan = tk.Button(master=frame_months_row, text="JAN",
                                command=(lambda: self.get_chosen_month_data(1)))
        button_feb = tk.Button(master=frame_months_row, text="FEB",
                                command=(lambda: self.get_chosen_month_data(2)))
        button_mar = tk.Button(master=frame_months_row, text="MAR",
                                command=(lambda: self.get_chosen_month_data(3)))
        button_apr = tk.Button(master=frame_months_row, text="APR",
                                command=(lambda: self.get_chosen_month_data(4)))
        button_may = tk.Button(master=frame_months_row, text="MAY",
                                command=(lambda: self.get_chosen_month_data(5)))
        button_jun = tk.Button(master=frame_months_row, text="JUN",
                                command=(lambda: self.get_chosen_month_data(6)))
        button_jul = tk.Button(master=frame_months_row, text="JUL",
                                command=(lambda: self.get_chosen_month_data(7)))
        button_aug = tk.Button(master=frame_months_row, text="AUG",
                                command=(lambda: self.get_chosen_month_data(8)))
        button_sep = tk.Button(master=frame_months_row, text="SEP",
                                command=(lambda: self.get_chosen_month_data(9)))
        button_oct = tk.Button(master=frame_months_row, text="OCT",
                                command=(lambda: self.get_chosen_month_data(10)))
        button_nov = tk.Button(master=frame_months_row, text="NOV",
                                command=(lambda: self.get_chosen_month_data(11)))
        button_dec = tk.Button(master=frame_months_row, text="DEC",
                                command=(lambda: self.get_chosen_month_data(12)))
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
        self._chosen_month.set(service.get_month_name(datetime.now().month))  # e.g. 12 = December
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
        # button for entering and saving numbers for a new month
        button_save_figures = ttk.Button(
            master=frame_main,
            text="Save figures",
            command=self.set_month_figures
        )
        button_save_figures.grid(row=8, column=1)
        """button_quit = ttk.Button(  # button de-activated
            master=frame_main,
            text="Quit",
            command=self._root.quit  # self.quit_program
        )
        button_quit.grid(row=9, column=2)"""

        # RECEIVED / SPENT column entry fields
        entry_receivedspent_income = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_bills = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_spending = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_debt = tk.Entry(master=frame_main, width=width_entry_field)
        entry_receivedspent_income.grid(row=4, column=2, sticky="e")
        entry_receivedspent_bills.grid(row=5, column=2, sticky="e")
        entry_receivedspent_spending.grid(row=6, column=2, sticky="e")
        entry_receivedspent_debt.grid(row=7, column=2, sticky="e")

    """def quit_program(self):  # this doesn't close the program for some reason
        ok_to_quit = askokcancel('Verify quit', 'Are you sure you want to quit?')
        print("ok_to_quit:", ok_to_quit)
        if ok_to_quit:
            self._root.quit"""

    def create_all_months_table(self):
        # move this to service.py
        # in the final version all 4 values below should be 0, current values while developing
        income = 2000
        bills = 800
        spending = 500
        debt = 600
        for i in range(1, 13):
            month_name = service.get_month_name(i)
            print("for loop i & month_name:", i, month_name)
            created_month = em.Month(month_name, income+i, bills+i, spending+i, debt+i)
            self.table_all_months.append(created_month)

    def set_month_figures(self):
        print("saving this month's figures")
        # under construction
        month_number = service.get_month_number_and_name(self._chosen_month.get())[0]
        self.table_all_months[month_number].set_income(self._chosen_month_planned_income)

    def get_chosen_month(self):
        return self._chosen_month

    def get_chosen_month_data(self, month_number):
        print("get_chosen_month_data, month_number:", month_number)
        month_name = self.table_all_months[month_number].get_month_name()
        income = self.table_all_months[month_number].get_income()
        bills = self.table_all_months[month_number].get_bills()
        spending = self.table_all_months[month_number].get_spending()
        debt = self.table_all_months[month_number].get_debt()
        left_to_budget = service.calculate_left_to_budget(income, bills, spending, debt)
        print("table_all_months name  :", month_name)
        print("table_all_months income:", income)
        self._chosen_month.set(month_name)
        self._chosen_month_left_to_budget.set(left_to_budget)
        self._chosen_month_planned_income.delete(0, tk.END)
        self._chosen_month_planned_income.insert(0, income)
        self._chosen_month_planned_bills.delete(0, tk.END)
        self._chosen_month_planned_bills.insert(0, bills)
        self._chosen_month_planned_spending.delete(0, tk.END)
        self._chosen_month_planned_spending.insert(0, spending)
        self._chosen_month_planned_debt.delete(0, tk.END)
        self._chosen_month_planned_debt.insert(0, debt)

    def create_menu_bar(self):
        top = Menu(self._root)
        self._root.config(menu=top)
        file = Menu(top, tearoff=False)
        file.add_command(label='Open...', command=service.bar_item_notdone, underline=0)
        file.add_separator()
        file.add_command(label='Quit', command=self._root.quit, underline=0)
        top.add_cascade(label='File', menu=file, underline=0)

        help_menu = Menu(top, tearoff=False)
        help_menu.add_command(label='Help', command=self.open_help_window, underline=0)
        top.add_cascade(label='Help', menu=help_menu, underline=0)

    def create_tool_bar(self):
        toolbar_left_side = tk.Frame(master=self._root, cursor='hand2', relief=tk.SUNKEN, borderwidth=1)
        toolbar_center = tk.Frame(master=self._root, cursor='hand2', relief=tk.SUNKEN, borderwidth=1)
        toolbar_right_side = tk.Frame(master=self._root, cursor='hand2', relief=tk.SUNKEN, borderwidth=1)
        toolbar_left_side.grid(row=25, column=0)
        toolbar_center.grid(row=25, column=1)
        toolbar_right_side.grid(row=25, column=2, sticky='e')
        tk.Button(toolbar_left_side, text='Year overview', command=service.bar_item_notdone).pack(side=tk.LEFT)
        tk.Button(toolbar_center, text='Open', command=service.bar_item_notdone).pack(side=tk.LEFT)
        tk.Button(toolbar_center, text='Help', command=self.open_help_window).pack(side=tk.LEFT)
        tk.Button(toolbar_right_side, text='Quit', command=self._root.quit).pack(side=tk.RIGHT)

    def open_help_window(self):
        print("opening help window")
        help_window_text_field = tk.Text(master=self._root, width=75, height=7)
        help_window_text_field.insert("1.0", "HELP - how to use the program")
        help_window_text_field.insert("2.0", "\nEnter your income and expenses in respective fields.")
        help_window_text_field.insert("3.0", "\nClick 'Save figures' to save figures.")
        nav_text = "\nNavigate between months by clicking the month buttons on top of the window."
        help_window_text_field.insert("4.0", nav_text)
        help_window_text_field.insert("5.0", "Left to budget shows how much you have left to allocate.")
        help_window_text_field.place(x=30, y=300)
        # add button for help_window closing
