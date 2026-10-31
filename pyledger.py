from datetime import datetime
def show_options():
    print("1.Add Transaction")
    print("2.List Transaction")
    print("3.Edit Transaction")
    print("4.Delete Transaction")
    print("5.Summary Report")
    print("6.Category Budgets")
    print("7.Search Transactions")
    print("8.Export to CSV")
    print("9.Quit")

def add_transaction(info):
    while True:
        trans_type = input("Transaction type (income/expense): ").strip().lower()
        if trans_type in ["income", "expense"]:
            break
        else:
            print("invalid transaction try again...")
    while True:
        try:
            a = input("Transaction amount: ")
            amount = float(a)
            if amount > 0:
                break
            else:
                print("Amount must be positive...")
        except ValueError:
            print("Please type in a NUMBER amount...")     
    while True:
        category = input("Transaction category: ").strip()
        if category:
            break
        else:
            print("Category cannot be empty...")
    while True:
        try:
            date = input("Transaction date (YYYY-MM-DD): ")
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD...")
    while True:
        description = input("Transaction description: ").strip()
        if description:
            break
        else:
            print("Description cannot be empty...")
    ids = [t["id"] for t in info]
    new_id = max(ids, default=0) + 1
    transaction = {"id": new_id,
    "date": date,
    "type": trans_type,
    "amount": amount,
    "category": category,
    "description": description,}
    info.append(transaction)
    print(f"Added:(id: {new_id}) {description} ({amount:.2f})")
##############################################################################
def list_filter(info):
    if not info:
        print("No transactions yet...")
        return
    print("Filter by: 1.All  2.Month  3.Category  4.Type")
    choice = input("Choose 1-4: ").strip()
    if choice == "1":
        results = info

    elif choice == "2":
        try:
            month = int(input("Type in a month (1-12): "))
        except ValueError:
            print("Please type a number from 1 to 12...")
            return
        results = []
        for t in info:
            if int(t["date"][5:7]) == month:
                results.append(t)

    elif choice == "3":
        category = input("Category: ").strip()
        results = []
        for t in info:
            if t["category"].lower() == category.lower():   
                results.append(t)

    elif choice == "4":
        trans_type = input("Type (income/expense): ").strip().lower()
        results = []
        for t in info:
            if t["type"] == trans_type:
                results.append(t)  

    else:
        print("That filter isn't available yet...")
        return 

    if not results:
        print("No matching transactions...")
        return

    for t in results:
        print(f"[{t['id']}] {t['date']} | {t['type']} | {t['amount']:.2f} | {t['category']} | {t['description']}")


##############################################################################
def main_menu():
    storage = []
    while True:
        show_options()
        action = input("Choose an action 1-9: ")
        if action == "1":
            add_transaction(storage)
        elif action == "2":
            list_filter(storage)
        elif action == "3":   
            print("edit")
        elif action == "4":
            print("delete")
        elif action == "5":
            print("summary")
        elif action == "6":
            print("category")
        elif action == "7":
            print("search")
        elif action == "8":
            print("export")
        elif action == "9":
            break
        else:
            print("Invalid input, input must be 1-9: ")
            continue
        
if __name__ == "__main__":
    main_menu()
