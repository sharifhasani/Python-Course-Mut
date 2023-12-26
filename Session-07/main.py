# class definition
x = 10
# print(type(x))
address = {
    "city": "tehran",
    "street": "",
}
# name (str), family(str), address(dict), grade(float), term(str)



# class Student:
#     name = ""
#     family = ""
#     address = ""
#     grade = 0.0
#     term = "4021"

# s1 = Student()
# print(s1)



# create object
# s2 = Student()


# magic methods

# class Student:
#     # family = "Nasiri"
#     university = "tehran"
    
#     def __init__(self, name, family):
#         # print("__init__ is called")
#         # print(self)
#         self.name = name
#         self.family = family
    
#     def __str__(self):
#         return self.name + " " + self.family


# s1 = Student(name="ali", family="nasiri")
# # print(s1, "\n\n")

# s2 = Student(name="hassan", family="ghayoumi")
# print(s2)

# print(s1.name, s1.family, s1.university)
# print(s2.name, s2.family, s2.university)

# s1.name = "maryam"
# print(s1.name, s1.family, s1.university)

# print(s1)


# self in class



# properties
class Address:
    
    def __init__(self, city, street, floor):
        self.city = city
        self.street = street
        self.floor = floor

    

class Student:
    university = "tehran"
    
    def __init__(self, name, family, address):
        self.name = name
        self.family = family
        self.address = address
        self.grade = 0.0
    
    def __str__(self):
        return self.name + " " + self.family
    
    def set_grade(self, grade):
        self.grade = grade
    
    def get_grade(self):
        return self.grade


# s1_addr = Address(city="tehran", street="aaa", floor=1)
# s1 = Student(name="ali", family="nasiri", address=s1_addr)

# # print(s1.address.city)
# print(s1.get_grade())

# s1.set_grade(19.0)

# # print(s1.grade)

# grade = s1.get_grade()

# print(grade)

# try except

try:
    result = 10 / 0
    print(result)
except:
    print("Except scope")
finally:
    print("finally scope")


print("another process")
