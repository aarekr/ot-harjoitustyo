from tkinter import Tk, ttk, constants, StringVar, Menu, Label, Frame
import tkinter as tk
import entities.month as em
import services.service as service
import services.help_window as hp
from datetime import datetime

class UI:
    """ Application User Interface """

    def __init__(self, root):
        self._root = root

        # these values are retrieved and shown in the window when month buttons are clicked
        self._chosen_month = None
        self._chosen_month_left_to_budget = None
        self._chosen_month_planned_income = None        # salary, dividends, sale of assets etc.
        self._chosen_month_planned_rent = None          # rent or mortgage
        self._chosen_month_planned_bills = None         # electricty, phone, internet etc.
        self._chosen_month_planned_spending = None      # food, hobbies etc.
        self._chosen_month_planned_debt_service = None  # debt interest and repaiment
        self._chosen_month_planned_saving = None        # saving => this should change left_to_balance to 0

        self._chosen_month_receivedspent_income = None
        self._chosen_month_receivedspent_rent = None
        self._chosen_month_receivedspent_bills = None
        self._chosen_month_receivedspent_spending = None
        self._chosen_month_receivedspent_debt_service = None
        self._chosen_month_receivedspent_saving = None

        self.table_all_months_planned = service.create_all_months_table()
        self.table_all_months_receivedspent = service.create_all_months_table()

    def start(self):
        self._root.rowconfigure(4, weight=1)
        self._root.columnconfigure(2, weight=1)

        service.create_menu_bar(self._root)
        service.create_tool_bar(self._root)

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
        service.create_column_titles(frame_main)

        # CATEGORY column texts
        service.create_category_column_texts(frame_main)

        # PLANNED column entry fields
        width_entry_field = 16
        self._chosen_month_planned_income = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_rent = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_bills = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_spending = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_debt_service = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_saving = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_planned_income.grid(row=4, column=1, sticky="e")
        self._chosen_month_planned_rent.grid(row=5, column=1, sticky="e")
        self._chosen_month_planned_bills.grid(row=6, column=1, sticky="e")
        self._chosen_month_planned_spending.grid(row=7, column=1, sticky="e")
        self._chosen_month_planned_debt_service.grid(row=8, column=1, sticky="e")
        self._chosen_month_planned_saving.grid(row=9, column=1, sticky="e")
        # button for entering, changing and saving numbers for chosen month
        button_save_planned_figures = tk.Button(
            master=frame_main,
            text="Save planned",
            command=self.save_month_planned_figures
        )
        button_save_planned_figures.grid(row=10, column=1)

        # RECEIVED / SPENT column entry fields
        # under construction
        self._chosen_month_receivedspent_income = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_receivedspent_rent = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_receivedspent_bills = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_receivedspent_spending = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_receivedspent_debt_service = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_receivedspent_saving = tk.Entry(master=frame_main, width=width_entry_field)
        self._chosen_month_receivedspent_income.grid(row=4, column=2, sticky="e")
        self._chosen_month_receivedspent_rent.grid(row=5, column=2, sticky="e")
        self._chosen_month_receivedspent_bills.grid(row=6, column=2, sticky="e")
        self._chosen_month_receivedspent_spending.grid(row=7, column=2, sticky="e")
        self._chosen_month_receivedspent_debt_service.grid(row=8, column=2, sticky="e")
        self._chosen_month_receivedspent_saving.grid(row=9, column=2, sticky="e")
        button_save_receivedspent_figures = tk.Button(
            master=frame_main,
            text="Save rec./spent",
            command=self.save_month_receivedspent_figures
        )
        button_save_receivedspent_figures.grid(row=10, column=2)

    """def quit_program(self):  # this doesn't close the program for some reason
        ok_to_quit = askokcancel('Verify quit', 'Are you sure you want to quit?')
        print("ok_to_quit:", ok_to_quit)
        if ok_to_quit:
            self._root.quit"""

    def save_month_planned_figures(self):
        month_number = service.get_month_number_and_name(self._chosen_month.get())[0]
        income = str(0) if self._chosen_month_planned_income.get() == '' \
            else self._chosen_month_planned_income.get()
        rent = str(0) if self._chosen_month_planned_rent.get() == '' \
            else self._chosen_month_planned_rent.get()
        bills = str(0) if self._chosen_month_planned_bills.get() == '' \
            else self._chosen_month_planned_bills.get()
        spending = str(0) if self._chosen_month_planned_spending.get() == '' \
            else self._chosen_month_planned_spending.get()
        debt_service = str(0) if self._chosen_month_planned_debt_service.get() == '' \
            else self._chosen_month_planned_debt_service.get()
        saving = str(0) if self._chosen_month_planned_saving.get() == '' \
            else self._chosen_month_planned_saving.get()
        self.table_all_months_planned[month_number].set_income(int(income))
        self.table_all_months_planned[month_number].set_rent(int(rent))
        self.table_all_months_planned[month_number].set_bills(int(bills))
        self.table_all_months_planned[month_number].set_spending(int(spending))
        self.table_all_months_planned[month_number].set_debt_service(int(debt_service))
        self.table_all_months_planned[month_number].set_saving(int(saving))
        self._chosen_month_left_to_budget.set(service.calculate_left_to_budget(
            int(income), int(rent), int(bills), int(spending), int(debt_service), int(saving)))

    def save_month_receivedspent_figures(self):
        print("saving receivedspent figures")
        month_number = service.get_month_number_and_name(self._chosen_month.get())[0]
        income = str(0) if self._chosen_month_receivedspent_income.get() == '' \
            else self._chosen_month_receivedspent_income.get()
        rent = str(0) if self._chosen_month_receivedspent_rent.get() == '' \
            else self._chosen_month_receivedspent_rent.get()
        bills = str(0) if self._chosen_month_receivedspent_bills.get() == '' \
            else self._chosen_month_receivedspent_bills.get()
        spending = str(0) if self._chosen_month_receivedspent_spending.get() == '' \
            else self._chosen_month_receivedspent_spending.get()
        debt_service = str(0) if self._chosen_month_receivedspent_debt_service.get() == '' \
            else self._chosen_month_receivedspent_debt_service.get()
        saving = str(0) if self._chosen_month_receivedspent_saving.get() == '' \
            else self._chosen_month_receivedspent_saving.get()
        self.table_all_months_receivedspent[month_number].set_income(int(income))
        self.table_all_months_receivedspent[month_number].set_rent(int(rent))
        self.table_all_months_receivedspent[month_number].set_bills(int(bills))
        self.table_all_months_receivedspent[month_number].set_spending(int(spending))
        self.table_all_months_receivedspent[month_number].set_debt_service(int(debt_service))
        self.table_all_months_receivedspent[month_number].set_saving(int(saving))

    def get_chosen_month_data(self, month_number):
        print("get_chosen_month_data, month_number:", month_number)
        month_name = self.table_all_months_planned[month_number].get_month_name()
        income_planned = self.table_all_months_planned[month_number].get_income()
        rent_planned = self.table_all_months_planned[month_number].get_rent()
        bills_planned = self.table_all_months_planned[month_number].get_bills()
        spending_planned = self.table_all_months_planned[month_number].get_spending()
        debt_service_planned = self.table_all_months_planned[month_number].get_debt_service()
        saving_planned = self.table_all_months_planned[month_number].get_saving()
        left_to_budget = service.calculate_left_to_budget(income_planned, rent_planned,
            bills_planned, spending_planned, debt_service_planned, saving_planned)
        self._chosen_month.set(month_name)
        self._chosen_month_left_to_budget.set(left_to_budget)
        self._chosen_month_planned_income.delete(0, tk.END)
        self._chosen_month_planned_income.insert(0, income_planned)
        self._chosen_month_planned_rent.delete(0, tk.END)
        self._chosen_month_planned_rent.insert(0, rent_planned)
        self._chosen_month_planned_bills.delete(0, tk.END)
        self._chosen_month_planned_bills.insert(0, bills_planned)
        self._chosen_month_planned_spending.delete(0, tk.END)
        self._chosen_month_planned_spending.insert(0, spending_planned)
        self._chosen_month_planned_debt_service.delete(0, tk.END)
        self._chosen_month_planned_debt_service.insert(0, debt_service_planned)
        self._chosen_month_planned_saving.delete(0, tk.END)
        self._chosen_month_planned_saving.insert(0, saving_planned)

        self._chosen_month_receivedspent_income.delete(0, tk.END)
        self._chosen_month_receivedspent_income.insert(0,
            self.table_all_months_receivedspent[month_number].get_income())
        self._chosen_month_receivedspent_rent.delete(0, tk.END)
        self._chosen_month_receivedspent_rent.insert(0,
            self.table_all_months_receivedspent[month_number].get_rent())
        self._chosen_month_receivedspent_bills.delete(0, tk.END)
        self._chosen_month_receivedspent_bills.insert(0,
            self.table_all_months_receivedspent[month_number].get_bills())
        self._chosen_month_receivedspent_spending.delete(0, tk.END)
        self._chosen_month_receivedspent_spending.insert(0,
            self.table_all_months_receivedspent[month_number].get_spending())
        self._chosen_month_receivedspent_debt_service.delete(0, tk.END)
        self._chosen_month_receivedspent_debt_service.insert(0,
            self.table_all_months_receivedspent[month_number].get_debt_service())
        self._chosen_month_receivedspent_saving.delete(0, tk.END)
        self._chosen_month_receivedspent_saving.insert(0,
            self.table_all_months_receivedspent[month_number].get_saving())
