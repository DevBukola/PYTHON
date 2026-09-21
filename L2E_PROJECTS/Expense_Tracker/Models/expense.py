class Expense:
    def __init__(self, category, amount, description, id = None):
        self.category = category
        self.amount = amount
        self.description = description
        self.id = id