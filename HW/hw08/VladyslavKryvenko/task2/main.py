import models.login as login

while True:
    password = input("Enter your password: ")
    if login.validation_password(password):
        print("Your password is valid.")
        break
    else: 
        False  
        print("Your password is invalid. Please try again.")