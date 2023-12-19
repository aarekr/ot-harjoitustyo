""" User Interface """

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import ui.ui_helper as ui_helper
import services.service as service
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
        self.table_all_months_planned = service.create_all_months_table()
        self.table_all_months_receivedspent = service.create_all_months_table()

        ui_helper.create_menu_bar(self._root)
        ui_helper.create_tool_bar(self._root, self.get_data_from_file,
            self.table_all_months_planned, self.table_all_months_receivedspent)

        ui_helper.create_frame_month_button_row(self._root, self.get_and_display_chosen_month_data)
        self._chosen_month = tk.StringVar()
        self._chosen_month.set(service.get_month_name(datetime.now().month))  # e.g. 12 = December
        ui_helper.create_frame_chosen_month(self._root, self._chosen_month)
        self._chosen_month_left_to_budget = tk.StringVar()
        self._chosen_month_left_to_budget.set("0")
        ui_helper.create_frame_left_to_budget(self._root, self._chosen_month_left_to_budget)
        self.create_frame_main()  # self._root

        self.get_and_display_chosen_month_data(
            service.get_month_number_and_name(self._chosen_month.get())[0]
        )

    def create_frame_main(self):
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
        """ Creating 'RECEIVED / SPENT' column entry fields and 'Save rec./spent' button. """
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

    def save_month_planned_figures(self, testing="no"):
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
            if testing == "no":
                ui_helper.error_window_entered_item_not_integer()
            elif testing == "yes":
                return "Incorrect value"
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

    def save_month_receivedspent_figures(self, testing="no"):
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
            if testing == "no":
                ui_helper.error_window_entered_item_not_integer()
            elif testing == "yes":
                return "Incorrect value"
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
        (month_name, income_planned, rent_planned, bills_planned, spending_planned,
            debt_service_planned, saving_planned, left_to_budget) = service.get_planned_values(
                self.table_all_months_planned, month_number)
        self._chosen_month.set(month_name)
        self._chosen_month_left_to_budget.set(left_to_budget)
        # refactor this: data is first fetched from service and then sent back to another function
        service.update_entry_field_value(self._chosen_month_planned_income, income_planned)
        service.update_entry_field_value(self._chosen_month_planned_rent, rent_planned)
        service.update_entry_field_value(self._chosen_month_planned_bills, bills_planned)
        service.update_entry_field_value(self._chosen_month_planned_spending, spending_planned)
        service.update_entry_field_value(self._chosen_month_planned_debt_service, debt_service_planned)
        service.update_entry_field_value(self._chosen_month_planned_saving, saving_planned)

        service.update_entry_field_value(self._chosen_month_receivedspent_income,
            self.table_all_months_receivedspent[month_number].get_income())
        service.update_entry_field_value(self._chosen_month_receivedspent_rent,
            self.table_all_months_receivedspent[month_number].get_rent())
        service.update_entry_field_value(self._chosen_month_receivedspent_bills,
            self.table_all_months_receivedspent[month_number].get_bills())
        service.update_entry_field_value(self._chosen_month_receivedspent_spending,
            self.table_all_months_receivedspent[month_number].get_spending())
        service.update_entry_field_value(self._chosen_month_receivedspent_debt_service,
            self.table_all_months_receivedspent[month_number].get_debt_service())
        service.update_entry_field_value(self._chosen_month_receivedspent_saving,
            self.table_all_months_receivedspent[month_number].get_saving())

    def get_data_from_file(self):
        """ Importing and setting .csv data into tables planned and receivespent. """
        try:
            self.table_all_months_planned, self.table_all_months_receivedspent = service.open_data_from_file()
        except:
            print("Opening file canceled")
        self.get_and_display_chosen_month_data(
            service.get_month_number_and_name(self._chosen_month.get())[0]
        )
