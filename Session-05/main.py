# list indicies


sample_list = [9, 10, 11, 12, 1, 2, 4, 5, 6, 7, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(sample_list)
# print(sample_list[0])
# print(sample_list[2])

# print(sample_list[0:6])
# print(sample_list[6])

# print(sample_list[5: -1])



# loops in python

# for i in range(10):
#     print(i)



# range

# range(start=100, end=110, step=2)

# for i in range(100, 110, 2):
#     print(i)


# temp = range(100, 110, 2)
# print(temp)



# loop in list

# for item in sample_list:
#     print("Item:", item, "Exist in sample list")


# for item in sample_list[2: 8: 2]:
#     print("Item:", item, "Exist in sample list")

# print(len(sample_list))

# for i in range(len(sample_list)):
#     print("index=", i, "is", sample_list[i])


# i = 0
# for item in sample_list:
#     print("index=", i, "is", item)
#     i = i + 1


# print(sample_list[15])

# enumerate

# for index, value in enumerate(sample_list):
#     print("Index=", index, "Value=", value)


# for item in sample_list:
#     if item == 4:
#         print("Find 4, Break loops")
#         break
#     else:
#         print(item)

# for item in sample_list:
#     if item == 4:
#         print("Value is 4 and skip loop")
#         continue
#     else:
#         print(item)


adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# for adj in adjs:
#     for fruit in fruits:
#         print(fruit + " " + adj)
#     print("#####")


###########

# change item in list
# print(fruits[0])
# fruits[0] = "orange"
# print(fruits[0])

# add item to list
# print(fruits)
# fruits.append("orange")
# print(fruits)


# remove item from list
# print(fruits)
# fruits.remove("orange")
# print(fruits)

print(fruits)
del fruits
print(fruits)

# List Comprehension
