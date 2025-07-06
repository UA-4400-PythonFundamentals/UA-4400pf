
#list

# l = list()
# print(type(l), l)
# l = list("list")
# print(type(l), l)
# l = list((1, 2, 3, [4, 5], "hello"))
# print(type(l), l)
# # l = list(10) #TypeError: 'int' object is not iterable
# l = []
# print(type(l), l)
# l = [1, 2, 3, [4, 5], "hello"]
# print(type(l), l)


# print(l[0])  # 1
# print(l[1])  # 2
# print(l[2])  # 3
# print(l[3])  # [4, 5]
# print(l[3][1])  # 5
# print(l[4]) # hello
# print(l[4][1]) # e
# print(l[4][1:-1]) # e
# print(l[:2]) # e
# print(l[::3]) # e
# # l[start:end:step]
# l[0] = 10
# print(l)  # [10, 2, 3, [4, 5], 'hello']
# print(l[1:-2])  # [10, 2]
# l2 = l[1:-2] + l
# print(l2)  # [2, 3, [4, 5], 'hello', 10, 2, 3, [4, 5], 'hello']
# print(l2*3)  # [2, 3, [4, 5], 'hello', 10, 2, 3, [4, 5], 'hello']
# l = ["hello", [4, 5]]
# l1 = [1,2,3, l]
# l2 = [4,5,6]
# l3 = l1 + l2
# l3.append(l1)
# l3.append(l2)
# print(l3)  # [1, 2, 3, 4, 5, 6, [1, 2, 3], [4, 5, 6]]
# l4 = l3 * 2
# print(l4)  # [1, 2, 3, 4, 5, 6, [1, 2, 3], [4, 5, 6], 1, 2, 3, 4, 5, 6, [1, 2, 3], [4, 5, 6]]
# l.append("toshi")
# l1.append("freedom")
# print(l3)
# print(l4) 

# print(9 in l3)  # False
# print(3 in l3)  # True
# print(['hello', [4, 5], 'toshi'] in l3)  # True
# print([4, 5] in l3)  # False

# l1 = [1,2,3,4,5]
# l2 = [1,2,3,4,5]
# l2 = [3,4,5,1,2]
# print(l1 == l2)  # True
# print(l1 is l2)  # False
# print(l1 == l3)  # False
# l22 = [7, 8, 9]
# l2 = [4, 5]
# l1 = ["hello", l2, l22]
# l = [1,2,3, l1]
# print(l)  # [1, 2, 3, ['hello', [4, 5]]]
# l.append(10)
# l.append([9, 8, 7])
# l.append("text")
# print(l)
# # l.extend(10)  # TypeError: 'int' object is not iterable
# l.extend([9, 8, 7])
# l.extend("text")
# print(l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']

# # print(l, l1, l2, l22)
# # l2 = []
# # l22.clear()
# # print(l, l1, l2, l22)  # [1, 2, 3, ['hello', []], 10, 9, 8, 7, 't', 'e', 'x', 't'] ['hello', []] [] []
# copy_l = l.copy()
# print(copy_l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
# from copy import deepcopy
# deep_copy_l = deepcopy(l)
# l[1] = 10
# l[3][0] = "bye"
# print(l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
# print(copy_l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
# print(deep_copy_l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
# print(l)
# print(l.count(10))  # 1
# print(l.count(['bye', [4, 5], [7, 8, 9]]))  # 1
# print(l.index(10))  # 1
# print(l.index(['bye', [4, 5], [7, 8, 9]]))  # 1
# # number = int(input("Enter a number to search in the list: "))
# # ll = l.copy()  # Create a copy of the list to avoid modifying the original
# # i = -1
# # while True:
# #     i = ll.index(number, i+1) if number in ll[i+1:] else -1
# #     print(f"Index of {number} in the list: {i}")
# #     if i == -1:
# #         break
# #     else:
# #         print(f"Found {number} at index {i}.")
       


