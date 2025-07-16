# # # f = open("in.txt")
# # f = open("lesson\\lesson14\\in.txt")
# # # print(f.read())
# # # print(f.read(5))
# # print(f.readline())
# # print(f.tell())
# # print(f.readline())
# # print(f.tell())
# # print(f.readlines())
# # print(f.tell())
# # f.seek(0)
# # print(f.readline())

# # f.close()

# with open("lesson\\lesson14\\in.txt") as f:
#     print(f.readline())
#     print(f.tell())
#     print(f.readline())
#     print(f.tell())
#     print(f.readlines())
#     print(f.tell())
#     f.seek(0)
#     print(f.readline())
# import os
# path = os.path.abspath(__file__)
# print(path)
# with open(os.path.dirname(path) +"\\out.txt", "a") as file:
# # with open(os.getcwd()+"\\out.txt", "w") as file:
#     file.write("hello\n")


with open("lesson\\lesson14\\in.txt") as f:
    for line in f:
        print(line)