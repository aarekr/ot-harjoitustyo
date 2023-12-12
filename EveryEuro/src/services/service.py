""" Services module """

from tkinter import ttk, Frame, Menu, Label, Text, Button, SUNKEN, RIGHT, LEFT, HORIZONTAL, Toplevel
from tkinter.messagebox import showerror
import entities.month

def calculate_left_to_budget(income, rent, bills, spending, debt_service, saving):
    """Calculating left to budget item shown in the top left part of the program window.
    Args:
        income: planned/expected income for current month
        rent: planned rent/mortgage for current month
        bills: planned bills for current month
        spending: planned spending for current month
        debt_service: planned debt servicing for current month
        saving: planned saving for current month
    Returns:
        Int: income minus all other parameters
    """
    left_to_budget = income - rent - bills - spending - debt_service - saving
    print(f"left_to_budget is: {left_to_budget}")
    return left_to_budget

def bar_item_notdone():  # this function will not be in the final version
    """Shows an error window for functionalities that are not yet implemented.
    """
    showerror('Not implemented', 'Functionality not yet available, but coming soon')

# combine the two functions below
def get_month_name(month_number):
    """Returning month in string format.
    Args:
        month_number: month number as an integer e.g. 3 (March)
    Returns:
        String: month name
    """
    all_months = ["", "JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST",
                    "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    return all_months[month_number]

def get_month_number_and_name(month_name):
    """Returning index of a month.
    Args:
        month_name: month name as in calendar
    Returns:
        Int: number of the given month
        String: month name
    """
    dict_months = {"JANUARY": 1, "FEBRUARY": 2, "MARCH": 3, "APRIL": 4,
            "MAY": 5,"JUNE": 6, "JULY": 7, "AUGUST": 8,
            "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}
    return (dict_months[month_name], month_name)

def create_all_months_table():
    """Creating month data with default values 0 for all entry fields.
    Returns:
        Table of 12 Month objects with month names and fields as 0
    """
    table_all_months = ["empty cell"]  # leaving index 0 empty
    for i in range(1, 13):
        created_month = entities.month.Month(get_month_name(i), 0, 0, 0, 0, 0, 0)
        table_all_months.append(created_month)
    return table_all_months

def create_menu_bar(root):
    """Creating menu bar in the top part on the window.
    """
    top = Menu(root)
    root.config(menu=top)
    file = Menu(top, tearoff=False)
    file.add_command(label='Open...', command=bar_item_notdone, underline=0)
    file.add_command(label='Save to file', command=bar_item_notdone, underline=0)
    file.add_separator()
    file.add_command(label='Quit', command=root.quit, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)

    help_menu = Menu(top, tearoff=False)
    help_menu.add_command(label='Help', command=open_help_window, underline=0)
    top.add_cascade(label='Help', menu=help_menu, underline=0)

def create_tool_bar(root):
    """Creating toolbar, placed on bottom of the program window.
    """
    toolbar_left_side = Frame(master=root, cursor='hand2', relief=SUNKEN, borderwidth=1)
    toolbar_center = Frame(master=root, cursor='hand2', relief=SUNKEN, borderwidth=1)
    toolbar_right_side = Frame(master=root, cursor='hand2', relief=SUNKEN, borderwidth=1)
    toolbar_left_side.grid(row=25, column=0)
    toolbar_center.grid(row=25, column=1)
    toolbar_right_side.grid(row=25, column=2, sticky='e')
    Button(toolbar_left_side, text='Year overview',
        command=open_year_overview_window).pack(side=LEFT)
    Button(toolbar_center, text='Open', command=bar_item_notdone).pack(side=LEFT)
    Button(toolbar_center, text='Help', command=open_help_window).pack(side=LEFT)
    Button(toolbar_right_side, text='Quit', command=root.quit).pack(side=RIGHT)

def open_help_window():
    """Opens help window that explains how to use the program.
    """
    help_window = Toplevel()
    help_window.title("Help")
    help_window.geometry("670x200")
    help_window_text_field = Text(master=help_window, width=80, height=7)
    table_row_texts = ["", "How to use the program:",
        "\nEnter your monthly planned income and expenses in respective fields.",
        "\nClick 'Save planned' to save the figures.",
        "\nDuring the month, enter actual income and expenses.",
        "\nClick 'Save rec./spent' to save the figures.",
        "\nNavigate between months by clicking the month buttons on top of the window.",
        "\nLeft to budget shows how much you have left to allocate this month."]
    for row in range(1, 8):
        help_window_text_field.insert(str(float(row)), table_row_texts[row])
    help_window_text_field.place(x=10, y=10)
    Button(help_window, text='Got it! Close Help', command=help_window.destroy).place(x=260, y=150)

def open_year_overview_window():
    """Opens year overview window that summarizes this year's data.
    """
    # under construction
    year_overview_window = Toplevel()
    year_overview_window.title("Year overview")
    year_overview_window.geometry("670x500")
    progress_bar = ttk.Progressbar(year_overview_window, orient=HORIZONTAL, length=200,
            value=0, mode='determinate')
    label_ai_analyzes_year = Label(master=year_overview_window,
        text='Please wait while Artificial Intelligence analyzes your budget')
    label_ai_analyzes_year.place(x=120, y=150)
    progress_bar.place(x=220, y=200)
    progress_bar.after(1000, lambda: progress_bar.config(value=20))
    progress_bar.after(2000, lambda: progress_bar.config(value=40))
    progress_bar.after(3000, lambda: progress_bar.config(value=60))
    progress_bar.after(4000, lambda: progress_bar.config(value=80))
    progress_bar.after(5000, lambda: progress_bar.config(value=100))
    progress_bar.after(7000, lambda: progress_bar.destroy())
    label_ai_analyzes_year.after(7000, lambda: label_ai_analyzes_year.destroy())

    # data comes here
    Button(year_overview_window, text='Close overview',
        command=year_overview_window.destroy).place(x=260, y=400)

def create_column_titles(frame_main):
    """Creating column title that are on first row of each column.
    """
    label_item_category = Label(master=frame_main, text='CATEGORY')
    label_item_category.grid(row=3, column=0, sticky="w")
    label_planned_column = Label(master=frame_main, text='PLANNED')
    label_planned_column.grid(row=3, column=1)
    label_receivedspent_column = Label(master=frame_main, text='RECEIVED / SPENT')
    label_receivedspent_column.grid(row=3, column=2)

def create_category_column_texts(frame_main):
    """Creating texts that are in the CATEGORY column.
    """
    label_income = Label(master=frame_main, text='Income')
    label_rent = Label(master=frame_main, text='Rent / mortgage')
    label_bills = Label(master=frame_main, text='Bills')
    label_spending = Label(master=frame_main, text='Spending')
    label_debt_service = Label(master=frame_main, text='Debt service')
    label_saving = Label(master=frame_main, text='Saving')
    label_income.grid(row=4, column=0, sticky="w")
    label_rent.grid(row=5, column=0, sticky="w")
    label_bills.grid(row=6, column=0, sticky="w")
    label_spending.grid(row=7, column=0, sticky="w")
    label_debt_service.grid(row=8, column=0, sticky="w")
    label_saving.grid(row=9, column=0, sticky="w")
