class FinancialManagement:
    def __init__(self):
        self.income = 0
        self.expenses = 0

    def record_income(self, amount):
        self.income += amount

    def record_expense(self, amount):
        self.expenses += amount

    def generate_profit_loss_statement(self):
        profit_or_loss = self.income - self.expenses
        print(f"Total Income: {self.income}, Total Expenses: {self.expenses}, Profit/Loss: {profit_or_loss}")
