a1 = [1.0,2,3]
x = 1
a2 = [x,2,3]
a3 = [2,3,1]
a4 = a1
print(f"{a1 == a2 =}")  # Check if a1 and a2 are equal
print(f"{a1 is a2 =}")  # Check if a1 and a2 are the same object
print(f"{a1 == a3 =}")  # Check if a1 and a3 are equal
print(f"{a1 is a3 =}")  # Check if a1 and a3 are the same object
print(f"{a1 == a4 =}")  # Check if a1 and a4 are equal
print(f"{a1 is a4 =}")  # Check if a1 and a4 are the same object

# a = 1
# b = 2
# c = 3
# x = int(input("Enter a value for x: "))

# # print(x < a and x < 50)  # Check if x is less than a

# print(True and False or True)  # Evaluate logical expression
# print(True or False and True)  # Evaluate logical expression
# print(True or True and False)  # Evaluate logical expression
# print((True or True) and False)  # Evaluate logical expression

# print(x < a < 50)  # Check if x is less than a
# print(a <b and b < c)  # Check if a is less than b and b is less than c
# print(a < b < c)  # Check if a is less than b and b is less than c
# print(a < b < c < 100)  # Check if a is less than b, b is less than c, and c is less than 100
# print(int(True))
# print(int(False))
# print(10 + True)
# print(False - 1)
# print(a > 10 or a == 10) # Check if a is greater than 10 or equal to 10 >=

# print(10 or True)

# print(10 and True and "test")  # Evaluate logical expression
# print(10 and 0 and "test")  # Evaluate logical expression
# print(10 and 0 and False and "test")  # Evaluate logical expression
# print(10 and False and 0 and "test")  # Evaluate logical expression
# print(0 or False or [] or "test2" or 15)  # Evaluate logical expression
# print(0 or False or [] or 15 or "test2")  # Evaluate logical expression
# print(0 or False or [] or None)  # Evaluate logical expression

# is_false = [False, None, 0, 0.0, 0j, [], "", set(), {}, ()]

# # is
# a = [1,2,3]
# b= a
# print(f"{a is b =}")  # Check if a and b are the same object
# print(f"{id(a) == id(b) =}")  # Check if a and b have the same memory address


# l = [1, 2, 3, [4, 5, 6], "test"]

# print(f"{1 in l =}")  # Check if 1 is in l
# print(f"{2 in l =}")  # Check if 2 is in l
# print(f"{3 in l =}")  # Check if 3 is in l
# print(f"{4 in l =}")  # Check if 4 is in l
# print(f"{[4, 5, 6] in l =}")  # Check if [4, 5, 6] is in l
# print(f"{'test' in l =}")  # Check if 'test' is in l
# print(f"{'t' in l =}")  # Check if 'test2' is in l

# for i in l:
#     # if isinstance(i, list):
#     # if type(i) is list:
#     if type(i) in (list, str, tuple, set, dict):
#         print(i)


# line = input("Enter a line: ")

# # Check if the line is empty
# # if len(line) > 0:
# #     print(line, id(line), type(line), type(line) is str)  # Print line and its memory address
# #     print("The line is not empty.")

# # print("end of the program.")

# if line:
#     print(line, id(line), type(line), type(line) is str)  # Print line and its memory address
#     print("The line is not empty.")
# else:
#     print("The line is empty.")
# print("end of the program.")

# age = int(input("Enter your age: "))
# if age < 0:
#     print("Age cannot be negative.")
# else:
#     if age < 12:
#         print( "You are a kid.")
#     else:
#         if age < 18:
#             print("You are a teenager.")
#         else:
#             if age < 60:
#                 print("You are an adult.")
#             else:
#                 print("You are a senior citizen.")

# print("Thank you for using the age classification program.")

# if age < 0:
#     print("Age cannot be negative.")
# elif age < 12:
#     print("You are a kid.")
# elif age < 18:
#     print("You are a teenager.")
# elif age < 60:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")
# print("Thank you for using the age classification program.")



