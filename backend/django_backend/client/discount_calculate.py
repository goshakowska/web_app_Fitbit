from datetime import datetime, date

def calculate_price_after_discount(price_before, discount):
    """
    Calculate the price after applying a discount.

    Args:
        price_before (int): The original price.
        discount (int): The discount percentage.

    Returns:
        float: The discounted price.
    """
    return price_before * (100 - discount) / 100


def str_date(date_obj):
    """
    Convert a date object to a formatted string.

    Args:
        date_obj (datetime): The date object to be formatted.

    Returns:
        str: The formatted date string.
    """
    return date_obj.strftime("%Y-%m-%d") if date_obj else None


def str_hour(time_obj):
    """
    Convert a time object to a formatted string.

    Args:
        time_obj (datetime): The time object to be formatted.

    Returns:
        str: The formatted time string.
    """
    return time_obj.strftime("%H:%M:%S") if time_obj else None