from datetime import datetime, timedelta 

high_risk_countries = ["RU", "KP", "IR"]
velocity_window_hours = 24
velocity_limit = 3

def evaluate_risk(amount, country_code, is_first_time):
    risk = False

    if amount > 100000:
        risk = True

    if country_code in high_risk_countries:
        risk =True
    
    if is_first_time and amount > 100000:
        risk = True

    return risk

def check_velocity(transactions, customer):
    current_time = datetime.now()
    time_limit = current_time -timedelta(hours=velocity_window_hours)

    recent_transactions = 0

    for transaction in transactions:
        if transaction["name"].lower() == customer.lower():
            transaction_time = datetime.fromisoformat(
                transaction["timestamp"]
            )

            if transaction_time >= time_limit:
                recent_transactions += 1

    return recent_transactions >= velocity_limit
