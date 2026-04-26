import os
import pandas as pd
from datetime import datetime

FILENAME = "file.xlsx"

def load_data():
    if os.path.exists(FILENAME):
        return pd.read_excel(FILENAME)
    return pd.DataFrame(columns=['Party', 'Date', 'Category', 'Type', 'Amount'])

def save_data(df):
    df.to_excel(FILENAME, index=False)

def process_entry(df, party, category, trans_type, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    new_row = pd.DataFrame({
        'Party': [party.lower()], 
        'Date': [date], 
        'Category': [category], 
        'Type': [trans_type.capitalize()], 
        'Amount': [amount]
    })
    return pd.concat([df, new_row], ignore_index=True)

def get_party_stats(df, party_name):
    party_df = df[df['Party'] == party_name.lower()]
    if party_df.empty:
        return None
    
    bills = party_df[party_df['Type'] == 'Bill']['Amount'].sum()
    payments = party_df[party_df['Type'] == 'Payment']['Amount'].sum()
    return {"bills": bills, "payments": payments, "net": bills - payments}