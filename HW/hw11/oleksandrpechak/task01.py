def ask_age (age):
   
    if age < 0:
        raise ValueError("This is not a positive number. Try again!")
    elif age % 2 == 0:
        print("even")
    else:
        print("Odd")
        
try:  
    ask_age(int(input()))      
except ValueError as e:
    print(e) 