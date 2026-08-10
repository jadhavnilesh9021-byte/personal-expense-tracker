class Expense:
    """
    Represents a single expense record.
    This class does NOT talk to the database — it's just a data structure.
    """

    def __init__(self, amount, category, date, note="", expense_id=None):
        self.id = expense_id       # None until saved in DB, then DB assigns an ID
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def __repr__(self):
        return (f"Expense(id={self.id}, amount={self.amount}, "
                f"category='{self.category}', date='{self.date}', note='{self.note}')")