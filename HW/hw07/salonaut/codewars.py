# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# II. Find The Distance Between Two Points
from math import sqrt

def distance(x1, y1, x2, y2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


# III. No yelling!
def filter_words(st):
    return " ".join((st.capitalize().split()))


# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

# V. Reversing Words in a String
def reverse(st):
    l = st.split()
    st = ' '.join(l[::-1])
    return st


# VI. Reverse List Order
def reverse_list(l):
    return l[::-1]


# VII. Multiples of 3 or 5
def solution(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])


# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if mpg * fuel_left >= distance_to_pump else False


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + " plays banjo" if name.lower().startswith('r') else name + " does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


# XI. Counting sheep
def count_sheeps(sheep: list):
  return sheep.count(True)


# XII. Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail[0]

