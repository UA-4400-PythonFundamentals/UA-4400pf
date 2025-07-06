#Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#Simple: Find The Distance Between Two Points
from math import sqrt, pow
def distance(x1, y1, x2, y2):
    return round(sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)), 2)

# #No yelling!
def filter_words(st):
    st = " ".join(st.split())
    print(st)
    result = ""
    print(result)
    for item in st:
        if result == "":
            result = item
        else:
            result += item.lower()
    return result

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Reversing Words in a String
def reverse(st):
    words = st.split(" ")
    result = ""
    for item in reversed(words):
        result += item + " "
    return result.rstrip()

#Reverse List Order
def reverse_list(l):
    return list(reversed(l))

#Multiples of 3 or 5
def solution(number):
    i = 1
    list = []
    result = 0
    while i < int(number):
        if i % 3 == 0 or i % 5 == 0:
            list.append(i)
        i += 1
    for item in list:
        result += item
    return result

#Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    max_distance = mpg * fuel_left
    return max_distance >= distance_to_pump

#Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#Counting sheep...
def count_sheeps(sheep):
    i = 0
    for item in sheep:
        if item:
            i += 1
    return i

#Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail