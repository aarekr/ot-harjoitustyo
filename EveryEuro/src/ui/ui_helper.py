""" User Interface helper functions """

from tkinter import ttk, Menu, Frame, Toplevel, Label, Text, Button, LEFT, RIGHT, SUNKEN, HORIZONTAL
from tkinter.messagebox import showerror

def create_menu_bar(root):
    """ Creating menu bar in the top part on the window. """
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

def create_column_titles(frame_main):
    """ Creating column title that are on first row of each column. """
    label_item_category = Label(master=frame_main, text='CATEGORY')
    label_item_category.grid(row=3, column=0, sticky="w")
    label_planned_column = Label(master=frame_main, text='PLANNED')
    label_planned_column.grid(row=3, column=1)
    label_receivedspent_column = Label(master=frame_main, text='RECEIVED / SPENT')
    label_receivedspent_column.grid(row=3, column=2)

def create_category_column_texts(frame_main):
    """ Creating texts that are in the CATEGORY column. """
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

def open_help_window():
    """ Opens help window that explains how to use the program. """
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

def open_year_overview_window(table_all_months_planned):
    """ Opens year overview window that summarizes this year's data. """
    # under construction
    year_overview_window = Toplevel()
    year_overview_window.title("Year overview")
    year_overview_window.geometry("670x500")
    progress_bar = ttk.Progressbar(year_overview_window, orient=HORIZONTAL, length=200,
            value=0, mode='determinate')
    label_ai_analyzes_year = Label(master=year_overview_window,
        text='Please wait while Artificial Intelligence analyzes your budget')
    label_ai_analyzes_year.place(x=120, y=150)
    label_year_summary = Label(master=year_overview_window)
    label_year_summary.place(x=10, y=10)
    progress_bar.place(x=220, y=200)
    progress_bar.after(1000, lambda: progress_bar.config(value=20))
    progress_bar.after(2000, lambda: progress_bar.config(value=40))
    progress_bar.after(3000, lambda: progress_bar.config(value=60))
    progress_bar.after(4000, lambda: progress_bar.config(value=80))
    progress_bar.after(5000, lambda: progress_bar.config(value=100))
    progress_bar.after(7000, lambda: progress_bar.destroy())
    label_ai_analyzes_year.after(7000, lambda: label_ai_analyzes_year.destroy())
    label_year_summary.after(8000,
        lambda: show_year_summary(table_all_months_planned, year_overview_window))

    # data should be loaded from the my_budget.csv file?
    Button(year_overview_window, text='Close overview',
        command=year_overview_window.destroy).place(x=260, y=400)

def show_year_summary(table_all_months_planned, year_overview_window):
    label_year_summary_title = Label(master=year_overview_window, text="Your year analyzed")
    label_year_summary_title.place(x=20, y=20)
    count_rent_above_25_per_cent_of_income = 0
    for i in range(1, 13):
        print(table_all_months_planned[i].get_month_name())
        income = table_all_months_planned[i].get_income()
        rent = table_all_months_planned[i].get_rent()
        if income == 0:  # avoiding ZeroDivisionError
            income = 0.01
        if rent / income > 0.25:
            count_rent_above_25_per_cent_of_income += 1
    label_rent_comment = Label(master=year_overview_window, text="Rent:")
    label_rent_comment.place(x=40, y=50)

def bar_item_notdone():  # this function will not be in the final version
    """ Shows an error window for functionalities that are not yet implemented. """
    showerror('Not implemented', 'Functionality not yet available, but coming soon')
