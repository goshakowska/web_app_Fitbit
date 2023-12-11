import string

def validate_password(password):
    """
    Function checks whether password contains a special character, number
    lowercase and uppercase letters
    """
    if len(password) < 8:
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.islower() for char in password):
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char in set(string.punctuation) for char in password):
        return False
    return True