def calculate_investment(purchase_price, current_value, dividend_yield):
    
    roi = ((current_value - purchase_price) / purchase_price) * 100

    annualized_roi = roi

    quarterly_dividend = (
        purchase_price * (dividend_yield / 100)
    ) / 4

    return {
        "net_annualized_roi": round(annualized_roi, 2),
        "quarterly_dividend": round(quarterly_dividend, 2)
    }