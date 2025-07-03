def whats_greater(x,y):
    """
    Returns greater/equel number X or Y
    """
    if x < y:
        print(f"Number {y} is greater than {x}")  
    elif y < x:
        print(f"Number {x} is greater than {y}")
    else: 
        print(f"Number {y} equels {x}")
print("Provide two numbers to compare:")
x = int(input())
y = int(input())
whats_greater(x,y)