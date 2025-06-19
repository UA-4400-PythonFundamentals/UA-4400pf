# 1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# 2
def distance(x1, y1, x2, y2):
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return a.__round__(2)

# 3
def filter_words(str):
    return " ".join(str.split()).capitalize()
    
# 4
def number_to_string(num):
    return str(num) 

# 5
def reverse(st):
    return " ".join(st.split()[::-1])

# 6
def reverse_list(l):
    return l[::-1]

# 7
def solution(number):
    test = 0
    if number <= 3:
        return 0
    else:
        for i in range(3, number):
            if i % 3 == 0 or i % 5 == 0:
                test += i
    return test

# 8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return bool(distance_to_pump <= mpg * fuel_left)

# 9
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    
# 10
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# 11
def count_sheeps(sheep):
    return sheep.count(True)

# 12
def correct_tail(body, tail):
    return body[-1] == tail