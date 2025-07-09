def greet(name):
    clean_name = name.strip().lower()
    if clean_name == "johnny":
        return "Hello, my honey!"
    return "Hello, " + name.strip().title()

user_name=input("Enter your name")
print(greet(user_name)) 
def distance(x1,x2,y1,y2):
    l = ((x2-x1)**2+(y2-y1)**2)**0.5
    return round(l,2)

(x1, y1), (x2, y2) = (1, 2), (4, 6)
print(distance(x1,x2,y1,y2))

text = "WOW this is REALLY          amazing"

def wow(text):
    text = "WOW this is REALLY          amazing"
    words = text.split()
    first = words[0].capitalize()
    rest = [word.lower() for word in words[1:]]
    all_words = [first
] + rest
    return " ".join(all_words)

print(wow(text))


n= input("Enter your number")
def number_on_string(number):
    return str(number)

print(number_on_string(n))
w = input("Enter your original sentense to reversed")
def reverse_word(w:str):
    words = w.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)
print(reverse_word(w))    


def reverse_list(input_list: list) -> list:
    return input_list[::-1]
my_constant_list = [10, 20, 30, 40, 50]
print(f"original list: {my_constant_list}")
reversed_constant_list = reverse_list(my_constant_list)
print(f"reversed original list: {reversed_constant_list}")

number_string = input("Enter your Number for task 7") 
number1 = int(number_string)
def solution_number(number1):
    if number1 < 0:
        return 0
    total_sum = 0
    for i in range(number1): # Iterate through numbers from 0 up to (but not including) 'number'
        if i % 3 == 0 or i % 5 == 0: # Check if the number is a multiple of 3 or 5
            total_sum += i
            
    return total_sum
print(solution_number(number1)) 


def Fuel_distance(volume_tank):
    
    fuel_cons = input("Enter Fuel Consumption your car")
    fuel_consumption = int(fuel_cons)
    distance=volume_tank*fuel_consumption
    if distance >= 50:
        print("You can drive to gas station")
    else:
         print("you'll have to walk to get petrol.")
    print(f"This vehicle can travel {distance} miles ")        

    return distance
      

Fuel_distance(2)         
    
def banjo(name: str) -> str:
    if name.lower().startswith('r'):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
user_name = input("Enter your name: ")
result_message = banjo(user_name)
print(result_message)


def bool_to_word(boolean_value: bool) -> str:
    if boolean_value:  
        return "Yes"
    else:              
        return "No"

print(f"True  -> {bool_to_word(True)}")
print(f"False -> {bool_to_word(False)}")
print(f"bool(1) -> {bool_to_word(bool(1))}") 
print(f"bool(0) -> {bool_to_word(bool(0))}") 
print(f"bool('hello') -> {bool_to_word(bool('hello'))}") 
print(f"bool('') -> {bool_to_word(bool(''))}") 

def count_sheeps(sheep_list: list) -> int:

    count = 0
    for sheep in sheep_list:
        if sheep is True:
            count += 1
    return count

sheep_list = [
    True,  True,  True,  False,
    True,  True,  True,  True,
    True,  False, True,  False,
    True,  False, False, True,
    True,  True,  True,  True,
    False, False, True,  True
]

present_sheep_count = count_sheeps(sheep_list)
print(f"The number of present sheep in your list is: {present_sheep_count}")

def correct_tail(body: str, tail: str) -> bool:

    last_letter_of_body = body[-1]

    if last_letter_of_body == tail:
        return True
    else:
        return False

print(f"Body: 'Fox', Tail: 'x' -> {correct_tail('Fox', 'x')}")     
print(f"Body: 'Tiger', Tail: 'r' -> {correct_tail('Tiger', 'r')}") 
print(f"Body: 'Bear', Tail: 'r' -> {correct_tail('Bear', 'r')}")   
print(f"Body: 'Dog', Tail: 'g' -> {correct_tail('Dog', 'g')}")     
print(f"Body: 'Cat', Tail: 't' -> {correct_tail('Cat', 't')}")    

print(f"\n--- Incorrect Tails ---")
print(f"Body: 'Dog', Tail: 'f' -> {correct_tail('Dog', 'f')}")    
print(f"Body: 'Lion', Tail: 'n' -> {correct_tail('Lion', 'z')}")   
print(f"Body: 'Elephant', Tail: 'a' -> {correct_tail('Elephant', 't')}") 