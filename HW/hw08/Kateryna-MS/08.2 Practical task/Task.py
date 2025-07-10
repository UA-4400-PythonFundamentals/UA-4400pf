import re

password = input("Enter your password: ")
if len(password) < 16 and len(password) > 6:
    pattern1 = re.findall(r"[a-z]+", password)
    pattern2 = re.findall(r"[A-Z]+", password)
    pattern3 = re.findall(r"[$#@]+", password)
    pattern4 = re.findall(r"\d+", password)
    if pattern1 and pattern2 and pattern3 and pattern4:
        print("Your password is valid")
    else:
        print("Please try again")
else:
    print("Please try again")
