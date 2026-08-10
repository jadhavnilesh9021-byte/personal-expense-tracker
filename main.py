import database
import expense_manager
import report
from utils import is_valid_amount, is_valid_category, is_valid_date, normalize_date


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if is_valid_date(date):
            return normalize_date(date)
        print("❌ Date must be in YYYY-MM-DD format. Try again.")

def show_menu():
    print("\n==== Personal Expense Tracker ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Filter by Category")
    print("6. Summary Report")
    print("7. Export to CSV")
    print("8. Generate Category Chart")
    print("9. Exit")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if is_valid_amount(amount):
                return amount
            print("❌ Amount must be a positive number. Try again.")
        except ValueError:
            print("❌ Invalid input — please enter a number.")


def get_valid_category():
    while True:
        category = input("Enter category: ")
        if is_valid_category(category):
            return category.strip()
        print("❌ Category must contain only letters (no numbers/symbols). Try again.")


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if is_valid_date(date):
            return normalize_date(date)
        print("❌ Date must be in YYYY-MM-DD format. Try again.")


def handle_add_expense():
    amount = get_valid_amount()
    category = get_valid_category()
    date = get_valid_date()
    note = input("Enter note (optional): ")

    try:
        expense_manager.add_expense(amount, category, date, note)
        print("✅ Expense added successfully!")
    except expense_manager.InvalidExpenseError as e:
        print(f"❌ {e}")


def handle_view_expenses():
    expenses = expense_manager.get_all_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nID | Amount | Category | Date | Note")
    print("-" * 50)
    for exp in expenses:
        exp_id, amount, category, date, note = exp
        print(f"{exp_id} | ₹{amount} | {category} | {date} | {note}")


def handle_update_expense():
    handle_view_expenses()
    try:
        expense_id = int(input("\nEnter ID of expense to update: "))
    except ValueError:
        print("❌ Invalid ID.")
        return

    existing = expense_manager.get_expense_by_id(expense_id)
    if not existing:
        print(f"❌ No expense found with id {expense_id}.")
        return

    amount = get_valid_amount()
    category = get_valid_category()
    date = get_valid_date()
    note = input("Enter note (optional): ")

    try:
        expense_manager.update_expense(expense_id, amount, category, date, note)
        print("✅ Expense updated successfully!")
    except expense_manager.InvalidExpenseError as e:
        print(f"❌ {e}")


def handle_delete_expense():
    handle_view_expenses()
    try:
        expense_id = int(input("\nEnter ID of expense to delete: "))
        expense_manager.delete_expense(expense_id)
        print("✅ Expense deleted successfully!")
    except ValueError:
        print("❌ Invalid ID.")
    except expense_manager.InvalidExpenseError as e:
        print(f"❌ {e}")


def handle_filter_by_category():
    category = input("Enter category to filter by: ")
    expenses = expense_manager.get_expenses_by_category(category)

    if not expenses:
        print("No expenses found in this category.")
        return

    print("\nID | Amount | Category | Date | Note")
    print("-" * 50)
    for exp in expenses:
        exp_id, amount, cat, date, note = exp
        print(f"{exp_id} | ₹{amount} | {cat} | {date} | {note}")


def handle_summary_report():
    print(report.generate_summary())


def handle_export_csv():
    filename = report.export_to_csv()
    print(f"✅ Expenses exported to '{filename}' successfully!")


def handle_generate_chart():
    filename = report.generate_category_chart()
    if filename:
        print(f"✅ Chart saved as '{filename}'. Open it to view your spending breakdown.")
    else:
        print("No expenses to chart yet.")

def main():
    database.create_table()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            handle_add_expense()
        elif choice == "2":
            handle_view_expenses()
        elif choice == "3":
            handle_update_expense()
        elif choice == "4":
            handle_delete_expense()
        elif choice == "5":
            handle_filter_by_category()
        elif choice == "6":
            handle_summary_report()
        elif choice == "7":
            handle_export_csv()
        elif choice == "8":
            handle_generate_chart()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()