# weather = "raining"
# text = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# text = weather == "raining" ? "Open Your umbrella" : "Wear your cap"
# print(text)  # Print the result of the conditional expression




# weather = "raining"
# # new_text = ""
# if weather != "raining":
#     new_text = "Open Your umbrella"
# else:
#     new_text =  "Wear your cap"

# print(new_text)

# x = input("Enter a value for x: ")
# t= None
# if x.isdigit() or (x.startswith('-') and x[1:].isdigit()):
#     x = int(x)
# if x < 0:
#     print("x is negative.")
#     t = "negative"
# elif x == 0:   
#     print("x is zero.")
# elif x < 10:
#     print("x is a single-digit positive number.")

# print(f"x is {t} and its value is {x}.")


# text = 0
# while text < 10:
#     print(text)
#     text += 1
#     s = text * 2

# print(s)


# # http_status_codes = int(input("Enter an HTTP status code (100-599): "))
# match int(input("Enter an HTTP status code (100-599): ")):
#     case 100 | 101 | 102 as code:
#         print(f"Informational response {code}")
#     case 200 | 201 | 202 | 203 | 204 | 205 | 206:
#         print("Successful response")
#     case 300 | 301 | 302 | 303 | 304 | 305 | 307:
#         print("Redirection message")
#     case 400 | 401 | 402 | 403 | 404 | 405 as code:
#         print(f"Client error response {code}")  # Handle specific client error codes
#     case 500 | 501 | 502 | 503 | 504:
#         print("Server error response")
#     case _ as code:
#         print(f"Unknown status code {code}")  # Handle any other status codes

# "link https://www.w3schools.com/python/python_ref_string.asp" 1
# "save http://www.w3schools.com/python/python_ref_string.asp data1.txt" 2
# "save http://www.w3schools.com/python/python_ref_string.asp data1.txt data2.txt data3.txt" 3
# "save http://www.w3schools.com/python/python_ref_string.asp data11.txt data12.txt data13.txt data14.txt" 3



# while True:
#     row = input("values: ").split()
#     match row:
#         case "link", link:
#             print(f"Link: {link}")
#         case "save", link, file_name:
#             print(f"Saving data from {link} to {file_name}")
#         case "save", link, *file_names:
#             print(f"Saving data from {link} to files:")
#             for file_name in file_names:
#                 print(f"\t- {file_name}")
#         case _:
#             print("Unknown command")
#             if row[0] == "exit":
#                 break


# # match item:
# #     case ['evening', action]:
# #     print(f'You almost finished the day! Now {action}!’)
# # case [time, action]:
# # print(f'Good {time}! It is time to {action}!’)
# # case _:
# # print('The time is invalid.’)

# print("Hello, World!")  # Print a simple message

# print("")

# numbers = input("Enter a list of numbers separated by spaces: ").split()
# numbers = [int(num) for num in numbers]  # Convert input strings to integers
# print(f"Numbers: {numbers}")  # Print the list of numbers

# numbers.append([1,2,3,4,5])  # Append a list to the numbers list
# print(numbers)
# for index, i in enumerate(numbers):
#     match i:
#         case 0:
#             print(f"{i} is zero")  # Handle the case where the number is zero
#         case _ if type(i) is list:
#             print(f"{i} is a list")  # Handle the case where the number is a list
#             i.append(6)  # Append 6 to the list
#             print(f"Updated list: {i}")  # Print the updated list
#         case _ if i < 0:
#             print(f"{i} is negative")  # Handle the case where the number is negative
#             i = abs(i)  # Convert negative number to positive
#             numbers[index] = i  # Update the list with the converted positive number
#             print(f"Converted to positive: {i}")  # Print the converted positive number
#         case _ if i > 0:
#             print(f"{i} is positive")  # Handle the case where the number is positive
#         case _:
#             print(f"{i} is an unknown value")  # Handle any other cases (should not occur with current logic)
# print(numbers)