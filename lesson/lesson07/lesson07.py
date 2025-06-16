# print()
# sum()
# help(print)
# print(print.__doc__)
# def print_hello():
#     """
#     Prints 'Hello, World!' to the console.
#     """
#     print("Hello, World! This is a simple greeting function.")
#     print("This is a simple function that prints a greeting message.")
#     print("You can call this function to see the message printed.")

# print("Calling the print_hello function:")
# print_hello()
# print_hello()
# help(print_hello)
# print(print_hello.__doc__)
# print(print_hello)
# print(print_hello)
# print("call:", print_hello())

# def print_hello():
#     """
#     Prints 'Hello, World!' to the console.
#     """
#     print("Hello, World! This is a simple greeting function.")
#     print("This is a simple function that prints a greeting message.")
#     print("You can call this function to see the message printed.")
#     return "Hello, World!"
# print("call:", print_hello())

# def greet(name):
#     return f"Hello, {name}!"    

# print(greet("Alice"))
# print(greet("Bob"))
# text = greet("Charlie")
# print(text)


# def greet(name):
#     if not isinstance(name, str):
#        print("\tError: The name must be a string.")
#     elif len(name) >5:
#         return "The name is too long."
#     elif len(name) < 3:
#         return "The name is too short."
#     else:
#         return f"Hello, {name}!"
#         print("This line will not be executed due to the return statement above.")
#     return 50
#     print("This line will not be executed due to the return statement above.")
# print(greet("Alice"))
# print(greet("Bob"))
# print(greet("Charlie"))
# print(greet("A"))
# print(greet("Alexander"))
# print(greet(123))

# def greet(name, age, city):
#     """
#     Greets a person with their name, age, and city.
    
#     Parameters:
#     name (str): The name of the person.
#     age (int): The age of the person.
#     city (str): The city where the person lives.
    
#     Returns:
#     str: A greeting message.
#     """
#     return f"Hello, {name}! You are {age} years old and live in {city}."

# text = greet("Alice", 30, "New York")
# print(text)
# text = greet(1, 25, 25)
# print(text)
# # greet() #  TypeError: greet() missing 3 required positional arguments: 'name', 'age', and 'city'  
# # greet("Alice") #TypeError: greet() missing 2 required positional arguments: 'age' and 'city'
# # greet("Bob", 25)#TypeError: greet() missing 1 required positional argument: 'city'
# greet("Charlie", 35, "Los Angeles", "extra_arg") # TypeError: greet() takes 3 positional arguments but 4 were given
# greet("David", 40, "Chicago", "extra_arg1", "extra_arg2") # TypeError: greet() takes 3 positional arguments but 5 were given

# def greet(name, age=18, city="Lviv"):
#     """
#     Greets a person with their name, age, and city.
    
#     Parameters:
#     name (str): The name of the person.
#     age (int): The age of the person.
#     city (str): The city where the person lives.
    
#     Returns:
#     str: A greeting message.
#     """
#     return f"Hello, {name}! You are {age} years old and live in {city}."
# # greet() # ypeError: greet() missing 1 required positional argument: 'name'
# print(greet("Alice"))
# print(greet("Bob", 25))
# print(greet("Alice", 30, "New York"))
# # greet("Charlie", 35, "Los Angeles", "extra_arg") #TypeError: greet() takes from 1 to 3 positional arguments but 4 were given
# # greet("David", 40, "Chicago", "extra_arg1", "extra_arg2") #TypeError: greet() takes from 1 to 3 positional arguments but 5 were given
# def f(a, b=1, n):SyntaxError: parameter without a default follows parameter with a default
#     pass
# def f(a=1, b=2, c=3):
#     d = a+b+c
#     print(d)

# print(f(4,6,8))
# # print(a,b,c,d)#NameError: name 'a' is not defined

# def add(l=[]):
#     l.append(1)
#     print(l)
# add()
# add([1,2,3])
# add([1,2])
# add()
# add()
# add()
# add()


# def inc(l=[], i=1):
#     l.append(1)
#     i += 1
#     print(l, i)

# inc()
# inc()
# inc()
# ll = [1,2,3]
# ii = 10
# inc(ll, ii)
# print(f"{ll=} {ii=}")



