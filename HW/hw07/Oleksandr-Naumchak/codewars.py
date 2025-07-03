#1.Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
    
#2.Simple: Find The Distance Between Two Points
import math

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(dist, 2)

#3.No yelling!
def filter_words(sentence):
    words = sentence.split()
    updated = ' '.join(words).lower()
    return updated.capitalize()

#4.Convert a Number to a String!
def number_to_string(num):
    return "{}".format(num)

#5.Reversing Words in a String
def reverse_words(text):
    words = text.strip().split()       
    reversed_words = words[::-1]       
    return ' '.join(reversed_words) 

#6.Reverse List Order
def reverse_list(lst):
    return lst[::-1]   

#7.Multiples of 3 or 5
def sum_of_multiples(number):
    return sum(i for i in range(number) if i % 3 == 0 or i % 5 == 0)

#8.Will you make it?
def can_reach_pump(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump

#9.Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
#10.Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(value):
    return "Yes" if value else "No"

#11.Counting sheep...   
def count_sheep(sheep):
    return sum(1 for s in sheep if s is True)

#12.Is this my tail? 
def correct_tail(body, tail):
    return body[-1] == tail
