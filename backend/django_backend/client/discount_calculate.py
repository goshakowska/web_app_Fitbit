from datetime import datetime, date

def calcucate_price_after_discount(price_before, discount):
    return price_before * (100 - discount) / 100

def str_date(date_obj):
    return date_obj.strftime("%Y-%m-%d") if date_obj else None

def str_hour(time_obj):
    return time_obj.strftime("%H:%M:%S") if time_obj else None
