# while True:
#     value = input("Enter a number (or 'exit' to quit): ")
#     print(value)


# number = int(input("Enter a number: "))
# while number < 10:
#     print(f"The number is less than 10. Current number: {number}")
#     number += 1
# else:
#     print(f"The number is now {number}. Exiting the loop.")


# print("The number is now 10 or greater. Exiting the loop.")



# for i in 10: TypeError: 'int' object is not iterable

# for i in "hello":
#     print(i)
# print("Done with the string loop.")
# l = [1,2,3, "hello", 4.5, [5, 6]]
# for i in l:
#     print(f"Current item: {i}")


# l = [1,2,3, "hello", 4.5, [5, 6]]
# for i in l:
#     print(f"Current item: {i}")

# l = (1,2,3, "hello", 4.5, [5, 6])
# for i in l:
#     print(f"Current item: {i}")

# l = "hello"
# for i in l:
#     print(f"Current item: {i}")

# l = set("hello")
# for i in l:
#     print(f"Current item: {i}")



# l = {"key1": 1, "key2": 2, "key3": 3}
# for i in l:
#     print(f"Current item: {i} -> {l[i]}")
# print(l.items())
# a, b = 1, 2
# print(f"Values before swap: a = {a}, b = {b}")
# a, b = b, a
# print(f"Values after swap: a = {a}, b = {b}")
# for  x in l.items():
#     print(f"Current item: {x} \t {x[0]} -> {x[1]}")
# for  k, v in l.items():
#     print(f"Current item: {k} -> {v}")

# l = [1, 2, 3, "hello", 4.5, [5, 6]]
# print(l)
# for i in l:
#     if type(i) is int:
#         i += 1
#     elif type(i) is str:
#         i = i.upper()
#     elif type(i) is list:
#         i.append(7)
#     print(f"Current item: {i}")

# print(l)

# print(list(enumerate(l)))
# print(list(enumerate("list")))
# print(l)
# for index, value in enumerate(l):
#     print(f"Index: {index}, Value: {value}")
#     if type(value) is int:
#         l[index] += 1
#     elif type(value) is str:
#         l[index].upper()
#     elif type(value) is list:
#         l[index].append(7)
#     # print(f"Current item: {i}")
# print(l)

# print(range(10))
# print(list(range(10)))
# print(list(range(-5, 5)))
# print(list(range(0, 10, 2)))
# print(list(range(10, 0, -1)))

# for i in range(len(l)):
#     print(f"Index: {i} Value: {l[i]}")
#     if type(l[i]) is int:
#         l[i] += 1
#     elif type(l[i]) is str:
#         l[i] = l[i].upper()
#     elif type(l[i]) is list:
#         l[i].append(7)

# print(l)


# text = input("Enter a string: ")
# s = 0
# for i in range(len(text)):
#     if text[i].isdigit():
#         s += int(text[i])
#     if s > 10:
#         print(f"Sum exceeded 10 at index {i}. Current sum: {s}")
#         break
#     print(f"Current character: {text[i]}, Current sum: {s}")
# else:
#     print(f"Sum did not exceed 10. Final sum: {s}")
# print(f"Final sum: {s}")



# text = input("Enter a string: ")
# s = 0
# for i in range(len(text)):
#     print(f"Processing character at index {i}: {text[i]}")
#     if not text[i].isdigit():
#         print(f"\tSkipping non-digit character: {text[i]}")
#         continue
#     print(f"\tProcessing character: {text[i]}")
#     s += int(text[i])
#     if s > 10:
#         print(f"\tSum exceeded 10 at index {i}. Current sum: {s}")
#         break
#     print(f"\tCurrent character: {text[i]}, Current sum: {s}")
# else:
#     print(f"Sum did not exceed 10. Final sum: {s}")
# print(f"Final sum: {s}")



# # print("Loop completed.")


# text = input("Enter a string: ")
# s = 0
# while True:
#     print(f"Current string: |{text}|")
#     if not text:
#         print("\tNo input provided. Exiting the loop.")
#         break
#     char = text[0]
#     print(f"\tProcessing character: {char}")
#     if not char.isdigit():
#         print(f"\tSkipping non-digit character: {char}")
#         text = text[1:]  # Remove the first character
#         continue
#     s += int(char)
#     if s > 10:
#         print(f"\tSum exceeded 10. Current sum: {s}. Exiting the loop.")
#         break
#     print(f"\tCurrent character: {char}, Current sum: {s}")
#     text = text[1:]  # Remove the first character


# sequence = {'p', 'a', 's', 's'}
# for val in sequence:
#     pass
# print("Loop completed.")

# for n in range(100):
#     if n % 2 == 0:
#         print(n, end=' ')
# print()
# for i in range(100):
#     if i % 2 != 0:
#         continue
#     print(i, end=' ')
# print()
# for i in range(0, 100, 2):
#     print(i, end=' ')
# print()
# i = 0
# while i < 100:
#     print(i, end=' ')
#     i += 2

# for i in range(100):
#     if i % 3 != 0:
#         continue
#     print(i, end=' ')
# print()

# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue 
#     print(i, end=' ')
# print()

# for i in range(100):
#     if i % 2 == 0:
#         continue  
#     print(i, end=' ')
# print()

from random import randint
random_list = [randint(1, 100) for _ in range(10)]
print("Random List:", random_list)

has_odd = False
for num in random_list:
    if num % 2 != 0:
        has_odd = True
        break

if has_odd:
    print("Список містить непарні числа.")
else:
    print("Усі числа в списку парні.")


for num in random_list:
    if num % 2 != 0:
        has_odd = True
        print("Список містить непарні числа.")
        break  
else:
    print("Усі числа в списку парні.")


if any(num % 2 != 0 for num in random_list):
    print("Список містить непарні числа.")
else:
    print("Усі числа парні.")

print( [num for num in random_list if num % 2 != 0])
if (num for num in random_list if num % 2 != 0):
    print("Список містить непарні числа.")
else:
    print("Усі числа парні.")