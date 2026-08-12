def convert_currency(amount):

    rates = {
        "USD": 1350,
        "EUR": 1550,
        "GBP": 1860
    }

    transaction_fee = 0.02

    results = {}

    for currency, rate in rates.items():

        converted_amount = amount / rate

        fee = converted_amount * transaction_fee

        final_amount = converted_amount - fee

        results[currency] = round(final_amount, 2)

    return results