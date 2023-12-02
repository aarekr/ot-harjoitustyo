import unittest
from tkinter import Tk, ttk, StringVar
from ui.ui import UI
import entities.month

# run the tests with command: poetry run invoke test
# generate test report html : poetry run invoke coverage-report

class TestUI(unittest.TestCase):
    def setUp(self):
        window = Tk()
        window.geometry("680x500")
        window.title("EveryEuro")
        self.UI = UI(window)
        self.UI.start()

    def test_ui_is_created(self):
        self.assertNotEqual(self.UI, None)

    #def test_window_size(self):
    #    self.assertEqual(self.UI.geometry, "200*200")

    # testing that number fields are created
    def test_current_month_left_to_budget_field_created_at_start(self):
        self.assertNotEqual(self.UI._current_month_left_to_budget, None)

    #def test_current_month_planned_income_field_created_at_start(self):
    #    self.assertNotEqual(self.UI._current_month_income, None)
        #self._current_month_income
        #self._current_month_bills
        #self._current_month_spending
        #self._current_month_debt

    # testing that number fields have correct values
    """def test_left_to_budget_has_correct_value(self):
        self._current_month_left_to_budget
        self.UI._current_month_left_to_budget.set(600)
        self.assertEqual(self.UI._current_month_left_to_budget.get(), str(600))"""

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
    """def test_left_to_budget_type(self):
        self.assertEqual(type(self.UI._left_to_budget), StringVar)

    def test_left_to_budget_text_type(self):
        self.assertEqual(type(self.UI._left_to_budget_text), StringVar)"""

    def test_current_month_has_correct_value(self):
        self.assertEqual(self.UI.get_current_month(0), "")
        self.assertEqual(self.UI.get_current_month(1), "JANUARY")
        self.assertEqual(self.UI.get_current_month(2), "FEBRUARY")
        self.assertEqual(self.UI.get_current_month(11), "NOVEMBER")

    # testing functions
    def test_calculate_budget_balance(self):
        self.assertEqual(entities.month.calculate_budget_balance(2500, 800, 600, 100), 1000)
        self.assertEqual(entities.month.calculate_budget_balance(2200, 700, 500, 200), 800)

    """def test_update_left_to_budget(self):
        self.UI.update_left_to_budget(500)
        self.assertEqual(self.UI._left_to_budget.get(), str(500))
        self.UI.update_left_to_budget(900)
        self.assertEqual(self.UI._left_to_budget.get(), str(900))"""

    def test_get_month_income(self):
        mar = entities.month.Month("MARCH", 3003, 1000, 800, 400)
        self.assertEqual(mar.get_income(), 3003)

    def test_get_month_bills(self):
        mar = entities.month.Month("MARCH", 3000, 1008, 700, 300)
        self.assertEqual(mar.get_bills(), 1008)

    def test_get_month_spending(self):
        mar = entities.month.Month("MARCH", 3000, 1000, 803, 250)
        self.assertEqual(mar.get_spending(), 803)

    def test_get_month_debt(self):
        mar = entities.month.Month("MARCH", 3000, 1000, 600, 350)
        self.assertEqual(mar.get_debt(), 350)
