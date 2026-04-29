class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({
            "category": category,
            "amount": amount
        })

    def show_expenses(self):
        print("\n💸 Expense List:")
        for e in self.expenses:
            print(f"{e['category']} - ₹{e['amount']}")

    def total_spent(self):
        return sum(e["amount"] for e in self.expenses)

class AIAdvisor:
    def __init__(self, tracker):
        self.tracker = tracker

    def analyze(self):
        if not self.tracker.expenses:
            return "No expenses recorded."

        total = self.tracker.total_spent()

        food = sum(e["amount"] for e in self.tracker.expenses if e["category"] == "food")
        shopping = sum(e["amount"] for e in self.tracker.expenses if e["category"] == "shopping")

        if shopping > food:
            return "You spend more on shopping. Try budgeting 🛍️"
        elif food > 1000:
            return "High food expense! Consider cooking at home 🍲"
        else:
            return "Good spending habits 👍"

def main():
    tracker = ExpenseTracker()
    ai = AIAdvisor(tracker)

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. AI Suggestion")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            category = input("Enter category (food/shopping/other): ").lower()
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, amount)
            print("✅ Expense added!")

        elif choice == "2":
            tracker.show_expenses()
            print("Total Spent: ₹", tracker.total_spent())

        elif choice == "3":
            print("🤖 AI:", ai.analyze())

        elif choice == "4":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
