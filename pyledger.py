from datetime import datetime
def show_options():
    print("1.Add Transaction")
    print("2.List/Filter Transaction")
    print("3.Edit/Delete Transaction")
    print("4.Summary Report")
    print("5.Category Budgets")
    print("6.Search Transactions")
    print("7.Save & Load")
    print("8.Export to CSV")
    print("9.Quit")

def add_transaction(info):
    while True:
        trans_type = input("Transaction type (income/expense/cancel): ").strip().lower()
        if trans_type == "cancel":
            print("Returning...")
            return 
        if trans_type in ["income", "expense", "cancel"]:
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
        category = input("Transaction category: ").strip().lower()
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
        description = input("Transaction description: ").strip().lower()
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
    print("Filter by: 0.Cancel 1.All  2.Month  3.Category  4.Type")
    choice = input("Choose 0-4: ").strip()
    if choice == "0":
        print("Returning...")
        return
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
##################################################################################################################
def edit_delete(info):
    if not info:
        print("No transactions yet...")
        return
    print("0.Cancel :: 1.Edit :: 2.Delete")
    choice = input("Choose 0-1-2: ").strip()
    if choice == "0":
        print("Returning")
        return
    if choice not in ["1", "2", "0"]:
        print("Invalid choice...")
        return
    while True:
        try:
            target_id = int(input("ID of the transaction to edit: "))
            break
            print("id received:", target_id)
        except ValueError:
            print("Please type a valid number ID...")
    print("id received:", target_id)
    for t in info:
        if t["id"] == target_id:
            if choice == "2":
                info.remove(t)
                print (f"Deleted transaction of ID -->({target_id})")
            elif choice == "1":
                while True:
                    new_category = input(f"Category ({t['category']}): ").strip()
                    if new_category:
                        t["category"] = new_category
                        break
                    else:
                        print("Category cannot be empty...")
                print(f"Updated transaction {target_id}.")
                while True:
                    new_description = input(f"Description ({t['description']}): ").strip()
                    if new_description:
                        t["description"] = new_description
                        break
                    else:
                        print("Description cannot be empty...")
                print(f"Updated transaction {target_id}")
                while True:
                    try:
                        new_a = input(f"Amount ({t['amount']}): ")
                        new_amount = float(new_a)
                        if new_amount > 0:
                            t["amount"] = new_amount
                            break
                        else:
                            print("Amount must be positive...")
                    except ValueError:
                        print("Please type in a NUMBER amount...")     
                print(f"Updated transaction {target_id}")
                while True:
                    try:
                        new_date = input(f"Date ({t['date']}): ")
                        datetime.strptime(new_date, "%Y-%m-%d")
                        t["date"] = new_date
                        break
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD...")
                print(f"Updated transaction {target_id}")
                while True:
                    new_trans_type = input(f"Transaction ({t['type']}): ").strip().lower()
                    if new_trans_type in ["income", "expense", "cancel"]:
                        t["type"] = new_trans_type
                        break
                    else:
                        print("invalid transaction try again...")
                print(f"Updated transaction {target_id}")
    print("No transaction with that id...")
##################################################################################################################
def summary(info):
    if not info:
        print("No transactions yet...")
        return
    incomes = 0
    expenses = 0
    categories = {}
    for t in info:
        if t["type"] == "income":
            incomes += t["amount"]
        else:
            expenses += t["amount"]
            if t["category"] not in categories:
                categories[t["category"]] = t["amount"]
            else:
                categories[t["category"]] = categories[t["category"]] + t["amount"]
    balance = incomes - expenses
    print(f"Total income:{incomes:.2f}\nTotal expenses:{expenses:.2f}\nTotal Balance: {balance}")
    if not categories:
        print("No expenses...")
    else:
        print("Category Expenses: ")
        for name, total in categories.items():
            print(f"{name}: {total}")

##################################################################################################################
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
            edit_delete(storage)
        elif action == "4":
            summary(storage)
        elif action == "5":
            print("category")
        elif action == "6":
            print("search")
        elif action == "7":
            print("Save and load")
        elif action == "8":
            print("export")
        elif action == "9":
            break
        else:
            print("Invalid input, input must be 1-9: ")
            continue
        
if __name__ == "__main__":
    main_menu()
