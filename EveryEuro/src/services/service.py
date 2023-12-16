""" Services module """

from tkinter import ttk, Frame, Menu, Label, Text, Button, SUNKEN, RIGHT, LEFT, HORIZONTAL, Toplevel
from tkinter.messagebox import showerror
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
    print(f"left_to_budget is: {left_to_budget}")
    return left_to_budget

def bar_item_notdone():  # this function will not be in the final version
    """Shows an error window for functionalities that are not yet implemented.
    """
    showerror('Not implemented', 'Functionality not yet available, but coming soon')

def error_window_entered_item_not_integer():  # this function will not be in the final version
    """ Shows an error window if other than integer is entered. """
    showerror('Value Error', 'Please enter only integers. Text, floats etc. are not allowed.')

# combine the two functions below
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
