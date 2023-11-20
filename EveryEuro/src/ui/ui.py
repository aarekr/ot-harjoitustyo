from tkinter import Tk, ttk, constants, StringVar

class UI:
    """ Application User Interface """

    def __init__(self, root):
        self._root = root
        self._left_to_budget = None
        self._income_entry = None
        self._bills_entry = None
        self._spending_entry = None
        self._debt_entry = None

    def start(self):
        self._left_to_budget = StringVar()
        self._left_to_budget_text = StringVar()
        self._column_title_type = StringVar()
        self._column_title_planned = StringVar()
        self._left_to_budget.set("0")
        self._left_to_budget_text.set("<- left to budget")
        self._column_title_type.set("TYPE")
        self._column_title_planned.set("PLANNED")
        self._column_title_type_label = ttk.Label(master=self._root, textvariable=self._column_title_type)
        left_to_budget_label = ttk.Label(master=self._root, textvariable=self._left_to_budget)
        left_to_budget_text_label = ttk.Label(master=self._root, textvariable=self._left_to_budget_text)
        column_title_type_label = ttk.Label(master=self._root, textvariable=self._column_title_type)
        column_title_planned_label = ttk.Label(master=self._root, textvariable=self._column_title_planned)
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
        self._income_entry = ttk.Entry(master=self._root)
        self._bills_entry = ttk.Entry(master=self._root)
        self._spending_entry = ttk.Entry(master=self._root)
        self._debt_entry = ttk.Entry(master=self._root)
        balance_button = ttk.Button(
            master=self._root,
            text="Calculate balance",
            command=self.calculate_budget_balance
        )

        # 'Spent' entry fields

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
        empty_space_label.grid(row=2, column=0, columnspan=1)

        income_text.grid(row=4, column=1, sticky=constants.W)
        self._income_entry.grid(row=4, column=2)
        bills_text.grid(row=5, column=1, sticky=constants.W)
        self._bills_entry.grid(row=5, column=2)
        spending_text.grid(row=6, column=1, sticky=constants.W)
        self._spending_entry.grid(row=6, column=2)
        debt_text.grid(row=7, column=1, sticky=constants.W)
        self._debt_entry.grid(row=7, column=2)
        balance_button.grid(row=8, column=2)

    def calculate_budget_balance(self):
        budget_balance = (int(self._income_entry.get())
                        - int(self._bills_entry.get())
                        - int(self._spending_entry.get())
                        - int(self._debt_entry.get()))
        print(f"budget_balance is: {budget_balance}")
        self.update_left_to_budget(budget_balance)

    def update_left_to_budget(self, budget_balance):
        self._left_to_budget.set(str(budget_balance))
