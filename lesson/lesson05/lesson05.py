
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
l22 = [7, 8, 9]
l2 = [4, 5]
l1 = ["hello", l2, l22]
l = [1,2,3, l1]
print(l)  # [1, 2, 3, ['hello', [4, 5]]]
l.append(10)
l.append([9, 8, 7])
l.append("text")
print(l)
# l.extend(10)  # TypeError: 'int' object is not iterable
l.extend([9, 8, 7])
l.extend("text")
print(l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']

# print(l, l1, l2, l22)
# l2 = []
# l22.clear()
# print(l, l1, l2, l22)  # [1, 2, 3, ['hello', []], 10, 9, 8, 7, 't', 'e', 'x', 't'] ['hello', []] [] []
copy_l = l.copy()
print(copy_l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
from copy import deepcopy
deep_copy_l = deepcopy(l)
l[1] = 10
l[3][0] = "bye"
print(l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
print(copy_l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
print(deep_copy_l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
print(l)
print(l.count(10))  # 1
print(l.count(['bye', [4, 5], [7, 8, 9]]))  # 1
print(l.index(10))  # 1
print(l.index(['bye', [4, 5], [7, 8, 9]]))  # 1
# number = int(input("Enter a number to search in the list: "))
# ll = l.copy()  # Create a copy of the list to avoid modifying the original
# i = -1
# while True:
#     i = ll.index(number, i+1) if number in ll[i+1:] else -1
#     print(f"Index of {number} in the list: {i}")
#     if i == -1:
#         break
#     else:
#         print(f"Found {number} at index {i}.")
       


print(l)
l.insert(1, "inserted")
print(l)  # [1, 'inserted', 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
l.remove("inserted")
print(l)  # [1, 2, 3, ['hello', [4, 5]], 10, 9, 8, 7, 't', 'e', 'x', 't']
# l.remove("inserted")#ValueError: list.remove(x): x not in list
l.reverse()
print(l)  # ['t', 'e', 'x', 't', 7, 8, 9, 10, ['hello', [4, 5]], 3, 2, 1]
a = l.pop()
print(a) 
print(l)  
a = l.pop(1)
print(a, l) 
# l.sort()  # This will raise an error because the list contains mixed types
l.sort(key=lambda x: str(x))  # Sorts by string representation
for i in l:
    print(i)     