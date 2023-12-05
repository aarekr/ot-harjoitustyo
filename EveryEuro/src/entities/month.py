""" Month objects """

class Month:
    """ Every month is an object """

    def __init__(self, month_name, income=0, rent=0, bills=0, spending=0, debt_service=0, saving=0):
        print("creating new month:", month_name)
        self.month_name = month_name
        self.income = income
        self.rent = rent
        self.bills = bills
        self.spending = spending
        self.debt_service = debt_service
        self.saving = saving

    def get_month_name(self):
        return self.month_name

    def get_income(self):
        return self.income

    def set_income(self, new_income):
        self.income = new_income

    def get_rent(self):
        return self.rent

    def get_bills(self):
        return self.bills

    def get_spending(self):
        return self.spending

    def get_debt_service(self):
        return self.debt_service

    def get_saving(self):
        return self.saving

    def print_month_info(self):
        print(self.month_name, self.income, self.rent, self.bills, self.spending, self.debt_service, self.saving)
