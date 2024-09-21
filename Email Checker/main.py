def is_valid_email(email):
    if len(email) < 6:
        return "Error: Email is too short."
    
    if not email[0].isalpha():
        return "Error: Email must start with a letter."
    
    if email.count("@") != 1:
        return "Error: Email must contain exactly one '@' symbol."
    
    if not (email[-4] == "." or email[-3] == "."):
        return "Error: Email must have a dot (.) in the correct place."
    
    # Checking for unwanted characters
    k, d, j = 0, 0, 0
    for char in email:
        if char.isspace():
            k = 1
        elif char.isalpha() and char.isupper():
            j = 1
        elif not (char.isdigit() or char == "@" or char == "." or char == "_"):
            d = 1
    
    if k == 1:
        return "Error: Email contains whitespace."
    if j == 1:
        return "Error: Email contains uppercase letters."
    if d == 1:
        return "Error: Email contains invalid characters."
    
    return "Email is valid."

# Driver code
email = input("Enter your Email: ")
print(is_valid_email(email))
