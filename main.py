import logic

def run_menu():
    df = logic.load_data()

    while True:
        print("\n--- Business Ledger ---")
        choice = input("1. Add Entry\n2. Check Balance\n3. Save & Exit\nChoice: ")

        if choice == '1':
            p = input("Party Name: ")
            c = input("Category: ")
            t = input("Type (Bill/Payment): ")
            try:
                a = float(input("Amount: "))
                df = logic.process_entry(df, p, c, t, a)
                print("Entry processed in memory.")
            except ValueError:
                print("Invalid amount!")

        elif choice == '2':
            p = input("Enter Party Name: ")
            stats = logic.get_party_stats(df, p)
            if stats:
                print(f"\n--- {p.capitalize()} ---")
                print(f"Bills: {stats['bills']} | Paid: {stats['payments']}")
                print(f"Pending: {stats['net']}")
            else:
                print("No records found.")

        elif choice == '3':
            logic.save_data(df)
            print("Data saved to Excel. Goodbye!")
            break

if __name__ == "__main__":
    run_menu()