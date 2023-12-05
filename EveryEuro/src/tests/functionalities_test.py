import unittest
from tkinter import Tk, ttk, StringVar
from ui.ui import UI
import entities.month as em
import services.service as service

class TestFunctionalities(unittest.TestCase):
    def setUp(self):
        window = Tk()
        window.geometry("680x500")
        window.title("EveryEuro")
        self.UI = UI(window)
        self.UI.start()

    def test_created_month_has_correct_name_value(self):
        jan = em.Month("JANUARY")
        self.assertEqual(jan.get_month_name(), "JANUARY")
        feb = em.Month("FEBRUARY", 3000, 750, 100, 500, 300, 1350)
        self.assertEqual(feb.get_month_name(), "FEBRUARY")

    def test_table_all_months_created_and_has_right_values(self):
        table_all_months = service.create_all_months_table()
        self.assertEqual(len(table_all_months), 13)
        self.assertEqual(table_all_months[12].get_month_name(), "DECEMBER")
        self.assertEqual(table_all_months[4].get_month_name(), "APRIL")
        self.assertEqual(table_all_months[8].get_month_name(), "AUGUST")

    # testing that planned entry fields have corrent values
    def test_get_month_income(self):
        march = em.Month("MARCH", 3003, 800, 100, 500, 300, 250)
        self.assertEqual(march.get_income(), 3003)

    def test_get_month_rent(self):
        april = em.Month("APRIL", 4004, 800, 100, 300, 250, 600)
        self.assertEqual(april.get_rent(), 800)

    def test_get_month_bills(self):
        may = em.Month("MAY", 3000, 800, 150, 300, 200)
        self.assertEqual(may.get_bills(), 150)

    def test_get_month_spending(self):
        june = em.Month("JUNE", 3000, 800, 130, 505, 250)
        self.assertEqual(june.get_spending(), 505)

    def test_get_month_debt_service(self):
        aug = em.Month("AUGUST", 3000, 800, 100, 350, 123, 5)
        self.assertEqual(aug.get_debt_service(), 123)

    def test_get_month_saving(self):
        sep = em.Month("SEPTEMBER", 2999, 999, 109, 300, 150, 567)
        self.assertEqual(sep.get_saving(), 567)
        october = em.Month("OCTOBER", 3010, 800, 110, 310, 110)  # leaving saving empty
        self.assertEqual(october.get_saving(), 0)

    def test_set_income(self):
        nov = em.Month("NOVEMBER", 3000, 600, 160, 565, 260)
        nov.set_income(2989)
        self.assertEqual(nov.get_income(), 2989)

    # testing month name and number values
    def test_get_month_name_has_correct_name_corresponding_to_number(self):
        self.assertEqual(service.get_month_name(3), "MARCH")
        self.assertEqual(service.get_month_name(12), "DECEMBER")

    def test_get_month_number_and_name_has_correct_values(self):
        self.assertEqual(service.get_month_number_and_name("APRIL"), (4, "APRIL"))
        self.assertEqual(service.get_month_number_and_name("JULY"), (7, "JULY"))
        self.assertEqual(service.get_month_number_and_name("NOVEMBER"), (11, "NOVEMBER"))

    # testing functions
    def test_calculate_left_to_budget(self):
        self.assertEqual(service.calculate_left_to_budget(2500, 800, 100, 600, 150, 100), 750)
        self.assertEqual(service.calculate_left_to_budget(2200, 700, 150, 500, 200, 130), 520)
