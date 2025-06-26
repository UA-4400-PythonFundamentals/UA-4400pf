def validation(password: str) -> bool:
    length = False
    fullness = False


    if 6 <= len(password) <= 16:
        length = True
    else:
        if len(password) < 6:
            print('Password length should be bigger than 6')
            return False
        elif len(password) > 16:
            print('Password length should be smaller than 16')
            return False

    num = False
    upper_char = False
    lower_char = False
    special_symbol = False
    spec = ['#', '$', '@']

    for i in password:
        if i.isdigit():
            num = True
        if i.isupper():
            upper_char = True
        if i.islower():
            lower_char = True
        if i in spec:
            special_symbol = True


    if num and upper_char and lower_char and special_symbol:
        fullness = True
    elif num is False:
        print('Password must have at least 1 number between')
        return False
    elif upper_char is False:
        print('Password must have at least 1 uppercase letter')
        return False
    elif lower_char is False:
        print('Password must have at least 1 lowercase letter')
        return False
    elif special_symbol is False:
        print(f'Password must have at least 1 character from {['#', '$', '@']}')
        return False



    return length and fullness


def password_requirements() -> None:
    print('''        Password Validation Rules:
    At least 1 lowercase letter between [a-z]
    At least 1 uppercase letter between [A-Z]
    At least 1 number between [0-9]
    At least 1 character from [$#@]
    Minimum length: 6 characters
    Maximum length: 16 characters
    ''')