# print(l)
# l.insert(1, "inserted")
# print(l)  # [1, 'inserted', 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
# l.remove("inserted")
# print(l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
# # l.remove("inserted")#ValueError: list.remove(x): x not in list
# l.reverse()
# print(l)  # ['t', 'e', 'x', 't', 7, 8, 9, 10, ['hello', [4, 5]], 3, 2, 1]
# a = l.pop()
# print(a) 
# print(l)  
# a = l.pop(1)
# print(a, l) 
# # l.sort()  # This will raise an error because the list contains mixed types
# l.sort(key=lambda x: str(x))  # Sorts by string representation
# for i in l:
#     print(i)     


# # tuple
# t = tuple()
# print(type(t), t)
# t = tuple("tuple")
# print(type(t), t)
# t = tuple((1, 2, 3, [4, 5], "hello"))
# print(type(t), t)
# # t = tuple(10)  # TypeError: 'int' object is not iterable
# t = ()
# print(type(t), t)
# t = (1, 2, 3, [4, 5], "hello")
# print(type(t), t)
# print(t[0])  # 1
# t = (1)
# print(type(t), t)  # <class 'int'> 1
# t = ("hello")  # <class 'str'> hello
# print(type(t), t)  # <class 'str'> hello
# t = (1,)
# print(type(t), t)  # <class 'tuple'> (1,)
# t = ("hello",)
# print(type(t), t)  # <class 'tuple'> ('hello',)

# t = (1, 2, 3, [4, 5], "hello")
# print(t[0])  # 1
# print(t[1])  # 2
# print(t[2])  # 3
# print(t[3])  # [4, 5]
# print(t[3][1])  # 5
# print(t[4])  # hello
# print(t[4][1])  # e
# print(t[-1])  # e
# print(t[1: -2])  # e
# t[1] = 10 # TypeError: 'tuple' object does not support item assignment
# print(t)  
# t[3].append(6)  # TypeError: 'tuple' object has no attribute 'append'
# print(t)  # (1, 2, 3, [4, 5, 6], 'hello')
# print(t.count(1))  # 1
# print(t.index(3))  # 0


# for i in range(5):
#     N = 10**i
#     print(f"Testing with N = {N}")
#     l = [i for i in range(N)]
#     t = tuple(i for i in range(N))
#     print(f"\tList: {l.__sizeof__()} bytes")
#     print(f"\tTuple: {t.__sizeof__()} bytes")

list
## set
# s = set()
# print(type(s), s)
# s = set("set")
# print(type(s), s)
# s = set("hello world")
# print(type(s), s)
# # s = set((1, 2, 3, [4, 5], "hello"))#TypeError: unhashable type: 'list'
# s = set((1, 2, 3, (4, 5), "hello"))
# print(type(s), s)
# # s = set((1, 2, 3, (4, 5, [1,2]), "hello"))# [1,2] -> TypeError: unhashable type: 'list'
# s = {} # This creates an empty dictionary, not a set
# print(type(s), s)  # <class 'dict'> {}
# s = {1}
# print(type(s), s)
# s = {1, 2, 3, (4, 5), "hello"}
# print(type(s), s)
# s = set()
# s.add(1) 
# s.add(2)
# s.add(3)
# s.add((4, 5))
# s.add("hello")
# print(type(s), s)  # <class 'set'> {1, 2, 3, (4, 5), 'hello'}
# s.update("hello") 
# s.update((4, 5))
# print(type(s), s)  # <class 'set'> {1, 2, 3, (4, 5), 'h', 'e', 'l', 'o'}
# s.remove(1)  # Removes 1 from the set
# # s.remove(50)  # Raises KeyError if 50 is not present
# s.discard(2)  # Removes 2 from the set, does nothing if 2 is not present
# s.discard(50)  # Does nothing if 50 is not present
# print(type(s), s)  # <class 'set'> {3, (4, 5), 'h', 'e', 'l', 'o'}
# element = s.pop()  # Removes and returns an arbitrary element from the set
# print(type(s), element, s)  # <class 'set'> {3, (4, 5), 'h', 'e', 'l', 'o'}

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print("Union of A and B:")
# print(A | B)  # Union: {1, 2, 3, 4, 5, 6, 7, 8}
# print(A.union(B))  
# print(B.union(A)) 
# c = A | B
# print(c)
# c = A.union(B)
# print(c)
# print("Intersection of A and B:")
# print(A & B)  # Intersection: {4, 5}
# print(A.intersection(B))
# print(B.intersection(A))  # Intersection: {4, 5}
# print("Difference of A and B:") 
# print(A - B)  # Difference: {1, 2, 3}
# print(B - A)  # Difference: {6, 7, 8}
# print(A.difference(B))  # Difference: {1, 2, 3}
# print(B.difference(A))  # Difference: {6, 7, 8}
# print("Symmetric Difference of A and B:")
# print(A ^ B)  # Symmetric Difference: {1, 2, 3, 6, 7, 8}
# print(A.symmetric_difference(B))  # Symmetric Difference: {1, 2, 3, 6, 7, 8}

