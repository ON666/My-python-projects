import re

def check_password_strength(password):
    min_length = 8
    length_ok = len(password) >= min_length
    upper_ok = re.search(r'[A-Z]', password) is not None
    lower_ok = re.search(r'[a-z]', password) is not None
    digit_ok = re.search(r'[0-9]', password) is not None
    special_ok = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    if all([length_ok, upper_ok, lower_ok, digit_ok, special_ok]):
        return "Your password is strong."
    elif length_ok and (upper_ok or lower_ok) and digit_ok:
        return "Your password is moderate. Consider adding special characters for better security."
    elif length_ok and (upper_ok or lower_ok or digit_ok):
        return "Your password is weak. Consider adding numbers, uppercase letters, and special characters."
    else:
        return "Your password is very weak. It should be at least 8 characters long and include uppercase letters, lowercase letters, numbers, and special characters."

def main():
    password = input("Enter a password to check its strength: ")
    feedback = check_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
