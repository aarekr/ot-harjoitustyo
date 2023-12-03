""" Month objects """

class Month:
    """ Every month is an object """

    def __init__(self, month_name, income=0, bills=0, spending=0, debt=0):
        print("creating new month:", month_name)
        self.month_name = month_name
        self.income = income
        self.bills = bills
        self.spending = spending
        self.debt = debt

    def get_month_name(self):
        return self.month_name

    def get_income(self):
        return self.income

    def set_income(self, new_income):
        self.income = new_income

    def get_bills(self):
        return self.bills

    def get_spending(self):
        return self.spending

    def get_debt(self):  # debt service amount (not total debt)
        return self.debt

    def print_month_info(self):
        print(self.month_name, self.income, self.bills, self.spending, self.debt)
