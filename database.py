import sqlite3

DB_NAME = "expenses.db"


def get_connection():
    """Creates and returns a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)


def create_table():
    """Creates the expenses table if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
    """)
    conn.commit()
    conn.close()


def insert_expense(amount, category, date, note):
    """Inserts a new expense record into the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)",
        (amount, category, date, note)
    )
    conn.commit()
    conn.close()


def fetch_all_expenses():
    """Retrieves all expense records, sorted by date."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_expense(expense_id, amount, category, date, note):
    """Updates an existing expense by id."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE expenses SET amount = ?, category = ?, date = ?, note = ? WHERE id = ?",
        (amount, category, date, note, expense_id)
    )
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0


def delete_expense(expense_id):
    """Deletes an expense by id. Returns True if a row was deleted."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0


def fetch_by_category(category):
    """Retrieves expenses matching a specific category."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE category = ? ORDER BY date DESC", (category,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def fetch_total_spent():
    """Returns the total amount spent across all expenses."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0


def fetch_category_totals():
    """Returns total spending grouped by category."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    return rows


def fetch_by_id(expense_id):
    """Retrieves a single expense by id, or None if it doesn't exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    row = cursor.fetchone()
    conn.close()
    return row