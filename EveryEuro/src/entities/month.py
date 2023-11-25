""" Month objects """

class Month:
    """ Every month is an object """

    def __init__(self, month_name):
        self.month = month_name

def calculate_budget_balance(income, bills, spending, debt):
    budget_balance = int(income) - int(bills) - int(spending) - int(debt)
    print(f"budget_balance is: {budget_balance}")
    return budget_balance
