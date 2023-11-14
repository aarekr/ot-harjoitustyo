import unittest
from tkinter import Tk
#import sys
#sys.path.append('../ui')
from ui import UI

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
