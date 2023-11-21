import unittest
from tkinter import Tk, ttk, StringVar
from ui.ui import UI

# run the tests with command: pytest src

class TestUI(unittest.TestCase):
    def setUp(self):
        window = Tk()
        window.geometry("650x500")
        window.title("EveryEuro")
        self.UI = UI(window)
        self.UI.start()

    def test_ui_is_created(self):
        self.assertNotEqual(self.UI, None)

    #def test_window_size(self):
    #    self.assertEqual(self.UI.width, "200*200")

    # testing that number fields are created
    def test_left_to_budget_field_created_at_start(self):
        self.assertNotEqual(self.UI._left_to_budget, None)

    def test_income_entry_field_created_at_start(self):
        self.assertNotEqual(self.UI._income_planned, None)

    def test_bills_entry_field_created_at_start(self):
        self.assertNotEqual(self.UI._bills_planned, None)

    def test_spending_entry_field_created_at_start(self):
        self.assertNotEqual(self.UI._spending_planned, None)

    def test_debt_entry_field_created_at_start(self):
        self.assertNotEqual(self.UI._debt_planned, None)

    # testing that number fields have correct values
    def test_left_to_budget_has_correct_value(self):
        self.UI._left_to_budget.set(600)
        self.assertEqual(self.UI._left_to_budget.get(), str(600))

    def test_income_entry_has_correct_value(self):
        self.UI._income_planned = 2000
        self.assertEqual(self.UI._income_planned, 2000)

    def test_bills_entry_has_correct_value(self):
        self.UI._bills_planned = 700
        self.assertEqual(self.UI._bills_planned, 700)

    def test_spending_entry_has_correct_value(self):
        self.UI._spending_planned = 500
        self.assertEqual(self.UI._spending_planned, 500)

    def test_debt_entry_has_correct_value(self):
        self.UI._debt_planned = 300
        self.assertEqual(self.UI._debt_planned, 300)

    # testing left_to_budget items
    def test_left_to_budget_type(self):
        self.assertEqual(type(self.UI._left_to_budget), StringVar)

    def test_left_to_budget_text_type(self):
        self.assertEqual(type(self.UI._left_to_budget_text), StringVar)

    # testing functions
    """def test_calculate_budget_balance(self):
        self.UI._income_entry = 2500
        self.UI._bills_entry = 800
        self.UI._spending_entry = 600
        self.UI._debt_entry = 100
        self.assertEqual(self.UI.calculate_budget_balance(), 500)"""


    def test_update_left_to_budget(self):
        self.UI.update_left_to_budget(500)
        self.assertEqual(self.UI._left_to_budget.get(), str(500))