# print(B.symmetric_difference(A))  # Symmetric Difference: {1, 2, 3, 6, 7, 8}

# print("Is A a subset of B?")
# c = {2,3,4}
# print(c.issubset(A))
# print(c.issubset(B))

# print("Is A a superset of B?")
# print(A.issuperset(c))  # True
# print(B.issuperset(c))  # False

# for i in A:
#     print(i)  # Prints each element in set A

# print("Is 3 in A?")
# print(3 in A)  # True
# print("Is 10 in A?")    
# print(10 in A)  # False
# print("Is 3 not in A?")
# print(3 not in A)  # False
# print("Is 10 not in A?")
# print(10 not in A)  # True
# del A  # Deletes the set A
# del B  # Deletes the set B
# print("Sets A and B deleted.")
# # print(A)  # Raises NameError: name 'A' is not defined
# # print(B)  # Raises NameError: name 'B' is not defined

# s = set("hello world")
# print(list(enumerate(s)))
# print(len(s))

# f = frozenset("hello world")
# print(type(f), f)  # <class 'frozenset'> frozenset({'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'})
# f.add("new")  # Raises AttributeError: 'frozenset' object has no attribute 'add'

# print(list.__dict__)

# dict
# d = dict()
# print(type(d), d)  # <class 'dict'> {}
# d = dict({"key1": 1, "key2": 2, "key3": 3}) 
# print(type(d), d)  # <class 'dict'> {'key1': 1, 'key2': 2, 'key3': 3}
# d = dict([
#     ("key1", 1),
#     ("key2", 2),
#     ("key3", 3)
#     ])
# print(type(d), d)  # <class 'dict'> {'key1': 1, 'key2': 2, 'key3': 3}
# d = dict(key1=1, key2=2, key3=3)
# print(type(d), d)  # <class 'dict'> {'key1': 1, 'key2': 2, 'key3': 3}
# d = {}  # This creates an empty dictionary
# print(type(d), d)  # <class 'dict'> {}
# d = {
#     "key1": 1,
#     "key2": 2,
#     "key3": 3,
#     2: "value2",
#     3: "value3"
# }
# print(type(d), d)
# print(d["key1"])  # 1
# print(d[2])  
# # print(d[555])  # KeyError: 555
# print(d.get("key1"))  # 1
# print(d.get(2))  # value2
# print(d.get("key555"))  # None
# print(d.get(555, "Not Found"))  # Not Found
# print(d.get(3, "Not Found"))  # Not Found
# print(d)
# d["key4"] = 4
# print(d)  # {'key1': 1, 'key2': 2, 'key3': 3, 2: 'value2', 3: 'value3', 'key4': 4}
# d["key1"] = 10
# print(d)  # {'key1': 10, 'key2': 2, 'key3': 3, 2: 'value2', 3: 'value3', 'key4': 4}
# d["key5"] = sum
# print(d)  # {'key1': 10, 'key2': 2, 'key3': 3, 2: 'value2', 3: 'value3', 'key4': 4, 'key5': <built-in function sum>}
# print(d["key5"]([1, 2, 3]))  # 6
# # d[["key6"]] = [1, 2, 3] # Raises TypeError: unhashable type: 'list' TypeError: unhashable type: 'list'
# print(d)
# x = d.pop("key1")  # Removes 'key1' and returns its value
# print(x, d)  # 10 {'key2': 2, 'key3': 3, 2: 'value2', 3: 'value3', 'key4': 4, 'key5': <built-in function sum>}
# # d.pop() #TypeError: pop expected at least 1 argument, got 0
# x = d.popitem()  # Removes and returns an arbitrary (key, value) pair
# print(x, d)  # (3, 'value3') {'key2': 2, 2: 'value2', 'key4': 4, 'key5': <built-in function sum>}
# x = d.popitem()  # Removes and returns an arbitrary (key, value) pair
# print(x, d)  # (2, 'value2') {'key2': 2, 'key4': 4, 'key5': <built-in function sum>}
# del d["key3"]  # Deletes the key 'key3'
# print(d)  # {'key2': 2, 'key4': 4, 'key5': <built-in function sum>}
# d2 = d.fromkeys(["key1", "key2"], 0)  # Creates a new dictionary with keys 'key1' and 'key2', both set to 0
# print(d2)  # {'key1': 0, 'key2': 0}

