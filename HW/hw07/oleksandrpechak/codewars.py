# task_07_03
# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny,
#    and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
# Can you help her?
# 1.
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

# 2
# Given two ordered pairs calculate the distance between them. Round to two decimal places. This should be easy to do in 0(1) timing.
# def distance(x1, y1, x2, y2):
#     return round(((x2-x1)**2+(y2-y1)**2)**(1/2), 2)

# 3
# def filter_words(st):
#     return " ".join(str(st).capitalize().split())

# print(filter_words("WOW this is REALLY          amazing"))


# 4
# def number_to_string(num):
#     return str(num)
# print(number_to_string(2))

# 5

# def reverse(st):
#     return ' '.join(st.split()[::-1])
# print(reverse("Ok then."))

# 6
# def reverse_list(l):
#     l.reverse()
#     return l
#     'return a list with the reverse order of l'
# a = [1,2,3,4]
# print(reverse_list(a))

# 7
def solution(number):
    n3 = number // 3
    # n5 = number // 5

    if n3 > 0:
        return sum()
    # if n5 > 0:
    #     return n5*5+(n5-1)*5
    
print(solution(7))



# 8

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if mpg*fuel_left >= distance_to_pump:
#         return True
#     else:
#         return False
#     #Happy Coding! ;)
# print(zero_fuel(31, 16, 2))

# 9

# def are_you_playing_banjo(name):
#     if str(name[0]).lower() == 'r':
#         return name + " plays banjo" 
#     else:
#         return name + " does not play banjo"
#     # Implement me!
# print(are_you_playing_banjo("rey"))

# 10
# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"
# print(bool_to_word(True))

# 11
# def count_sheeps(sheep):
#     return str(sheep).count("True")
#   # May the force be with you

# print(count_sheeps([True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]))

# 12
# def correct_tail(body, tail):
#     sub = body[-1::]
#     if sub == tail[0]:
#         return True
#     else:
#         return False
    
# print(correct_tail("Fox", "x"))