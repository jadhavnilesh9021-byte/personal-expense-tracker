from datetime import datetime


def is_valid_date(date_str):
    """Checks if a string is a valid date in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def normalize_date(date_str):
    """Converts a valid date string into a consistent zero-padded YYYY-MM-DD format."""
    parsed = datetime.strptime(date_str, "%Y-%m-%d")
    return parsed.strftime("%Y-%m-%d")


def is_valid_amount(amount):
    """Checks if amount is a positive number."""
    return isinstance(amount, (int, float)) and amount > 0


def is_valid_category(category):
    """Checks that category contains only letters and spaces (no numbers/symbols)."""
    if not category or not category.strip():
        return False
    return all(char.isalpha() or char.isspace() for char in category.strip())


def is_valid_note(note, max_length=200):
    """Note is optional but must not exceed a reasonable length."""
    return len(note.strip()) <= max_length