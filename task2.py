import csv
import os

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            return list(reader)
    return []

def save_data(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def display_menu():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense List")
    print("5. Exit")

def add_income(data):
    amount = float(input("Enter income amount: "))
    category = input("Enter income category: ")
    data.append(['Income', category, amount])
    print("Income added successfully!")

def add_expense(data):
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    data.append(['Expense', category, amount])
    print("Expense added successfully!")

def calculate_budget(data):
    total_income = sum(float(row[2]) for row in data if row[0] == 'Income')
    total_expense = sum(float(row[2]) for row in data if row[0] == 'Expense')
    return total_income - total_expense

def expense_analysis(data):
    categories = set(row[1] for row in data if row[0] == 'Expense')
    print("\nExpense List:")
    for category in categories:
        total_amount = sum(float(row[2]) for row in data if row[0] == 'Expense' and row[1] == category)
        print(f"{category}: ${total_amount:.2f}")
    print()

def main():
    file_path = 'budget_data.csv'
    data = load_data(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            remaining_budget = calculate_budget(data)
            print(f"\nRemaining Budget: ${remaining_budget:.2f}\n")
        elif choice == '4':
            expense_analysis(data)
        elif choice == '5':
            save_data(file_path, data)
            print("Budget data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
