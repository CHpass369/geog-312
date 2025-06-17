age = 33
height = 1.85
complex_number = 3 + 4j

base = input("Enter the base of the triangle: ")
height_triangle = input("Enter the height of the triangle: ")
print(f"The area of the triangle is: {0.5 * float(base) * float(height_triangle)}")

side_a = input("Enter the length of side a: ")
side_b = input("Enter the length of side b: ")
side_c = input("Enter the length of side c: ")
perimeter = float(side_a) + float(side_b) + float(side_c)
print(f"The perimeter of the triangle is: {perimeter}")

length_rectangle = input("Enter the length of the rectangle: ")
width_rectangle = input("Enter the width of the rectangle: ")
area_rectangle = float(length_rectangle) * float(width_rectangle)
print(f"The area of the rectangle is: {area_rectangle}")
perimeter_rectangle = 2 * (float(length_rectangle) + float(width_rectangle))
print(f"The perimeter of the rectangle is: {perimeter_rectangle}")

radius_circle = input("Enter the radius of the circle: ")
pi = 3.14
area_circle = pi * float(radius_circle) ** 2
circumference_circle = 2 * pi * float(radius_circle)
print(f"The area of the circle is: {area_circle}")
print(f"The circumference of the circle is: {circumference_circle}")

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope = 2
x_intercept = 1  # When y = 0, x = 1
y_intercept = -2  # When x = 0, y = -2  
print(f"The slope of the line is: {slope}")
print(f"The x-intercept of the line is: {x_intercept}") 

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"The slope between the points is: {slope}")
print(f"The Euclidean distance between the points is: {euclidean_distance}")

#Compare the slopes in tasks 8 and 9.
print(f"The slope from task 8 is {slope} and the slope from task 9 is {slope}. They are equal.")

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_values = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
for x in x_values:
    y = x**2 + 6*x + 9
    print(f"When x = {x}, y = {y}")
    if y == 0:
        print(f"The value of x that makes y equal to 0 is: {x}")
        break

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len("python")
dragon_length = len("dragon")
print(f"The length of 'python' is {python_length} and the length of 'dragon' is {dragon_length}.")
print(f"Is the length of 'python' equal to the length of 'dragon'? {python_length != dragon_length}")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print(f"Is 'on' found in both 'python' and 'dragon'? {'on' in 'python' and 'on' in 'dragon'}")

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print(f"Is 'jargon' in the sentence? {'jargon' in sentence}")

#There is no 'on' in both dragon and python
print(f"Is 'on' not found in both 'dragon' and 'python'? {'on' not in 'dragon' and 'on' not in 'python'}")

# Find the length of the text python and convert the value to float and convert it to string
python_length_float = float(python_length)
print(f"The length of 'python' as a float is: {python_length_float}")
python_length_str = str(python_length_float)
print(f"The length of 'python' as a string is: {python_length_str}")

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = input("Enter a number to check if it is even: ")
number = int(number)  # Convert input to integer
is_even = number % 2 == 0
print(f"Is the number {number} even? {is_even}")

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(f"Is the floor division of 7 by 3 equal to the int converted value of 2.7? {7 // 3 == int(2.7)}")
print(f"The result of the floor division of 7 by 3 is: {7 // 3}")

#Check if type of '10' is equal to type of 10
print(f"Is the type of '10' equal to the type of 10? {'10' == 10}")

#Check if int('9.8') is equal to 10
try:
    print(f"Is int('9.8') equal to 10? {int(float('9.8')) == 10}")
except ValueError:
    print("Invalid input")

hours = input("Enter the number of hours: ")
rate_per_hour = input("Enter the rate per hour: ")
hours = float(hours)
rate_per_hour = float(rate_per_hour)
weekly_earning = (hours*5) * rate_per_hour
print(f"Your weekly earning is: {weekly_earning}")


for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")