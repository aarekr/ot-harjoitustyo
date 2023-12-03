""" Services module """

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
