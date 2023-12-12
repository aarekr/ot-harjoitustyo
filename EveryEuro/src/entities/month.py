""" Month object """

class Month:
    """Class, handling months as objects.
    Attributes:
        month_name: month as a string
        income: planned/expected income for current month
        rent: planned rent/mortgage for current month
        bills: planned bills for current month
        spending: planned spending for current month
        debt_service: planned debt servicing for current month
        saving: planned saving for current month
    """

    def __init__(self, month_name, income=0, rent=0, bills=0, spending=0, debt_service=0, saving=0):
        """Class constructor that creates a month.
        Args:
            income: planned/received income for current month
            rent: planned/spent rent/mortgage for current month
            bills: planned/spent bills for current month
            spending: planned/spent spending for current month
            debt_service: planned/spent debt servicing for current month
            saving: planned/spent saving for current month
        """
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

    def set_rent(self, new_rent):
        self.rent = new_rent

    def get_bills(self):
        return self.bills

    def set_bills(self, new_bills):
        self.bills = new_bills

    def get_spending(self):
        return self.spending

    def set_spending(self, new_spending):
        self.spending = new_spending

    def get_debt_service(self):
        return self.debt_service

    def set_debt_service(self, new_debt_service):
        self.debt_service = new_debt_service

    def get_saving(self):
        return self.saving

    def set_saving(self, new_saving):
        self.saving = new_saving
