import unittest
from tkinter import Tk, ttk, StringVar
from ui.ui import UI
import ui.ui_helper as ui_helper
import entities.month as month
import services.service as service

class TestMonth(unittest.TestCase):
    def setUp(self):
        window = Tk()
        window.geometry("680x500")
        window.title("EveryEuro")
        self.UI = UI(window)
        self.UI.start()

    def test_created_month_has_correct_name_value(self):
        january = month.Month("JANUARY")
        self.assertEqual(january.get_month_name(), "JANUARY")
        february = month.Month("FEBRUARY", 3000, 750, 100, 500, 300, 1350)
        self.assertEqual(february.get_month_name(), "FEBRUARY")

    def test_table_all_months_created_and_has_right_values(self):
        table_all_months = service.create_all_months_table()
        self.assertEqual(len(table_all_months), 13)
        self.assertEqual(table_all_months[12].get_month_name(), "DECEMBER")
        self.assertEqual(table_all_months[4].get_month_name(), "APRIL")
        self.assertEqual(table_all_months[8].get_month_name(), "AUGUST")

    # testing that planned entry fields have corrent values
    def test_get_month_income(self):
        march = month.Month("MARCH", 3003, 800, 100, 500, 300, 250)
        self.assertEqual(march.get_income(), 3003)

    def test_get_month_rent(self):
        april = month.Month("APRIL", 4004, 800, 100, 300, 250, 600)
        self.assertEqual(april.get_rent(), 800)

    def test_get_month_bills(self):
        may = month.Month("MAY", 3000, 800, 150, 300, 200)
        self.assertEqual(may.get_bills(), 150)

    def test_get_month_spending(self):
        june = month.Month("JUNE", 3000, 800, 130, 505, 250)
        self.assertEqual(june.get_spending(), 505)

    def test_get_month_debt_service(self):
        august = month.Month("AUGUST", 3000, 800, 100, 350, 123, 5)
        self.assertEqual(august.get_debt_service(), 123)

    def test_get_month_saving(self):
        september = month.Month("SEPTEMBER", 2999, 999, 109, 300, 150, 567)
        self.assertEqual(september.get_saving(), 567)
        october = month.Month("OCTOBER", 3010, 800, 110, 310, 110)  # leaving saving empty
        self.assertEqual(october.get_saving(), 0)

    # testing setting values
    def test_set_income(self):
        november = month.Month("NOVEMBER", 3000, 600, 160, 565, 260)
        november.set_income(2989)
        self.assertEqual(november.get_income(), 2989)

    def test_set_rent(self):
        october = month.Month("OCTOBER", 2900, 700, 180, 495, 230)
        october.set_rent(777)
        self.assertEqual(october.get_rent(), 777)

    def test_set_bills(self):
        september = month.Month("SEPTEMBER", 2850, 888, 200, 500, 220)
        september.set_bills(222)
        self.assertEqual(september.get_bills(), 222)
        self.assertNotEqual(september.get_bills(), 200)

    def test_set_spending(self):
        august = month.Month("AUGUST", 2800, 808, 288, 555, 245)
        august.set_spending(600)
        self.assertEqual(august.get_spending(), 600)

    def test_set_debt_service(self):
        july = month.Month("JULY", 2750, 780, 300, 500, 220)
        july.set_debt_service(1000)
        self.assertEqual(july.get_debt_service(), 1000)

    def test_set_saving(self):
        june = month.Month("JUNE", 2700, 750, 333, 543, 234, 123)
        june.set_saving(800)
        self.assertEqual(june.get_saving(), 800)

class TestService(unittest.TestCase):
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

    # testing opening data from file
    def test_open_data_from_file(self):
        table_all_months_planned, table_all_months_receivedspent = service.open_data_from_file("yes")
        self.assertEqual(len(table_all_months_planned), 13)
        self.assertEqual(len(table_all_months_receivedspent), 13)
        self.assertEqual(table_all_months_planned[1].get_month_name(), "JANUARY")
        self.assertEqual(table_all_months_planned[4].get_month_name(), "APRIL")
        # add more tests here

    # testing saving data to file
    def test_save_data_to_file(self):
        # opening my_budget.csv
        table_all_months_planned, table_all_months_receivedspent = service.open_data_from_file("yes")
        # saving my_budget.csv contents to backup_budget.csv
        service.save_data_to_file(table_all_months_planned, table_all_months_receivedspent, "yes")
        # opening the saved data from backup_budget.csv
        table_planned_saved, table_receivedspent_saved = service.open_data_from_file("yes", "backup_budget.csv")
        self.assertEqual(len(table_planned_saved), 13)
        self.assertEqual(len(table_receivedspent_saved), 13)
        # comparing the original data and saved data, in planned testing all values
        for i in range(1, 13):
            self.assertEqual(table_all_months_planned[i].get_month_name(), table_planned_saved[i].get_month_name())
            self.assertEqual(table_all_months_planned[i].get_income(), table_planned_saved[i].get_income())
            self.assertEqual(table_all_months_planned[i].get_rent(), table_planned_saved[i].get_rent())
            self.assertEqual(table_all_months_planned[i].get_bills(), table_planned_saved[i].get_bills())
            self.assertEqual(table_all_months_planned[i].get_spending(), table_planned_saved[i].get_spending())
            self.assertEqual(table_all_months_planned[i].get_debt_service(), table_planned_saved[i].get_debt_service())
            self.assertEqual(table_all_months_planned[i].get_saving(), table_planned_saved[i].get_saving())
        # in receivedspent testing only some values
        #self.assertEqual(table_all_months_receivedspent[2].get_income(), table_receivedspent_saved[3].get_income())
        # add more tests here
