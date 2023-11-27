""" Month objects """

class Month:
    """ Every month is an object """

    def __init__(self, month_name, income=0, bills=0, spending=0, debt=0):
        print("creating new month:", month_name)
        self.month = month_name
        self.income = income
        self.bills = bills
        self.spending = spending
        self.debt = debt
    
    def print_month_info(self):
        print(self.month, self.income, self.bills, self.spending, self.debt)

    def __str__(self):
        print(self.month, self.income, self.bills, self.spending, self.debt)

def calculate_budget_balance(income, bills, spending, debt):
    print("income:", income, type(income))
    budget_balance = income - bills - spending - debt
    #budget_balance = int(income) - int(bills) - int(spending) - int(debt)
    #budget_balance = float(income) - float(bills) - float(spending) - float(debt)
    print(f"budget_balance is: {budget_balance}")
    return budget_balance
