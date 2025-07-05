import re

password = input("Enter the password: ")

def check_password(password):
    if re.findall(r'[a-z]', password) and \
        re.findall(r'[A-Z]', password) and \
        re.findall(r'[0-9]', password) and \
        re.findall(r'[$#@]', password) and \
        len(password) >= 6 and \
        len(password) <= 16:
        return print("Valid password")
    else:
        return print("Invalid password")
    
check_password(password)    