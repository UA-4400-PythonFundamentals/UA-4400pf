from Check import is_valid_password

def main():
    password = input("Enter your password: ")
    if is_valid_password(password):
        print("Password is valid ✅")
    else:
        print("Password is invalid ❌")

if __name__ == "__main__":
    main()
