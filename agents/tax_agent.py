def calculate_tax(transaction):

    location = transaction["location"]
    amount = transaction["amount"]

    tax_rates = {
        "US": 0.08,
        "EU": 0.20,
        "India": 0.18
    }

    tax = amount * tax_rates.get(location, 0)

    return tax