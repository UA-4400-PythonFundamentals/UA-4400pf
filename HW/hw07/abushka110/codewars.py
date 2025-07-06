# 07.3 Practical Tasks / [GitHub Outside for Topic 7]

# I. Jenny's secret message
def greet(name):
    
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

# II. Find The Distance Between Two Points
from math import sqrt

def distance(x1, y1, x2, y2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

# III. No yelling!
def filter_words(st):
    words = st.split()
    cleaned = ' '.join(words).lower()
    return cleaned.capitalize()

# IV. Convert a Number to a String
def number_to_string(num):
    return f"{num}"

# V. Reversing Words in a String
def reverse(st):
    words = st.split(" ")
    st = ' '.join(words[::-1])
    return st

# VI. Reverse List Order
def reverse_list(l):
    return l[::-1]

# VII. Multiples of 3 or 5
def solution(number):
    if number <= 0:
        return 0

    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# XI. Counting sheep
def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s is True:
            count += 1
    return count

# XII. Is this my tail?
def correct_tail(body, tail):
    last_char = body[-1]
    return last_char == tail