def detect_anomalies(transactions):

    if not transactions:
        return []

    total = 0

    for transaction in transactions:
        total += transaction["amount"]

    average = total / len(transactions)

    anomalies = []

    for transaction in transactions:

        if transaction["amount"] > average * 3:
            anomalies.append(transaction)

    return anomalies