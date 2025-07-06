from Check import rule

def is_valid_password(password):
    return all([
        rule.is_valid_length(password),
        rule.has_lowercase(password),
        rule.has_uppercase(password),
        rule.has_digit(password),
        rule.has_special_char(password)
    ])
