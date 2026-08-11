def calculate_loan(credit_score, annual_income, debt_ratio):

    if credit_score >= 750 and annual_income >= 5000000 and debt_ratio <= 0.30:
        status = "Approved"
        interest_rate = 8

    elif credit_score >= 650 and annual_income >= 3000000 and debt_ratio <= 0.40:
        status = "Approved"
        interest_rate = 10

    elif credit_score >= 600 and annual_income >= 2000000 and debt_ratio <= 0.50:
        status = "Approved"
        interest_rate = 12

    else:
        status = "Rejected"
        interest_rate = 0

    return status, interest_rate