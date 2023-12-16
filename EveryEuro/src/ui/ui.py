""" User Interface """

from tkinter import Tk, ttk, constants, StringVar, Menu, Label, Frame, Button, LEFT, RIGHT, SUNKEN
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ui.ui_helper as ui_helper
import services.service as service
import entities.month
from datetime import datetime

class UI:
    """ Class that handles application user interface. """

    def __init__(self, root):
        """ Class constructor that creates the user interface. """
        self._root = root
        self._root.rowconfigure(4, weight=1)
        self._root.columnconfigure(2, weight=1)

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

    def start(self):
        """Starts the user interface.
           Creates layout, menu bar, toolbar, buttons, texts, entry fields for numbers.
           Creates two tables for keeping planned and received/spent figures with default values 0.
        """
        ui_helper.create_menu_bar(self._root)
        #ui_helper.create_tool_bar(self._root)
        self.create_tool_bar()

        self.create_frame_month_button_row(self._root)
        self.create_frame_chosen_month(self._root)
        self.create_frame_left_to_budget(self._root)
        self.create_frame_main(self._root)

        self.table_all_months_planned = service.create_all_months_table()
        self.table_all_months_receivedspent = service.create_all_months_table()

    def create_frame_month_button_row(self, root):
        """ Creating frame and month buttons on top row of the window. """
        # refactor this part so that it is shorter?
        frame_months_row = tk.Frame(master=root, relief=tk.RAISED, borderwidth=1)
        button_jan = tk.Button(master=frame_months_row, text="JAN",
                                command=(lambda: self.get_and_display_chosen_month_data(1)))
        button_feb = tk.Button(master=frame_months_row, text="FEB",
                                command=(lambda: self.get_and_display_chosen_month_data(2)))
        button_mar = tk.Button(master=frame_months_row, text="MAR",
                                command=(lambda: self.get_and_display_chosen_month_data(3)))
        button_apr = tk.Button(master=frame_months_row, text="APR",
                                command=(lambda: self.get_and_display_chosen_month_data(4)))
        button_may = tk.Button(master=frame_months_row, text="MAY",
                                command=(lambda: self.get_and_display_chosen_month_data(5)))
        button_jun = tk.Button(master=frame_months_row, text="JUN",
                                command=(lambda: self.get_and_display_chosen_month_data(6)))
        button_jul = tk.Button(master=frame_months_row, text="JUL",
                                command=(lambda: self.get_and_display_chosen_month_data(7)))
        button_aug = tk.Button(master=frame_months_row, text="AUG",
                                command=(lambda: self.get_and_display_chosen_month_data(8)))
        button_sep = tk.Button(master=frame_months_row, text="SEP",
                                command=(lambda: self.get_and_display_chosen_month_data(9)))
        button_oct = tk.Button(master=frame_months_row, text="OCT",
                                command=(lambda: self.get_and_display_chosen_month_data(10)))
        button_nov = tk.Button(master=frame_months_row, text="NOV",
                                command=(lambda: self.get_and_display_chosen_month_data(11)))
        button_dec = tk.Button(master=frame_months_row, text="DEC",
                                command=(lambda: self.get_and_display_chosen_month_data(12)))
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

    def create_frame_chosen_month(self, root):
        """ Creating frame (top left) that displays the chosen month name. """
        frame_chosen_month = tk.Frame(master=root, relief=tk.FLAT, borderwidth=1)
        self._chosen_month = StringVar()
        self._chosen_month.set(service.get_month_name(datetime.now().month))  # e.g. 12 = December
        # add get_and_display_chosen_month_data here so that chosen month figures are displayed at start
        label_chosen_month = tk.Label(master=frame_chosen_month, textvariable=self._chosen_month)
        label_chosen_month.grid(row=1, column=0)
        frame_chosen_month.grid(row=1, column=0, sticky='w', padx=10)

    def create_frame_left_to_budget(self, root):
        """ Creating frame (top left) that displays the left to budget figure. """
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

    def create_frame_main(self, root):
        """ Creating main window frame that holds row and column texts, and entry fields. """
        # main window frame displaying budgeting items
        frame_main = tk.Frame(master=self._root, relief=tk.FLAT, borderwidth=1)
        frame_main.grid(row=3, column=1, padx=10, pady=10)
        ui_helper.create_column_titles(frame_main)
        ui_helper.create_category_column_texts(frame_main)
        entry_field_width = 16
        self.create_planned_entry_fields(frame_main, entry_field_width)
        self.create_receivedspent_entry_fields(frame_main, entry_field_width)

    def create_planned_entry_fields(self, frame_main, width):
        """ Creating 'PLANNED' column entry fields and 'Save planned' button. """
        self._chosen_month_planned_income = tk.Entry(master=frame_main, width=width)
        self._chosen_month_planned_rent = tk.Entry(master=frame_main, width=width)
        self._chosen_month_planned_bills = tk.Entry(master=frame_main, width=width)
        self._chosen_month_planned_spending = tk.Entry(master=frame_main, width=width)
        self._chosen_month_planned_debt_service = tk.Entry(master=frame_main, width=width)
        self._chosen_month_planned_saving = tk.Entry(master=frame_main, width=width)
        self._chosen_month_planned_income.grid(row=4, column=1, sticky="e")
        self._chosen_month_planned_rent.grid(row=5, column=1, sticky="e")
        self._chosen_month_planned_bills.grid(row=6, column=1, sticky="e")
        self._chosen_month_planned_spending.grid(row=7, column=1, sticky="e")
        self._chosen_month_planned_debt_service.grid(row=8, column=1, sticky="e")
        self._chosen_month_planned_saving.grid(row=9, column=1, sticky="e")
        button_save_planned_figures = tk.Button(
            master=frame_main,
            text="Save planned",
            command=self.save_month_planned_figures
        )
        button_save_planned_figures.grid(row=10, column=1)

    def create_receivedspent_entry_fields(self, frame_main, width):
        """ Creating 'RECEIVED / SPENT' column entry fields and 'Save planned' button. """
        self._chosen_month_receivedspent_income = tk.Entry(master=frame_main, width=width)
        self._chosen_month_receivedspent_rent = tk.Entry(master=frame_main, width=width)
        self._chosen_month_receivedspent_bills = tk.Entry(master=frame_main, width=width)
        self._chosen_month_receivedspent_spending = tk.Entry(master=frame_main, width=width)
        self._chosen_month_receivedspent_debt_service = tk.Entry(master=frame_main, width=width)
        self._chosen_month_receivedspent_saving = tk.Entry(master=frame_main, width=width)
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
        """ Saving month's planned column figures in the month object (not file). """
        month_number = service.get_month_number_and_name(self._chosen_month.get())[0]
        try:
            income_int = int(self._chosen_month_planned_income.get())
            rent_int = int(self._chosen_month_planned_rent.get())
            bills_int = int(self._chosen_month_planned_bills.get())
            spending_int = int(self._chosen_month_planned_spending.get())
            debt_service_int = int(self._chosen_month_planned_debt_service.get())
            saving_int = int(self._chosen_month_planned_saving.get())
        except ValueError:
            service.error_window_entered_item_not_integer()
            return
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
        """ Saving month's received/spent figures in the month object (not file). """
        month_number = service.get_month_number_and_name(self._chosen_month.get())[0]
        try:
            income_int = int(self._chosen_month_receivedspent_income.get())
            rent_int = int(self._chosen_month_receivedspent_rent.get())
            bills_int = int(self._chosen_month_receivedspent_bills.get())
            spending_int = int(self._chosen_month_receivedspent_spending.get())
            debt_service_int = int(self._chosen_month_receivedspent_debt_service.get())
            saving_int = int(self._chosen_month_receivedspent_saving.get())
        except ValueError:
            service.error_window_entered_item_not_integer()
            return
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

    def get_and_display_chosen_month_data(self, month_number):
        """ Getting the chosen month data and displaying figures in the window. """
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

    def create_tool_bar(self):
        """ Creating toolbar, placed on bottom of the program window. """
        toolbar_left_side = Frame(master=self._root, cursor='hand2', relief=SUNKEN, borderwidth=1)
        toolbar_center = Frame(master=self._root, cursor='hand2', relief=SUNKEN, borderwidth=1)
        toolbar_right_side = Frame(master=self._root, cursor='hand2', relief=SUNKEN, borderwidth=1)
        toolbar_left_side.grid(row=25, column=0)
        toolbar_center.grid(row=25, column=1)
        toolbar_right_side.grid(row=25, column=2, sticky='e')
        Button(toolbar_left_side, text='Year overview',
            command=(lambda: ui_helper.open_year_overview_window(
                self.table_all_months_receivedspent))).pack(side=LEFT)
        Button(toolbar_center, text='Open', command=self.open_data_from_file).pack(side=LEFT)
        Button(toolbar_center, text='Save', command=self.save_data_to_file).pack(side=LEFT)
        Button(toolbar_center, text='Help', command=ui_helper.open_help_window).pack(side=LEFT)
        Button(toolbar_right_side, text='Quit', command=self._root.quit).pack(side=RIGHT)

    def open_data_from_file(self):
        """ Opening file and importing previously saved data. """
        print("opening data from a file")
        path = askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not path:
            return
        with open(path) as f:
            lines = f.readlines()
        index = 1
        table_all_months_planned = ["empty cell"]  # leaving index 0 empty
        table_all_months_receivedspent = ["empty cell"]  # leaving index 0 empty
        for line in lines:
            line_stripped = line.strip()
            parts = line_stripped.split(",")
            if index <= 12:
                created_month = entities.month.Month(service.get_month_name(index), int(parts[0]),
                    int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]))
                table_all_months_planned.append(created_month)
            elif index >= 13:
                created_month = entities.month.Month(service.get_month_name(index-12), int(parts[0]),
                    int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]))
                table_all_months_receivedspent.append(created_month)
            index += 1
        self.table_all_months_planned = table_all_months_planned
        self.table_all_months_receivedspent = table_all_months_receivedspent

    def save_data_to_file(self):
        """ Saving budget figures to a .csv file. """
        print("saving data to a file")
        path = asksaveasfilename(filetypes=[("CSV Files", "*.csv")])
        if not path:
            return
        month_data_to_be_saved = ["empty cell"]
        for i in range(1, 13):
            parts = [str(self.table_all_months_planned[i].get_income()),
                str(self.table_all_months_planned[i].get_rent()),
                str(self.table_all_months_planned[i].get_bills()),
                str(self.table_all_months_planned[i].get_spending()),
                str(self.table_all_months_planned[i].get_debt_service()),
                str(self.table_all_months_planned[i].get_saving())]
            row = ",".join(parts)
            month_data_to_be_saved.append(row)
        for i in range(13, 25):
            parts = [str(self.table_all_months_receivedspent[i-12].get_income()),
                str(self.table_all_months_receivedspent[i-12].get_rent()),
                str(self.table_all_months_receivedspent[i-12].get_bills()),
                str(self.table_all_months_receivedspent[i-12].get_spending()),
                str(self.table_all_months_receivedspent[i-12].get_debt_service()),
                str(self.table_all_months_receivedspent[i-12].get_saving())]
            row = ",".join(parts)
            month_data_to_be_saved.append(row)
        with open(path, mode="w") as f:
            for i in range(1, 25):
                f.write(month_data_to_be_saved[i] + "\n")
