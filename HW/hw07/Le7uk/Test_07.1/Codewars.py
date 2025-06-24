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
def reverse_list(l):
    return list(reversed(l))
# Example usage:
print(reverse_list([1, 2, 3, 4, 5]))