# def greet(name, age=18, city="Lviv"):
#     return f"Hello, {name}! You are {age} years old and live in {city}."
# print(greet("Liubomyr", 39, "Lviv"))
# print(greet(39, "Liubomyr", "Lviv"))
# print(greet("Lviv", "Liubomyr", 39))
# print(greet(city="Lviv", name="Liubomyr", age=39))
# # print(greet(city="Lviv", name="Liubomyr", 39)) #SyntaxError: positional argument follows keyword argument
# # print(greet("Lviv", name="Liubomyr", age=39)) #TypeError: greet() got multiple values for argument 'name'
# print(greet("Liubomyr", age=39, city="Lviv")) 

# def my_print(*args, sep=", "):
#     print(f"{args=} {sep=}")
#     args = list(map(str, args))
#     result = sep.join(args)
#     print(result)
#     return result
# my_print(1,2,3,4,5,6)
# my_print(1,2,3, sep="=>")

# def func(a, b, *args, k=1, j=2, **kwargs):
#     print(f"{a=} {b=} {args=} {k=} {j=} {kwargs=}")

# func(1,2,3,4,5,6, k=100, m=200, test="text")
# params = [1,2,3,4,5,6,100,"text"]
# func(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7])
# func(*params)

# d = {
#     "a": 100,
#     "b": 200,
#     "j": 300,
#     "Uni": -100
# }
# func(**d)
# func(a=d["a"], b=d["b"], j=d["j"], Uni=d["Uni"])
# global_dir_start = set(dir())
# print("global_dir:", global_dir_start)
# def f(x=1, y = 10):
#     a = 1
#     print("f_dir: ", dir())
# f()
# print("global_dir_deff:", set(dir()) - global_dir_start)


# class M:
#     def __init__(self, name=None):
#         self.name = name
#         print(f"\t create value:{self.name}")
#     def __del__(self):
#         print(f"\tdel -> value:{self.name}")
# print("start")
# m = M()
# def f(n):
#     temp = M(n)
#     if n >0:
#         return temp
    
# print("in progress 1")
# f(-10)
# print("in progress 2")
# t = f(10)
# print("in progress 3")
# f(-5)
# print("in progress 4")
# print("test")
# print("end")


glo = "global"

# def f():
#     print(glo)
#     g = glo*2
#     print(g)
# f()
# def f():
#     glo = 100
#     print("local: ", glo)
#     g = glo*2
#     print("local: ", g)
# f()
# print("global: ", glo)
# def f():
#     print("local: ", glo)
#     glo = 100
#     print("local: ", glo)
#     g = glo*2
#     print("local: ", g)
# f()
# print("global: ", glo)


# def f():
#     global glo
#     print("local: ", glo)
#     glo = 100
#     print("local: ", glo)
#     g = glo*2
#     print("local: ", g)
# f()
# print("global: ", glo)

# g = 5
# def f(name):
#     # nonlocal g
#     name = name.capitalize() + "01"
#     def inner(text):
#         nonlocal name
#         name = name[:-1] + str(int(name[-1:])+1)
#         print(f"Hi {name}, text:{text}")
#     return inner

# my_f = f("Liubomyr")
# my_f("1,2,3")
# my_f("foo ")
# my_f("boo ")
# import sys
# sys.setrecursionlimit(3000)

# def rec(in_param):
#     print(in_param)
#     rec(in_param+1)
# rec(1)

# a = 1
# b = 1
# N = int(input("n:"))
# if N <= 3:
#     print(1)
# else:
#     for i in range(N-2):
#         a, b = b, a+b
#         print(b)


# def fibo(n):
#     if n<3:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(N))


def s(a, b):
    return a+b
print(s(1,2))
print(s(22,2))
s = lambda a, b: a+b
print(s(1,2))
print(s(22,2))

def conver(element):
    if type(element) in (float, int):
        return int(element)
    if type(element) is str and element.isdigit():
        return int(element)
    else:
        return len(element)
    
l = [1,2,3,"456","4a6", "text", {1,2}, [1,2,3,5,6]]
l.sort(key=conver)
print(l)
l.sort(key=lambda e: -int(e) if type(e) in (float, int) else -int(e) if type(e) is str and e.isdigit() else -len(e))
print(l)

