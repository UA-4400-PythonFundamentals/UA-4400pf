# I. Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#II. Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    return round(((x2-x1)**2 + (y2-y1)**2)**(1/2),2)

#III. No yelling!

def filter_words(st):
    
    st =' '.join(st.split())
    st = st.capitalize()
    return st

#IV. Convert a Number to a String

def number_to_string(num):
    return f"{num}" 

#V. Reversing Words in a String

def reverse(st):
    
    return ' '.join(st.split()[::-1])

#VI. Reverse List Order

def reverse_list(l):
    return l[::-1]

#VII. Multiples of 3 or 5

def solution(number):
    if number < 0 :
        return 0
    else:
        sum = 0
        for i in range(number):
            if i % 3 == 0:
                sum +=i
                continue
            elif i % 5 == 0:
                sum +=i
        return sum
  
#VIII. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= mpg * fuel_left else False

#IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == 'r' :
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"
    
#X. Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#XI. Counting sheep

def count_sheeps(sheep):
    count = 0
    for sh in sheep:
        if sh:
            count += 1
    return count

#XII. Is this my tail?

def correct_tail(body, tail):
     return body[-1:] == tail

