def reconcile_cash_flow(cash_flow):

    opening_balance = cash_flow["opening_balance"]
    transactions = cash_flow["transactions"]

    total_credits = 0
    total_debits = 0

    for transaction in transactions:

        if transaction["type"] == "credit":
            total_credits += transaction["amount"]

        elif transaction["type"] == "debit":
            total_debits += transaction["amount"]

    closing_balance = (
        opening_balance
        + total_credits
        - total_debits
    )

    net_change = closing_balance - opening_balance

    return {
        "opening_balance": opening_balance,
        "total_credits": total_credits,
        "total_debits": total_debits,
        "closing_balance": closing_balance,
        "net_change": net_change
    }