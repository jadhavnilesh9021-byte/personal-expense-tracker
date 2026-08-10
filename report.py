import database
import csv
import database
import matplotlib.pyplot as plt


def generate_category_chart(filename="category_chart.png"):
    """Creates a bar chart of spending by category and saves it as an image."""
    category_totals = database.fetch_category_totals()

    if not category_totals:
        return None

    categories = [row[0] for row in category_totals]
    amounts = [row[1] for row in category_totals]

    plt.bar(categories, amounts, color="skyblue")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent (₹)")
    plt.title("Spending by Category")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    return filename


def export_to_csv(filename="expenses_export.csv"):
    """Exports all expenses to a CSV file. Returns the filename on success."""
    expenses = database.fetch_all_expenses()

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Amount", "Category", "Date", "Note"])
        for exp in expenses:
            writer.writerow(exp)

    return filename


def generate_summary():
    """Builds and returns a summary report as a formatted string."""
    total = database.fetch_total_spent()
    category_totals = database.fetch_category_totals()

    lines = ["\n==== Expense Summary ====", f"Total Spent: ₹{total}", "\nBy Category:"]
    for category, amount in category_totals:
        lines.append(f"  {category}: ₹{amount}")

    return "\n".join(lines)