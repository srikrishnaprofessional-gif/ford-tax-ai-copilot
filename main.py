from agents.tax_agent import calculate_tax

transaction = {
    "location": "US",
    "amount": 40000
}

tax = calculate_tax(transaction)

print("Calculated Tax:", tax)