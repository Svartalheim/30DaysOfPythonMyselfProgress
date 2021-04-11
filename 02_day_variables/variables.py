# Day 2: 30 Days of Python Programming
# 1
firstname = "Aqsyal"
lastname = "Jamil"
fullname = "Aqsyal Raihan Jamil"
country = "Indonesia"
city = "Kediri"
age = 16
year = 2021
is_married = False
is_true = True
is_light_on = False
who, umur, where = "Aku", 17, "Home"

# 2
print(type(firstname))
print((type(lastname)))
print(type(fullname))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(city))
print(type(umur))

# 2
print("Length: ")
print(len(firstname))
print(len(lastname))
print(len(firstname) - len(lastname))

# 4
num_one = 5
num_two = 4
_total = num_one + num_two
_diff = num_one - num_two
_product = num_one * num_two
_division = num_one / num_two
_remainder = num_two % num_one
_exp = num_one ** num_two
_floor_division = num_one // num_two
print("Operators: ")
print(_total)
print(_diff)
print(_product)
print(_division)
print(_remainder)
print(_exp)
print(_floor_division)

#5
import math
radius = int(input("Enter this circle radius: "))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2*math.pi*radius
print(area_of_circle)
print(circum_of_circle)

#6
firstName = input("Enter your first name:")
lastName = input("Enter your last name:")
Country = input("Enter your Country: ")
Age = input("Enter your age: ")