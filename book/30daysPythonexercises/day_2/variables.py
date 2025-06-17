''' Day 2: 30 Days of Python programming
   Variables and Data Types'''

first_name = 'Pablo Abigail'
last_name = 'Orellana Cardozo'
country = 'Bolivia'
city = 'Cochabamba'
age = 33
year = 1991
is_married = True
is_true = True
is_light = False
programming_language, db_language, data_science= 'Python', 'PostgreSQL', 'R'
skills = ['Python', 'JavaScript', 'HTML', 'CSS']
person_info = {
   'firstname':'Pablo Abigail',
   'lastname':'Orellana Cardozo',
   'country':'Bolivia',
   'city':'Cochabamba'
   }

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(programming_language))
print(type(db_language))
print(type(data_science))
print(type(skills))
print(type(person_info))

#Using the len() built-in function, find the length of your first name
print(len(first_name))
print(len(last_name))
print(len(country))
print(len(city))
print(len(str(age)))
print(len(str(year)))
print(len(str(is_married)))
print(len(str(is_true)))
print(len(str(is_light)))
print(len(programming_language))
print(len(db_language))
print(len(data_science))
print(len(skills))
print(len(person_info))
print(len(skills[0]))
print(len(person_info['firstname']))

#Compare the length of your first name and your last name
print(f'{first_name} has {len(first_name)} characters and {last_name} has {len(last_name)} characters.')
print(len(first_name) == len(last_name))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
 
 #Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

#Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

#The radius of a circle is 30 meters
radius = 30
#Calculate the area of a circle and assign the value to a variable area_of_circle
pi = 3.14
area_of_circle = pi * radius**2    
#Calculate the circumference of a circle and assign the value to a variable circum_of_circle
circum_of_circle = 2 * pi * radius
#Take radius as user input and calculate the area.
radius_input = float(input("Enter the radius of the circle: "))
area_of_circle_input = pi * radius_input**2

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name_input = input("Enter your first name: ")
last_name_input = input("Enter your last name: ") 
country_input = input("Enter your country: ")
age_input = int(input("Enter your age: "))

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
import keyword
# Print the list of Python keywords
print(keyword.kwlist)  