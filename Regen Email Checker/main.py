# Program to Check Email is Follow the Pattern or Not

import re

email_condition = r"^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

def validate_email(email):
    if re.search(email_condition, email):
        return "Right Email"
    else:
        return "Not right Email"
