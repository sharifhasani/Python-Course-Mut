# list comprehension

# sample_list = []

# for i in range(100):
#     sample_list.append(i)

# print(sample_list)


# sample_list_2 = [x for x in range(0, 10)]
# print(sample_list_2)


# sample_list_2 = [x**2 for x in range(0, 10)]
# print(sample_list_2)

# sample_list = [x for x in range(10) if x >= 5]
# print(sample_list)


from hmac import new


car = ["benz", "bmw", "tesla"]

# sample_list = [car_name for car_name in car if len(car_name) > 3]
# print(sample_list)

# name = "ali, ALI"
# print(name.lower())
# print(name.upper())


# sample_list = [car_name.upper() for car_name in car ]
# print(sample_list)


# newlist = [True if x == "benz" else False for x in car] 
# print(newlist)

# newlist = [x*(10**-2) for x in range(100)]
# print(newlist[0])

# Dictionary
new_dict = {
    "name": "Ali",
    "family": "nasiri",
    "Age": 20,
}

# print(new_dict["name"], new_dict["family"])
# new_dict["name"] = "Hassan"
# print(new_dict["name"], new_dict["family"])
# print(len(new_dict))

# new_dict["grade"] = 19

# print(len(new_dict))
# print(new_dict)


# for item in new_dict:
#     print(new_dict[item])



# for item in new_dict:
#     print(new_dict[item])

# print(new_dict.keys())
# print(new_dict.values())

# for item in new_dict.keys():
#     print(item)


# for item in new_dict.values():
#     print(item)

# Tuple

new_tuple = ('apple', 'orange', 'banana', 'apple')
# print(new_tuple)


# print(new_tuple[0])

# for item in new_tuple:
#     print(item)


# Set

new_set = {'apple', 'orange', 'banana', 'apple'}
# print(len(new_set))

# for item in new_set:
#     print(item)

# print("apple" in new_set)

new_list = ['apple', 'orange', 'banana', 'apple','orange', 'banana', 'apple','orange', 'banana', 'apple']
# print(new_list)

# function definition

def custom_print_list(input_list):
    for item in input_list:
        print("##", item, "##")

length = len(new_list)

# print(length)

# custom_print_list(new_list)


# def mul(x, y):
#     return x * y

# result = mul(x=10, y=15)
# print(result)


def mul2(x=1, y=1):
    return x * y

result = mul2(x=50)
# print(result)


def mul(x:int, y:int) -> int:
    return x * y

mul()
