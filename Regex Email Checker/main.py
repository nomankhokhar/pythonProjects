# Program to Check Email is Follow the Pattern or Not

import re

email_condition = r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

def validate_email(email):
    if re.search(email_condition, email):
        return "Right Email"
    else:
        return "Not right Email"

def run_tests():
    test_cases = [
        ("test@example.com", "Right Email"),
        ("test123@example.co", "Right Email"),
        ("first.last@example.org", "Right Email"),
        ("user_name@domain.com", "Right Email"),

        ("Test@Example.Com", "Not right Email"),        # Uppercase letters
        ("test@.com", "Not right Email"),               # Missing domain name
        ("test@domain.c", "Not right Email"),           # TLD too short
        ("@example.com", "Not right Email"),            # Missing username
        ("test@examplecom", "Not right Email"),         # Missing dot in domain
        ("test@domain.abcde", "Not right Email"),       # TLD too long
        ("test..email@domain.com", "Not right Email"),  # Consecutive dots in the local part
        ("test_email@", "Not right Email"),             # Missing domain
        ("test@domain..com", "Not right Email")         # Double dots in domain
    ]

    for email, expected in test_cases:
        result = validate_email(email)
        assert result == expected, f"Test failed for: {email}. Expected: {expected}, but got: {result}"
    
    print("All tests passed.")

run_tests()
