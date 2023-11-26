""" Month objects """

class Month:
    """ Every month is an object """

    def __init__(self, month_name):
        self.month = month_name

def calculate_budget_balance(income, bills, spending, debt):
    print("income:", income, type(income))
    budget_balance = 555
    #budget_balance = int(income) - int(bills) - int(spending) - int(debt)
    #budget_balance = float(income) - float(bills) - float(spending) - float(debt)
    print(f"budget_balance is: {budget_balance}")
    return budget_balance
