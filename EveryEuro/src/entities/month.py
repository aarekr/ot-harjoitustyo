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

    def get_income(self):
        return self.income

    def get_bills(self):
        return self.bills

    def get_spending(self):
        return self.spending

    def get_debt(self):  # debt service amount (not total debt)
        return self.debt

    def print_month_info(self):
        print(self.month, self.income, self.bills, self.spending, self.debt)

def calculate_budget_balance(income, bills, spending, debt):
    print("income:", income, type(income))
    budget_balance = income - bills - spending - debt
    #budget_balance = int(income) - int(bills) - int(spending) - int(debt)
    #budget_balance = float(income) - float(bills) - float(spending) - float(debt)
    print(f"budget_balance is: {budget_balance}")
    return budget_balance
