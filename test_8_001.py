
"""
Программа для вериффикации паролей
"""

def valid_password(password):
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    if len(password) >= 7:
        correct_length = True
        for item in password:
            if item.isupper():
                has_uppercase = True
            if item.islower():
                has_lowercase = True
            if item.isdigit():
                has_digit = True
        if correct_length and has_uppercase and \
            has_lowercase and has_digit:
            is_valid = True
    else:
        is_valid = False
    return is_valid


