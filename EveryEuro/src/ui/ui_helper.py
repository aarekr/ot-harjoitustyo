""" User Interface helper functions """

from tkinter import ttk, Menu, Frame, Toplevel, Label, Text, Button, LEFT, RIGHT, SUNKEN, \
    HORIZONTAL, StringVar
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

def open_year_overview_window(table_all_months_receivedspent):
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
        lambda: show_year_summary(table_all_months_receivedspent, year_overview_window))

    # data should be loaded from the my_budget.csv file?
    Button(year_overview_window, text='Close overview',
        command=year_overview_window.destroy).place(x=260, y=400)

def show_year_summary(table_all_months_receivedspent, year_overview_window):
    frame_summary = Frame(master=year_overview_window, borderwidth=1)
    frame_summary.grid(row=0, column=0, padx=10, pady=10)
    label_year_summary_title = Label(master=frame_summary, text="Your year analyzed:", font=12)
    label_year_summary_title.grid(row=1, column=0)
    count_months_filled_in = 0
    sum_total_income = 0
    sum_total_rent = 0
    sum_total_bills = 0
    sum_total_spending = 0
    sum_total_debt_service = 0
    sum_total_saving = 0
    count_months_rent_above_25_per_cent_of_income = 0
    count_months_saving_positive = 0
    for i in range(1, 13):
        income = table_all_months_receivedspent[i].get_income()
        rent = table_all_months_receivedspent[i].get_rent()
        bills = table_all_months_receivedspent[i].get_bills()
        spending = table_all_months_receivedspent[i].get_spending()
        debt_service = table_all_months_receivedspent[i].get_debt_service()
        saving = table_all_months_receivedspent[i].get_saving()
        sum_total_income += income
        sum_total_rent += rent
        if rent / (0.1 if income == 0 else income) > 0.25:
            count_months_rent_above_25_per_cent_of_income += 1
        sum_total_bills += bills
        sum_total_spending += spending
        sum_total_debt_service += debt_service
        sum_total_saving += saving
        if saving > 0:
            count_months_saving_positive += 1
        if income != 0:
            count_months_filled_in += 1
        if count_months_filled_in == 0:
            count_months_filled_in = 1
        if sum_total_income == 0:
            sum_total_income = 1

    # analyze text items
    label_income = Label(master=frame_summary, text="Your average monthly income")
    label_rent = Label(master=frame_summary, text="Rent percentage of income")
    label_bills = Label(master=frame_summary, text="Bills in total")
    label_spending = Label(master=frame_summary, text="Spending percentage of income")
    label_debt_service = Label(master=frame_summary, text="Debt service total")
    label_saving = Label(master=frame_summary, text="Saving positive months")
    label_income.grid(row=2, column=1, sticky="w")
    label_rent.grid(row=3, column=1, sticky="w")
    label_bills.grid(row=4, column=1, sticky="w")
    label_spending.grid(row=5, column=1, sticky="w")
    label_debt_service.grid(row=6, column=1, sticky="w")
    label_saving.grid(row=7, column=1, sticky="w")

    # analyze number items
    average_income = int(sum_total_income / count_months_filled_in)
    label_income_average = Label(master=frame_summary, text=str(average_income))
    label_income_average.grid(row=2, column=2, padx=10)
    rent_percentage_of_income = 100 * sum_total_rent / sum_total_income
    str_rent_percentage = f"{rent_percentage_of_income:.2f}%"
    label_rent_percentage = Label(master=frame_summary, text=str_rent_percentage)
    label_rent_percentage.grid(row=3, column=2, padx=10)
    label_bills_total = Label(master=frame_summary, text=str(sum_total_bills))
    label_bills_total.grid(row=4, column=2, padx=10)
    spending_percentage_of_income = 100 * sum_total_spending /sum_total_income
    str_spending_percentage = f"{spending_percentage_of_income:.2f}%"
    label_spending_percentage = Label(master=frame_summary, text=str_spending_percentage)
    label_spending_percentage.grid(row=5, column=2, padx=10)
    label_debt_service_total = Label(master=frame_summary, text=str(sum_total_debt_service))
    label_debt_service_total.grid(row=6, column=2)
    label_saving_positive_month_count = Label(master=frame_summary,
        text=str(count_months_saving_positive))
    label_saving_positive_month_count.grid(row=7, column=2)

    # comments part
    label_comments = Label(master=frame_summary, text="Comments:")
    label_comments.grid(row=9, column=0, sticky="w")
    if count_months_rent_above_25_per_cent_of_income > 0:
        label_rent_per_income_too_high = Label(master=frame_summary,
            text=f"Your rent / morgage might be too high!", fg="red")
        label_rent_per_income_too_high.grid(row=10, column=1, sticky="w", columnspan=2)
    if spending_percentage_of_income > 30:
        label_spending_too_much = Label(master=frame_summary,
            text="Your spending is out of control!", fg="red")
        label_spending_too_much.grid(row=11, column=1, sticky="w")
    if count_months_saving_positive == 12:
        label_saving_every_month = Label(master=frame_summary,
            text="Excellent! You are saving every month.", fg="green")
        label_saving_every_month.grid(row=12, column=1, sticky="w")

def bar_item_notdone():  # this function will not be in the final version
    """ Shows an error window for functionalities that are not yet implemented. """
    showerror('Not implemented', 'Functionality not yet available, but coming soon')
