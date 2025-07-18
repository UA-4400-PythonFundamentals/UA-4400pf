# print("test")
# print("test2"
# print("test3")

# value = input("Enter a value: ")
# try:
#     value = int(value)
#     print(f"Value is {value} and its type is {type(value)}")
# except:
#     print(f"Invalid input, please enter a number. valeue:{value} is type{type(value)}")

# print("End of program")


# try:
#     a = int(input("Enter your number: ")) # throws ValueError for non-integer input
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except(ZeroDivisionError, NameError, ValueError):
#     print("Error Occurred and Handled")

# print("End of program")

# while True:

#     try:
#         a = input("Enter your number: ") 
#         if a == "exit":
#             print("Exiting the program.")
#             break
#         a = int(a) # throws ValueError for non-integer input
 
#         if a < 4:
#             b = a/(a-3) # throws ZeroDivisionError for a = 3
#         if a >= 4:
#             print("Value of b = ", b) # throws NameError
#     # note that braces () are necessary here for multiple exceptions
#     except ZeroDivisionError:
#         print("ZeroDivisionError Occurred and Handled")
#     except NameError:
#         print("NameError Occurred and Handled")
#     except ValueError:
#         print("ValueError Occurred and Handled")
#     except Exception:
#         print(f"An unexpected error occurred")

# print("End of program")


# while True:

#     try:
#         a = input("Enter your number: ") 
#         if a == "exit":
#             print("Exiting the program.")
#             break
#         a = int(a) 
 
#         a  = 3/a
#     except ZeroDivisionError:
#         print("ZeroDivisionError Occurred and Handled")
#     except ArithmeticError as error:
#         print("ArithmeticError Occurred and Handled", type(error),error)
#     except Exception:
#         print(f"An unexpected error occurred")
# print("End of program")


# try:
#     a = int(input("Enter your number: ")) # throws ValueError for non-integer input
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# except(ZeroDivisionError, NameError, ValueError) as error:
#     print(f"Error Occurred and Handled type: {type(error)}, message: {error}")

# value = input("Enter a value: ")
# try:
#     value = int(value)
# except:
#     print(f"Invalid input, please enter a number. valeue:{value} is type{type(value)}")
# else:
#     print(f"Value is {value} and its type is {type(value)}")
# print("End of program")



# value = input("Enter a value: ")
# try:
#     value = int(value)
# except:
#     print(f"Invalid input, please enter a number. valeue:{value} is type{type(value)}")
# else:
#     print(f"Value is {value} and its type is {type(value)}")
# finally:
#     print("This block always executes, regardless of exceptions.")
# print("End of program")

# def read():
#     value = input("Enter a value: ")
#     try:
#         value = int(value)
#         return value
#     except:
#         print(f"Invalid input, please enter a number. valeue:{value} is type{type(value)}")
#     finally:
#         print("This block always executes, regardless of exceptions.")
#         return "ERROR"

# a = read()
# print(f"Value is {a} and its type is {type(a)}")


# print("End of program")



# def read():
#     value = input("Enter a value: ")
#     if value.isdigit():
#         value = int(value)
#         return value
#     else:
#         # raise 10 #TypeError: exceptions must derive from BaseException
#         raise ZeroDivisionError(f"Invalid input, please enter a number. value:{value} is type{type(value)}")
    
# read()

class CustomError(Exception):
    pass



def read():
    value = input("Enter a value: ")
    if value.isdigit():
        value = int(value)
        return value
    else:
        # raise 10 #TypeError: exceptions must derive from BaseException
        raise CustomError(f"Invalid input, please enter a number. value:{value} is type{type(value)}")

try:    
    read()
except CustomError as error:
    print(f"CustomError Occurred: {type(error)} {error}")
