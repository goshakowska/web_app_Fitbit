import datetime

def calcucate_price_after_discount(price_before, discount):
    return price_before * (100 - discount) / 100

def str_date(date):
    return datetime.strptime(date, "%Y-%m-%d") if date else None

def str_hour(date):
    return datetime.strptime(date, "%H:%M:%S") if date else None