# print(d.keys()) # dict_keys(['key2', 'key4', 'key5'])
# print(tuple(d.keys())) # ('key2', 2, 3)
# print(d.values()) # dict_values([2, 4, <built-in function sum>])

# # d.add("key6", 6)  # Raises AttributeError: 'dict' object has no attribute 'add'
# d["key6"] = 6  # Correct way to add a new key-value pair
# print(d)  # {'key2': 2, 'key4': 4, 'key5': <built-in function sum>, 'key6': 6}

# d.update({"key7": 7, "key8": 8})  # Adds multiple key-value pairs
# print(d)  # {'key2': 2, 'key4': 4, 'key5': <built-in function sum>, 'key6': 6, 'key7': 7, 'key8': 8}

# print(d.items())  # dict_items([('key2', 2), ('key4', 4),
# for k in d:
#     print(f"Key: {k}, Value: {d[k]}")  # Prints each key-value pair in the dictionary
# print()
# for pair in d.items():
#     print(f"Item: {pair} -> Key: {pair[0]}, Value: {pair[1]}")  # Prints each (key, value) pair in the dictionary

# a, b = (2,3)
# print(f"Values before swap: a = {a}, b = {b}")

# for key, value in d.items():
#     print(f"Current item: {key} -> {value}")


# A = list(map(int, input("Enter a numbers: ").split()))
# B = list(map(int, input("Enter a numbers: ").split(",")))
# result = []
# for a in A:
#     for b in B:
#         if a == b:
#             print(f"\tmatch for {a} and {b} -> {a**b}")
#             result.append(a**b)
#         else:
#             print(f"\t\tNo match for {a} and {b}")

# print(f"Result: {result}")

# result2 = [a**b for a in A for b in B if a == b]
# print(f"Result2: {result2}")

# result3 = {a: a**b for a in A for b in B if a == b}
# print(f"Result3: {result3}")

result4 = [a+b+c for a in range(0, 3) for b in range(10, 30, 10) for c in range(100, 300, 100)]
print(f"Result4: {result4}")

result41 = []
for a in range(0, 3):
    for b in range(10, 30, 10):
        for c in range(100, 300, 100):
            result41.append(a + b + c)
   
print(f"Result4: {result4}")