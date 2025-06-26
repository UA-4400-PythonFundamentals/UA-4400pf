# print(__name__)

# import math

# print(math.sin(25))
# print(math.pi)
# from math import pi, cos
# print(pi)
# print(cos(20))


# import sys
# from pprint import pprint

# pprint(sys.path)


# # sys.path.append("c:\\data\\github\\UA-4400\\UA-4400pf\\lesson")
# # pprint(sys.path)
# # from lesson07.lesson07 import s

# print(dir())
# from data import *
# import data
# from data import a as data_a, b, my_f as data_my_f
# import data as D
# print(dir())
# my_f()
# print(__name__)
# data_my_f()
# a= 20
# print(a)
# print(data.a)
# print(data_a)
# print(D.a)
# from data2 import print_name

# print_name()

# from utils import funk
# from utils.utilsl2.funk import printL2

# funk.my_print()
# printL2()
# from utils.utilsl2.funk import printL2

# import utils.utilsl2 as u2l
# import utils.util2d
# import utils.utilsl2.funk

# # utils.utilsl2.funk.printL2()
# u2l.funk.printL2()
# u2l.p()

init_dir_set = set(dir())
init_dir_set.add("init_dir_set")
from data3 import *
from data3 import b
# from data3 import a, _a, __a
after_import_dir_set = set(dir())

print(init_dir_set)
print(after_import_dir_set - init_dir_set)

import sys
print(sys.path)
