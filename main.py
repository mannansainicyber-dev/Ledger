import os
import pandas as pd

filename = "file.xlsx"

def add_entry():
    print("--- New Entry ---")
    date = input("Enter Date (YYYY-MM-DD):  ")
    category = input("Category (e.g., Stock, Food, Rent): ")
    trans_type = input("Type (Bill or Payment): ").capitalize()
    party = input("Type Party Name: ").lower()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Error: Amount must be a number!")
        return
    
    new_data = {
        'Party': [party],
        'Date': [date],
        'Category': [category],
        'Type': [trans_type],
        'Amount': [amount]
    }
    new_df = pd.DataFrame(new_data)

    if os.path.exists(filename):
        existing_df = pd.read_excel(filename)
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
        updated_df.to_excel(filename, index=False)
    else:
        new_df.to_excel(filename, index=False)

    print(f"Successfully added {trans_type} for ${amount}!")