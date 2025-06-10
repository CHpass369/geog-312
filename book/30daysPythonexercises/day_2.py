#Day 2: 30 Days of python programming
first_name = 'Pablo'
last_name= 'Orellana'
full_name = 'Pablo Abigail Orellana Cardozo'
country = 'Bolivia'
city = 'Cochabamba'
age = 33
year = 1991
is_married = True
is_true = True
is_light = True
wife ,daughter, dead_brother, live_brother = 'Nicole', 'Victoria', 'Emilio', 'Adrian'

#Data type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(wife))
print(type(daughter))
print(type(dead_brother))
print(type(live_brother))

#Compare the length of your first name and last name
len_firstname = len(first_name)
len_lastname = len(last_name)

print(f'The length of my first name is: {len_firstname}')
print(f'The length of my last name is: {len_lastname}')
difference = len_lastname - len_firstname
print(f'The diference between my first name and last name is: {difference} characters')

#declare new numbers
num_one = 5
num_two = 4
sum_numbers = num_one + num_two
subs_numbers = num_two + num_one
mult_numbers = num_two * num_one
div_numbers = num_two / num_one
mod_numbers = num_two % num_one
floor_numbers = num_two // num_one

print(f'the sum of the numbers is: {sum_numbers}')
print(f'the substraction of the numbers is: {subs_numbers}')
print(f'the multiplication of the numbers is: {mult_numbers}')

radius_1 = 30

import math

area_of_circle = math.pi * radius_1 ** 2
print(f'{area_of_circle:.3f}')

circunference_circle = 2 * math.pi * radius_1
print(f'{circunference_circle:.3f}')

input_user_radius = int(input ('Insert the radios of the circle: '))

area_of_circle2 = math.pi * input_user_radius ** 2
print(f'{area_of_circle2:.3f}')

circunference_circle2 = 2 * math.pi * input_user_radius
print(f'{circunference_circle2:.3f}')
