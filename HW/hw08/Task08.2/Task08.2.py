import string
def check_validity(password):
   
   has_letter = any(i in string.ascii_letters for i in password)
   has_upper = any(i.isupper() for i in password)
   has_digit = any(i.isdigit() for i in password)
   has_special = any(i in "@#$" for i in password)
   if (not has_letter or not has_upper or not has_digit or not has_special) or len(password) < 6 or len(password) > 16:
        return "Invalid password"
   else:
       return f"Valid password! Your password is : {password}"
print(check_validity(input("Enter your password:")))
   
        
          
        