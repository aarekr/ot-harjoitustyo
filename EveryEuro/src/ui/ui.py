from tkinter import Tk, ttk, constants, StringVar
import entities.month

class UI:
    """ Application User Interface """

    def __init__(self, root):
        self._root = root
        self._left_to_budget = None
        self._income_planned = None
        self._bills_planned = None
        self._spending_planned = None
        self._debt_planned = None
        self._income_actual = None
        self._bills_actual = None
        self._spending_actual = None
        self._debt_actual = None

    def start(self):
        self._left_to_budget = StringVar()
        self._left_to_budget_text = StringVar()
        self._column_title_type = StringVar()
        self._column_title_planned = StringVar()
        self._column_title_actual = StringVar()
        self._left_to_budget.set("0")
        self._left_to_budget_text.set("<- left to budget")
        self._column_title_type.set("TYPE")
        self._column_title_planned.set("PLANNED")
        self._column_title_actual.set("ACTUAL")
        self._column_title_type_label = ttk.Label(master=self._root, textvariable=self._column_title_type)
        left_to_budget_label = ttk.Label(master=self._root, textvariable=self._left_to_budget)
        left_to_budget_text_label = ttk.Label(master=self._root, textvariable=self._left_to_budget_text)
        column_title_type_label = ttk.Label(master=self._root, textvariable=self._column_title_type)
        column_title_planned_label = ttk.Label(master=self._root, textvariable=self._column_title_planned)
        column_title_actual_label = ttk.Label(master=self._root, textvariable=self._column_title_actual)
        empty_space = StringVar()  # change this to a line
        empty_space.set("")
        empty_space_label = ttk.Label(master=self._root, textvariable=empty_space)

        # Type texts
        month = ttk.Label(master=self._root, text="November 2023")
        income_text = ttk.Label(master=self._root, text="Income")
        bills_text = ttk.Label(master=self._root, text="Bills")
        spending_text = ttk.Label(master=self._root, text="Spending")
        debt_text = ttk.Label(master=self._root, text="Debt")

        # 'Planned' entry fields
        self._income_planned = ttk.Entry(master=self._root)
        self._bills_planned = ttk.Entry(master=self._root)
        self._spending_planned = ttk.Entry(master=self._root)
        self._debt_planned = ttk.Entry(master=self._root)
        balance_button = ttk.Button(
            master=self._root,
            text="Calculate balance",
            command=self.update_view
        )

        # 'Actual' entry fields
        self._income_actual = ttk.Entry(master=self._root)
        self._bills_actual = ttk.Entry(master=self._root)
        self._spending_actual = ttk.Entry(master=self._root)
        self._debt_actual = ttk.Entry(master=self._root)

        # Placing items in the window
        month.grid(row=0, column=0, columnspan=2)
        month.grid(padx=5, pady=5)
        # to do: left to budget items should be placed better
        left_to_budget_label.grid(row=1, column=1)
        left_to_budget_text_label.grid(row=1, column=2)
        left_to_budget_label.grid(padx=5, pady=5)
        column_title_type_label.grid(row=3, column=1, sticky=constants.W)
        column_title_type_label.grid(padx=2, pady=5)
        column_title_planned_label.grid(row=3, column=2)
        column_title_actual_label.grid(row=3, column=3)
        empty_space_label.grid(row=2, column=0, columnspan=1)

        income_text.grid(row=4, column=1, sticky=constants.W)
        self._income_planned.grid(row=4, column=2)
        bills_text.grid(row=5, column=1, sticky=constants.W)
        self._bills_planned.grid(row=5, column=2)
        spending_text.grid(row=6, column=1, sticky=constants.W)
        self._spending_planned.grid(row=6, column=2)
        debt_text.grid(row=7, column=1, sticky=constants.W)
        self._debt_planned.grid(row=7, column=2)
        balance_button.grid(row=8, column=2)
        self._income_actual.grid(row=4, column=3)  # sticky doesn't function here?
        self._bills_actual.grid(row=5, column=3)
        self._spending_actual.grid(row=6, column=3)
        self._debt_actual.grid(row=7, column=3)

    def update_view(self):
        self.update_left_to_budget(entities.month.calculate_budget_balance(
            self._income_planned.get(),
            self._bills_planned.get(),
            self._spending_planned.get(),
            self._debt_planned.get()
        ))

    def update_left_to_budget(self, budget_balance):
        self._left_to_budget.set(str(budget_balance))
