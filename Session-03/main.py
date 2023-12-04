# Mathematical Operators

# x = 10
# y = 21

# +
# z = x + y
# print(z)

# print("sum:", x + y, type(y + x))
# print("sub:", y - x, type(y - x))
# print("mul:", y * x, type(y * x))
# print("div:", y / x, type(y / x))

# x = 10.5
# y = 22.5

# print("sum:", x + y, type(y + x))
# print("sub:", y - x, type(y - x))
# print("mul:", y * x, type(y * x))
# print("div:", y / x, type(y / x))

# print("mod:", y % x)
# print("exp:", x ** y)
# print("floor:", y // x, type(y // x))





# Logical Operators

# x = 10
# y = 10

# variable_true = True
# variable_false = False

# result = variable_true and variable_false
# print(result)

# print(variable_true and variable_false, type(variable_true and variable_false))
# print(variable_true or variable_false)
# print(not variable_false)


# print(x is not y)
# print(x is y)

# in , not in
# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(20 in sample_list)
# print(20 not in sample_list)
# print(5 in sample_list)


# Bitwise Operators

# x = 7  # 0111, 1000
# y = 2  # 010

# print(x & y)
# #        010

# print(x | y)
# # 111

# print(x ^ y)
# 101

# print(~x)


# Condition Statements in Python

# if <condition>:
#     # statement

x = 100
y = 150

z = 100

# if z >= x:
#     # print("z > x")
#     print(z, ">=", x)
# else:
#     print('z < x')

# if z > x and z < y:
#     # print("z > x")
#     print("x < z < y")
# else:
#     print('z < x')


# if z > x or z < y:
#     # print("z > x")
#     print("z > x or z < y")

# if z < x:
#     print("z < x")

if z > x:
    print("z > x")
# elif z == x:
#     print("z == x")
elif z < x:
    print("z < x")
else:
    print("No conditions satisfied")

