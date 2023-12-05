""" Services module """

from tkinter.messagebox import showerror
import entities.month as em

#ALL_MONTHS = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
#                "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]

def calculate_left_to_budget(income, rent, bills, spending, debt_service, saving):
    left_to_budget = income - rent - bills - spending - debt_service - saving
    print(f"left_to_budget is: {left_to_budget}")
    return left_to_budget

def bar_item_notdone():  # this function will not be in the final version
    showerror('Not implemented', 'Functionality not yet available, but coming soon')

# combine the two functions below
def get_month_name(month_number):
    all_months = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                    "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    return all_months[month_number]

def get_month_number_and_name(chosen_month):
    month_name = chosen_month
    dict_months = {"JANUARY": 1, "FEBRUARY": 2, "MARCH": 3, "APRIL": 4,
            "MAY": 5,"JUNE": 6, "JULY": 7, "AUGUST": 8,
            "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}
    return (dict_months[month_name], month_name)

def create_all_months_table():
    table_all_months = ["empty cell"]
    # in the final version all 6 values below should be 0
    # current values while developing
    income = 2000
    rent = 800
    bills = 100
    spending = 500
    debt_service = 200
    saving = 0
    for i in range(1, 13):
        month_name = get_month_name(i)
        created_month = em.Month(month_name, income+i, rent+i, bills+i, spending+i,
                                    debt_service+i, saving)
        table_all_months.append(created_month)
    return table_all_months
