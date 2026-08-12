from datetime import datetime


def format_statement_date(timestamp):
    date_time = datetime.fromisoformat(timestamp)

    return date_time.strftime("%d/%m/%Y %H:%M")