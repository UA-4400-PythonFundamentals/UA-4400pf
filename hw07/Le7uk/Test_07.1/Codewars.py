# #Jenny's secret message

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)
    
# #  Find The Distance Between Two Points

# def distance(x1, y1, x2, y2):
#     result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     return round(result, 2)

# #  No yelling!
# def filter_words(st):
#     words = st.split()
#     words = [word.lower() for word in words]
#     cleaned = ' '.join(words)
#     result = cleaned[0].upper() + cleaned[1:] if cleaned else ''
#     return result

# #  Convert a Number to a String
# def number_to_string(num):
#     return str(num)

#Reversing Words in a String

# def reverse(st):
#     return " ".join(reversed(st.split()))
    
# print(reverse("Hello World"))  

# Reverse List Order

# def reverse_list(l):
#     return list(reversed(l))
# print(reverse_list([1, 2, 3, 4, 5]))

# #Multiples of 3 or 5    
# def solution(number):
#     sum = 0
#     if number < 0:
#         return 0
#     else:
#         for i in range(number):
#             if i % 3 == 0 or i % 5 == 0:
#                 sum += i
#         return sum

# Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if fuel_left*mpg >= distance_to_pump:
#         return True
#     else:
#         return False
   
#Are You Playing Banjo?

# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'

#Convert boolean values to strings 'Yes' or 'No

# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     else:
#         return "No"

#Counting sheep...

# def count_sheeps(sheep):
#     result = 0
#     for i in sheep:
#             if i == True:
#                 result += 1
#             else:
#                 continue
#     return result

#Is this my tail?

# def correct_tail(body, tail):
#     if body[-1] == tail:
#          return True
#     else:
#          return False