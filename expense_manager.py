import database
from utils import is_valid_date, is_valid_amount, is_valid_category, is_valid_note
class InvalidExpenseError(Exception):
    """Raised when expense data fails validation."""
    pass


def add_expense(amount, category, date, note=""):
    """Validates input, then saves the expense via the database layer."""
    if not is_valid_amount(amount):
        raise InvalidExpenseError("Amount must be a positive number.")

    if not is_valid_category(category):
        raise InvalidExpenseError("Category must contain only letters (no numbers or symbols).")

    if not is_valid_date(date):
        raise InvalidExpenseError("Date must be in YYYY-MM-DD format.")

    if not is_valid_note(note):
        raise InvalidExpenseError("Note must be under 200 characters.")

    database.insert_expense(amount, category.strip(), date, note.strip())
    return True


def get_all_expenses():
    """Returns all expenses from the database."""
    return database.fetch_all_expenses()


def update_expense(expense_id, amount, category, date, note=""):
    """Validates input, then updates the expense via the database layer."""
    if not is_valid_amount(amount):
        raise InvalidExpenseError("Amount must be a positive number.")
    if not is_valid_category(category):
        raise InvalidExpenseError("Category must contain only letters (no numbers or symbols).")
    if not is_valid_date(date):
        raise InvalidExpenseError("Date must be in YYYY-MM-DD format.")
    if not is_valid_note(note):
        raise InvalidExpenseError("Note must be under 200 characters.")

    success = database.update_expense(expense_id, amount, category.strip(), date, note.strip())
    if not success:
        raise InvalidExpenseError(f"No expense found with id {expense_id}.")
    return True


def delete_expense(expense_id):
    """Deletes an expense via the database layer."""
    success = database.delete_expense(expense_id)
    if not success:
        raise InvalidExpenseError(f"No expense found with id {expense_id}.")
    return True


def get_expenses_by_category(category):
    return database.fetch_by_category(category.strip())


def get_expense_by_id(expense_id):
    """Returns a single expense, or None if it doesn't exist."""
    return database.fetch_by_id(expense_id)