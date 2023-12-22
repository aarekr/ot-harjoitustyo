""" Services module """

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askyesno
import entities.month

def calculate_left_to_budget(income, rent, bills, spending, debt_service, saving):
    """Calculating left to budget item shown in the top left part of the program window.
    Args:
        income: planned/expected income for current month
        rent: planned rent/mortgage for current month
        bills: planned bills for current month
        spending: planned spending for current month
        debt_service: planned debt servicing for current month
        saving: planned saving for current month
    Returns:
        Int: income minus all other parameters
    """
    left_to_budget = income - rent - bills - spending - debt_service - saving
    return left_to_budget

def get_month_name(month_number):
    """Returning month in string format.
    Args:
        month_number: month number as an integer e.g. 3 (March)
    Returns:
        String: month name
    """
    all_months = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                    "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    return all_months[month_number]

def get_month_number_and_name(month_name):
    """Returning index of a month.
    Args:
        month_name: month name as in calendar
    Returns:
        Int: number of the given month
        String: month name
    """
    dict_months = {"JANUARY": 1, "FEBRUARY": 2, "MARCH": 3, "APRIL": 4,
            "MAY": 5,"JUNE": 6, "JULY": 7, "AUGUST": 8,
            "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}
    return (dict_months[month_name], month_name)

def create_all_months_table():
    """Creating month data with default values 0 for all entry fields.
    Returns:
        Table of 12 Month objects with month names and fields as 0
    """
    table_all_months = ["empty cell"]  # leaving index 0 empty
    for i in range(1, 13):
        created_month = entities.month.Month(get_month_name(i), 0, 0, 0, 0, 0, 0)
        table_all_months.append(created_month)
    return table_all_months

def get_planned_values(table_all_months_planned, month_number):
    """ Returning chosen month name and number items. """
    month_name = table_all_months_planned[month_number].get_month_name()
    income_planned = table_all_months_planned[month_number].get_income()
    rent_planned = table_all_months_planned[month_number].get_rent()
    bills_planned = table_all_months_planned[month_number].get_bills()
    spending_planned = table_all_months_planned[month_number].get_spending()
    debt_service_planned = table_all_months_planned[month_number].get_debt_service()
    saving_planned = table_all_months_planned[month_number].get_saving()
    left_to_budget = calculate_left_to_budget(income_planned, rent_planned, bills_planned,
        spending_planned, debt_service_planned, saving_planned)
    return (month_name, income_planned, rent_planned, bills_planned, spending_planned,
        debt_service_planned, saving_planned, left_to_budget)

def update_entry_field_value(entry_field, new_value):
    """ Updating planned / receivedspent entry field with new value. """
    entry_field.delete(0, tk.END)
    entry_field.insert(0, new_value)

def open_data_from_file(testing="no", test_file="my_budget.csv"):
    """ Opening file and importing previously saved data. """
    if testing == "no":
        path = askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not path:
            return
    elif testing == "yes":
        path = test_file
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    index = 1
    table_all_months_planned = ["empty cell"]        # leaving index 0 empty
    table_all_months_receivedspent = ["empty cell"]  # leaving index 0 empty
    for line in lines:
        line_stripped = line.strip()
        parts = line_stripped.split(",")
        if index <= 12:
            created_month = entities.month.Month(get_month_name(index), int(parts[0]),
                int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]))
            table_all_months_planned.append(created_month)
        elif index >= 13:
            created_month = entities.month.Month(get_month_name(index-12), int(parts[0]),
                int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]))
            table_all_months_receivedspent.append(created_month)
        index += 1
    return table_all_months_planned, table_all_months_receivedspent

def save_data_to_file(table_all_months_planned, table_all_months_receivedspent, testing="no"):
    """ Saving budget figures to a .csv file. """
    if testing == "no":
        path = asksaveasfilename(filetypes=[("CSV Files", "*.csv")])
        if not path:
            return
    elif testing == "yes":
        path = "backup_budget.csv"
    month_data_to_be_saved = ["empty cell"]
    for i in range(1, 13):
        parts = [str(table_all_months_planned[i].get_income()),
            str(table_all_months_planned[i].get_rent()),
            str(table_all_months_planned[i].get_bills()),
            str(table_all_months_planned[i].get_spending()),
            str(table_all_months_planned[i].get_debt_service()),
            str(table_all_months_planned[i].get_saving())]
        row = ",".join(parts)
        month_data_to_be_saved.append(row)
    for i in range(13, 25):
        parts = [str(table_all_months_receivedspent[i-12].get_income()),
            str(table_all_months_receivedspent[i-12].get_rent()),
            str(table_all_months_receivedspent[i-12].get_bills()),
            str(table_all_months_receivedspent[i-12].get_spending()),
            str(table_all_months_receivedspent[i-12].get_debt_service()),
            str(table_all_months_receivedspent[i-12].get_saving())]
        row = ",".join(parts)
        month_data_to_be_saved.append(row)
    with open(path, mode="w", encoding="utf-8") as f:
        for i in range(1, 25):
            f.write(month_data_to_be_saved[i] + "\n")
    print("data saved to file:", path)

def quit_program(root):
    """ Asking user to confirm that s/he wants to quit the program. """
    ok_to_quit = askyesno('Verify quit', 'Are you sure you want to quit?')
    if ok_to_quit:
        root.quit()
