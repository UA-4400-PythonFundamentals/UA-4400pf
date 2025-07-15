# # print([i**i for i in range(5)])
# # print({i**i for i in range(5)})
# # print({i:i**i for i in range(5)})
# # print((i**i for i in range(5)))


# # vec1 = [3, 10, 2]
# # vec2 = [-20, 5, 1]
# # print(zip(vec1, vec2))
# # print(list(zip(vec1, vec2)))


# # dot_mul = [u*v for u, v in zip(vec1, vec2)]
# # print(dot_mul)


# # vec1 = [3, 10, 2, 8]
# # vec2 = [-20, 5, 1]
# # vec3 = [99, -920, 95, 91]
# # print(zip(vec1, vec2, vec3))
# # print(list(zip(vec1, vec2, vec3)))




# # l = [1,2,"10", 50, "test"]

# # def f(a):
# #     if type(a) is not int:
# #         return 0
# #     return a
# # result = []

# # for i in l:
# #     result.append(f(i))

# # print(result)

# # print(list(map(f, l)))
# # print(list(filter(f, l)))


# l = [1,2,3,4,5]
# def add(a,b):
#     print(f"{a=} + {b=} => {a+b}")
#     return a+b

# from functools import reduce
# print(reduce(add, l))
# print(reduce(add, l, -100))


# s = "0123456789"
# for i in s:
#     print(i, end=" ")
# print()
# it = iter(s)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# class MyRange():
#     def __init__(self, start, stop=None, step=1):
#         if stop == None:
#             self.stop = start
#             self.start = 0    
#         else:
#             self.start = start
#             self.stop = stop
#         self.step = step
#         self.__current = None

#     def __str__(self):
#         return f"MyRange({self.start},{self.stop},{self.step})"
    
#     def __iter__(self):
#         self.__current = self.start
#         return self
#     def __next__(self):
#         if self.stop < self.__current:
#             raise StopIteration("MyRange")
#         value_to_return = self.__current
#         self.__current += self.step
#         return value_to_return
    
# r1 = MyRange(5)
# r2 = MyRange(-10, 10)
# r3 = MyRange(-10, 10, 3)
# print(r1, r2, r3)

# for i in r1:
#     print(i, end=" ")
# print()

# for i in r2:
#     print(i, end=" ")
# print()

# for i in r3:
#     print(i, end=" ")
# print()

# r3 = MyRange(-1, 2, 1)
# it = iter(r3)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# def my_gen():
#     print("run")
#     print("before yield 0")
#     yield 0
#     print("after yield 0")
#     print("before yield 1")
#     yield 1
#     print("after yield 1")
#     print("before yield 2")
#     yield 2
#     print("after yield 2")


# g1 = my_gen()
# print(g1)
# print(f"{next(g1)=}")
# print(f"{next(g1)=}")
# print(f"{next(g1)=}")
# # print(f"{next(g1)=}") StopIteration

# g1 = my_gen()
# for i in g1:
#     print(i)
    

# def my_range(n):
#     current = 0
#     while current < n:
#         current += 1
#         yield current
# for i in my_range(5):
#     print(i)

# for i in range(1, 5):
#     print(f"n={10**i}")
#     print("\t", my_range(10**i).__sizeof__())
#     print("\t", list(my_range(10**i)).__sizeof__())


# def star(func):
#     def wrap(*args, **kwarg):
#         print("*"*10)
#         result =  func(*args, **kwarg)
#         print("*"*10)
#         return result
#     return wrap

# def add(a, b):
#     return a + b
# # add = star(add)

# @star
# def div(a, b):
#     return a/b


# print("+"*10)
# print(add(1,2))
# print("+"*10)
# print("+"*10)
# print(add(5,7))
# print("+"*10)

# w_add = star(add)
# print(w_add(999, 9999))
# print(w_add(999, -9999))

# add = star(add)
# print(add(10, 20))

# print(div(15, 5))



# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner

# @star
# @percent
# def printer(msg):
#     print(msg)

# printer("Hello")


# @percent
# @star
# @percent
# def printer(msg):
#     print(msg)
    
# printer("Hello")

# import time
# import random

# def run_time(func):
#     def wrapper(*args, **keargs):
#         start_time = time.time()
#         result = func(*args, **keargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"run func: {func.__name__} args: {args} {keargs} executed {execution_time:.4f} seconds.")
#         return result
#     return wrapper

# # @run_time
# def run(n):
#     r = random.randint(0, n)
#     print(f"sleep: {r}")
#     time.sleep(r)


# for i in range(5):
#     run(i)

__inner_funcs = {} # (types): func

def param(*types):
    # print(inner_funcs)
    # print(types)
    def run(func):
        # print(func)
        __inner_funcs[types] = func
        def wraper(*args):
            # print(*args, **keargs)
            return __inner_funcs[tuple(map(type, args))](*args)
        return wraper
    return run


@param(int)
def add(a):
    print(a*5)

@param(int, int)
def add(a, b):
    print( a*b)

@param(str)
def add(a):
    print(a.upper())

add(3)
add(3,10)
add("aBa")
