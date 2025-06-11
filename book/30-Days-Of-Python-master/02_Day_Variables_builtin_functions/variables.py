# 30DaysOfPython create a folder called day_2. 
first_name = 'Pablo Abigail'
last_name = 'Orellana Cardozo'
full_name = first_name + ' ' + last_name
country = 'Bolivia'
city = 'Cochabamba'
age = 33
year = 1991
is_married = True
is_true = True
is_light = False
titles = 'planificador', 'geoinformatics expert', 'cadastral expert', 'land administration expert'

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
print(type(titles))

len_first_name = len(first_name)
print(len_first_name)
len_last_name = len(last_name)
print(len_last_name)
comp_first_last = len_first_name - len_last_name
print(comp_first_last)

num_one = 5
num_two = 4
variable_total = num_one + num_two
substract_numbers = num_two - num_one
multiply_numbers = num_two * num_one
divide_numbers = num_one / num_two
mod_of_numbers = num_two % num_one
power_of_numbers = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius ** 2
print(area_of_circle)
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle)
input_radius = input('Enter the radius of the circle: ')
area_of_circle_2 = 3.14 * int(input_radius) ** 2
print(f' The area of the circle is: {area_of_circle_2}')
circum_of_circle_2 = 2 * 3.14 * int(input_radius)
print(f' The circum of the circle is: {circum_of_circle_2}')

name_input = input('Enter your name: ')
last_name_input = input('Enter your last name: ')
country_input = input('Enter your country: ')
age_input = input('Enter your age: ')

print(help('keywords'))
