""" Services module """

from tkinter.messagebox import *

ALL_MONTHS = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

def calculate_left_to_budget(income, bills, spending, debt):
    left_to_budget = income - bills - spending - debt
    print(f"left_to_budget is: {left_to_budget}")
    return left_to_budget

def get_month_name(month_number):
    all_months = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                    "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    return all_months[month_number]

def bar_item_notdone():
    showerror('Not implemented', 'Functionality not yet available, but coming soon')

def get_month_number_and_name(chosen_month):
    month_name = chosen_month #self._chosen_month.get()
    dict = {"JANUARY": 1, "FEBRUARY": 2, "MARCH": 3, "APRIL": 4,
            "MAY": 5,"JUNE": 6, "JULY": 7, "AUGUST": 8,
            "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}
    return (dict[month_name], month_name)
