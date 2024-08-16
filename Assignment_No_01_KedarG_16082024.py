#!/usr/bin/env python
# coding: utf-8

# In[21]:


print ("hello world !!")
print ("This is Kedar Ghogale, CDAC Pune.")
print ("Please find the solution of assignment number 01 below (16/08/2024) ..")


# In[3]:


# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Read temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"The equivalent temperature in Fahrenheit is: {fahrenheit}°F")


# In[4]:


import math

# Function to calculate the area of the circle
def calculate_area(radius):
    return math.pi * (radius ** 2)

# Function to calculate the perimeter (circumference) of the circle
def calculate_perimeter(radius):
    return 2 * math.pi * radius

# Read radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and perimeter
area = calculate_area(radius)
perimeter = calculate_perimeter(radius)

# Print the results
print(f"The area of the circle is: {area:.2f} square units")
print(f"The perimeter (circumference) of the circle is: {perimeter:.2f} units")


# In[5]:


# Function to calculate the final amount after adding interest
def calculate_final_amount(amount, interest_rate):
    interest = (amount * interest_rate) / 100
    return amount + interest

# Read the original amount from the user
amount = float(input("Enter the original amount: "))

# Read the interest rate (percentage) from the user
interest_rate = float(input("Enter the interest rate (in %): "))

# Calculate the final amount
final_amount = calculate_final_amount(amount, interest_rate)

# Print the final amount
print(f"The final amount after adding {interest_rate}% interest is: {final_amount:.2f}")


# In[6]:


# Function to convert meters to centimeters
def meters_to_centimeters(meters):
    return meters * 100

# Function to convert meters to inches
def meters_to_inches(meters):
    return meters * 39.3701

# Function to convert meters to yards
def meters_to_yards(meters):
    return meters * 1.09361

# Read distance in meters from the user
meters = float(input("Enter distance in meters: "))

# Convert the distance to centimeters, inches, and yards
centimeters = meters_to_centimeters(meters)
inches = meters_to_inches(meters)
yards = meters_to_yards(meters)

# Print the results
print(f"{meters} meters is equivalent to:")
print(f"{centimeters:.2f} centimeters")
print(f"{inches:.2f} inches")
print(f"{yards:.2f} yards")


# In[7]:


# Function to calculate profit or loss
def calculate_profit_or_loss(cost_price, selling_price):
    if selling_price > cost_price:
        return "Profit", selling_price - cost_price
    elif selling_price < cost_price:
        return "Loss", cost_price - selling_price
    else:
        return "No Profit No Loss", 0

# Read the cost price and selling price from the user
cost_price = float(input("Enter the actual cost price of the product: "))
selling_price = float(input("Enter the selling price of the product: "))

# Calculate profit or loss
result, amount = calculate_profit_or_loss(cost_price, selling_price)

# Print the result
if amount > 0:
    print(f"You made a {result} of {amount:.2f} units.")
else:
    print(f"You have {result}.")


# In[8]:


# Function to calculate the gross salary
def calculate_gross_salary(basic_salary):
    da = 0.75 * basic_salary  # DA is 75% of basic
    hra = 0.20 * basic_salary  # HRA is 20% of basic
    
    if basic_salary < 10000:
        gross_salary = basic_salary + da
    elif 10000 <= basic_salary < 20000:
        gross_salary = basic_salary + da + 0.50 * hra
    else:
        gross_salary = basic_salary + da + hra
    
    return gross_salary

# Read the basic salary from the user
basic_salary = float(input("Enter the basic salary: "))

# Calculate the gross salary
gross_salary = calculate_gross_salary(basic_salary)

# Print the gross salary
print(f"The gross salary is: {gross_salary:.2f}")


# In[9]:


# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Read a number from the user
number = int(input("Enter a number to find its factorial: "))

# Calculate the factorial
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fact = factorial(number)
    print(f"The factorial of {number} is: {fact}")


# In[10]:


# Function to calculate the sum of all numbers between num1 and num2
def sum_in_range(num1, num2):
    if num1 > num2:
        # Swap if num1 is greater than num2 to ensure correct range
        num1, num2 = num2, num1
    
    total_sum = 0
    for num in range(num1, num2 + 1):
        total_sum += num
    
    return total_sum

# Read the two numbers from the user
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))

# Calculate the sum of all numbers in the range
result = sum_in_range(num1, num2)

# Print the result
print(f"The sum of all numbers between {num1} and {num2} is: {result}")


# In[11]:


# Given tuple
num = (56, 2, 35, 41, 43, 48, 32, 56, 71, 55, 68)

# Initialize empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through the tuple and classify numbers as even or odd
for number in num:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print the resulting lists
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")


# In[12]:


# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Read a number from the user
number = int(input("Enter a number: "))

# Use the function to determine if the number is odd or even
result = check_odd_even(number)

# Print the result
print(f"The number {number} is {result}.")


# In[14]:


import math

# Function to perform calculations
def calculate_values(number):
    # Check if the number is valid for certain operations
    if number < 0:
        raise ValueError("Cannot compute square root, logarithm, or factorial for negative numbers.")
    if number == 0:
        raise ValueError("Cannot compute logarithm of zero.")
    
    square_root = math.sqrt(number)
    sin_value = math.sin(math.radians(number))  # Convert number to radians for sin
    tan_value = math.tan(math.radians(number))  # Convert number to radians for tan
    log_value = math.log(number)  # Natural logarithm (base e)
    factorial_value = math.factorial(int(number))  # Factorial (need integer)

    return square_root, sin_value, tan_value, log_value, factorial_value

# Read a number from the user
try:
    number = float(input("Enter a number: "))
    
    # Calculate values
    square_root, sin_value, tan_value, log_value, factorial_value = calculate_values(number)
    
    # Print the results
    print(f"Square root: {square_root:.2f}")
    print(f"Sine (in radians): {sin_value:.2f}")
    print(f"Tangent (in radians): {tan_value:.2f}")
    print(f"Logarithm (base e): {log_value:.2f}")
    print(f"Factorial: {factorial_value}")
    
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# In[15]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate(self):
        return self.length * self.width

# Create an object of the Rectangle class
# Read length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create an instance of Rectangle
rectangle = Rectangle(length, width)

# Calculate and print the area
area = rectangle.calculate()
print(f"The area of the rectangle is: {area:.2f}")


# In[ ]:




