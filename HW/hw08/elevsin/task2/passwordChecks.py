import re

while True:
    pswd = str(input("Create your password: "))
    if len(pswd) < 6:
        print("Your password should contain minimum 6 characters\n")

    elif len(pswd) > 16:
        print("Your password should contain maximum 16 characters\n")

    elif not re.match("(?=.*\d)", pswd):
        print("Your password should contain at least one number 0-9\n")

    elif not re.match("(?=.*[a-z])", pswd):
        print("Your password should contain at least one letter in lower case\n")

    elif not re.match("(?=.*[A-Z])", pswd):
        print("Your password should contain at least one letter in upper case\n")

    elif not re.match("(?=.*[#$@])", pswd):
        print("Your password should contain at least one spec symbol like #, $ or @\n")

    else:
        print("Password accepted")
        break