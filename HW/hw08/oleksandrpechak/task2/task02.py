

# Task2. Write a Python program to check the validity of a password (input from users). 
# Validation : At least 1 letter between [a-z] and 1 letter between [A-Z]. 
# At least 1 number between (0-9J. 
# At least 1 character from [$#@]. 
# Minimum length 6 characters. 
# Maximum length 16 characters.

pas = input("Create a password: ")
import re
char = re.findall("[a-z]", pas)
Char = re.findall("[A-Z]", pas)
num = re.findall("\d", pas)
specific = re.findall("[@,#,$]", pas)

result = []
if True:
    if True:
        if len(pas) >= 6:
            result.append(True)
        if len(pas) <= 16:
            result.append(True)
        if len(specific) > 0 :
            result.append(True)
        for c in char:
            if len(c) >0:
                result.append(True)
                break
        else:
            result.append(False)
        if len(Char) > 0 :
            result.append(True)
        else:
            result.append(False)
        if len(num) > 0:
            result.append(True)
        else:
            result.append(False)
if sum(result) > 5 :
    print("The password was created")
else:
    print("Try again")
