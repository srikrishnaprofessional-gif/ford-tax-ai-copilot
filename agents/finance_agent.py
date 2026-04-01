import pandas as pd

def check_invoice_vs_po():

    invoices = pd.read_csv("data/invoices.csv")

    # Normalize column names
    invoices.columns = invoices.columns.str.strip().str.lower()

    issues = invoices[invoices["invoice_amount"] > invoices["po_amount"]]

    return issues