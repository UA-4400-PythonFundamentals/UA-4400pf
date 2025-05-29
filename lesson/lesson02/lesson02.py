# a = 10
# print(a, id(a)) 
# b = 20
# print(b, id(b)) 
# b += 30
# print(b, id(b)) 
# c = a + b
# print(c, id(c)) 
# a = [1,2,3 ]
# print(a, id(a)) 
# a.append(4)
# print(a, id(a)) 

# value = 10
# print(value, id(value), type(value), type(value) is str)  # Print value and its memory address
# value = "10"
# print(value, id(value), type(value), type(value) is str)  # Print value and its memory address
# value = ["10", 1, 2, 3]
# print(value, id(value), type(value), type(value) is list)  # Print value and its memory address


# value = ["10", 1, 2, 3]
# print(isinstance(value, list))  # Check if value is an instance of list


# class A:pass
# class B(A):pass
# a = A()
# b = B()
# print(f"{type(a) }\t{type(a) is A}\t{type(a) is B=}\t{isinstance(a, A)=}\t{isinstance(a, B)=}")  # Check if a is an instance of A
# print(f"{type(b)=}\t{type(b) is A=}\t{type(b) is B=}\t{isinstance(b, A)=}\t{isinstance(b, B)=}")  # Check if a is an instance of A

# a = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# print(a)
# a = 1 + 2 + 3 \
# + 4 + 5 + 6 + 7 + 8 + 9 + 10
# print(a)
# a = (1 
#      + 2
#     + 3 
#     + 4 + 5 + 6 
#     + 7 + 8 + 9 + 10)
# print(a)

# a = ("line1"
#      "line2"
#      "line3"
#      "line4"
#      "line5"
#      "line6")
# print(a)
# a = ["line1"
#      "line2"
#      "line3"
#      "line4"
#      "line5"
#      "line6"]
# print(a)

# a = 1;b=2;c = 3;d = 4;e = 5;f = 6;g = 7;h = 8;i = 9;j = 10
# print(a, b, c, d, e, f, g, h, i, j)  # Print all variables in one line
# for i in range(1, 6):
#  print(i)  # Print numbers from 1 to 10 in one line with space separation
#  for j in range(1, 6):
#    print(f"\t{i} * {j} = ", end="")  # Print multiplication table for each number from 1 
#    print(f"{i * j}")  # Print multiplication table for each number from 1 to 10


# a, b, c = input(), 2, input()
# a, b,c = 1, 2 #ValueError: not enough values to unpack (expected 3, got 2)
# a, b,c = 1, 2, 3, 4 #ValueError: too many values to unpack (expected 3)

# # print(a, b, c)  # Print values of a, b, and c   
# a = b = c =1

# a = 10000000
# print(a)

# a = 10_000_000
# print(a)
# print(1.1)
# print(.1)
# print(1.)

# print(1.1e3)  # Scientific notation
# print(1.1e-3)  # Scientific notation with negative exponent

# a = 9
# b = 0o11  # Octal representation
# c = 0x9
# d = 0b1001
# print(a,b,c,d)  # Octal representation

# for i in range(1, 20):
#     print(f"{i}\t{bin(i)[2:]}\t{oct(i)[2:]}\t{hex(i)[2:]}")
# print()
# for i in range(1, 20):
#     print(f"{bin(i)[2:].zfill(4)}\t{oct(i)[2:].zfill(2)}\t{str(i).zfill(2)}\t{hex(i)[2:].zfill(2)}")


# print(set("test"), list("test"))

# print(int("10"))  # Convert string to integer
# print(int("10", 2))  # Convert binary string to integer
# print(int("10", 8))  # Convert binary string to integer
# # print(int("10sss", 8))  #ValueError: invalid literal for int() with base 8: '10sss'
# print(float("10.5"))  # Convert string to float
# print(float(15))  # Convert string to float

# # print(str(15))

# for i in range(300):
#     print(f"{i} - {chr(i)}")  # Print ASCII characters from 0 to 255

# for i in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;:',.<>?/`~":
#     print(f"{i} - {ord(i)}") 

# print("A" > "B")  # Compare strings lexicographically
# print("A" < "B")  # Compare strings lexicographically
# print("Aasfas" > "asdsaB")  # Compare strings for equality
# print("Aasfas" < "asdsaB")  # Compare strings for equality

# s = "Hello, World!"
# print(s[0])  # Access first character
# print(s[7])  # Access character at index 7
# print(s[-1])  # Access last character
# print(s[-2])  # Access second last character
# print(s[2:5])  # Access second last character
# print(s[:5])  # Access second last character
# print(s[3:])  # Access second last character
# print(s[:])  # Access second last character
# print(s[::2])  # Access second last character
# # s[0] = "h"  # Attempt to modify string (will raise TypeError)

# text = "Hello,\nWorld!"
# print(text)  # Print the original string

# text = "Hello,World!\rXX"
# print(text)  # Print the string with carriage return

# text = "Hello,World!\tXX"
# print(text)  # Print the string with tab character
# text = "Hello,Worl\"X\\X"
# print(text)  # Print the string with vertical tab character

# template = "%s is %d years old. Your sallary is %.3f $"
# print(template % ("John", 30, 1234.56789))
# print(template % ("Anna", 18.5, 1234.5)) 
# template = "%s is %d years old. Your sallary is %.3f $ %s"
# print(template % ("John", 30, 1234.56789, "John"))

# template = "{} is {} years old. Your sallary is {:.3f} $"
# print(template.format("John", 30, 1234.56789))
# template = "{name} is {age} years old. Your sallary is {sel:.3f} $ {name}"
# print(template.format(name="John", age=30, sel=1234.56789))


# a = 'John'
# b = 'Bill'
# c = 5
# default_order = "Hello "+ str(a) + ", "  + str(b) + " and " + str(c**c)
# print(default_order)  # Default order of variables
# default_order = f"Hello {a}, {b} and {c**c}"
# print(default_order)  # Default order of variables

# sentence = "i love PYTHON. i love PYTHON."

# # converts first character to uppercase and others to lowercase
# capitalized_string = sentence.capitalize()

# print(capitalized_string)

# # Output: I love python
# message = 'python is popular programming language is python is popular programming language'

# # number of occurrence of 'p'
# print('Number of occurrence of p:', message.count('p'))
# print('Number of occurrence of p:', message.count('is'))

# # Output: Number of occurrence of p: 4


# message = 'laNguage Language lanGUage languAGE language'
# print(message.count("language"))  # Convert to lowercase
# print(message.count("laNGuage"))  # Convert to lowercase
# print(message.lower().count("laNGuage".lower()))  # Convert to lowercase

import math

# print(math.sin(30))  # Calculate combinations of 5 items taken 2 at a time
# print(math.pow(3, 2))  # Calculate 3 raised to the power of 2
# print(math.pow(3, 2.2))  # Calculate 3 raised to the power of 2
# print(math.sqrt(9))  # Calculate 3 raised to the power of 2
# print(math.sqrt(-9))  #print(math.sqrt(-9))  # Calculate 3 raised to the power of 2

print(3**3)
print(3**2.5)
print(3**0.5)
print((-1)**0.5)