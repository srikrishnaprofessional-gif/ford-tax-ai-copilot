import pandas as pd

def check_invoice_vs_po():

    invoices = pd.read_csv("data/invoices.csv")

    issues = invoices[invoices["invoice_amount"] > invoices["po_amount"]]

    return issues