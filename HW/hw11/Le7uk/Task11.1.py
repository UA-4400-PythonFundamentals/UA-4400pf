class MinusError(Exception):
     pass

def check_odd_even(num):

    try:
        num = int(num)
        if num < 0:
            raise MinusError
        elif num % 2 == 0:
            return "Entered age is even"
        elif num % 2 != 0:
            return "Entered age is odd"
        
    except ValueError:
        return ("You entered not a number.")
    except MinusError:
        return ("Your age can't be negative")

print(check_odd_even(input("Enter your age: ")))