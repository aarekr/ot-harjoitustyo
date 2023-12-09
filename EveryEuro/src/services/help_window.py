""" This class should handle Help Window, not in use at the moment """

from tkinter import * #Frame, Button

class HelpWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH)
        self.make_widgets()

    def make_widgets(self):
        button_quit = Button(text='Quit', command=close_help_window())

    def close_help_window():
        print("Closing Help Window")

def open_help_window():
    HelpWindow().mainloop()
