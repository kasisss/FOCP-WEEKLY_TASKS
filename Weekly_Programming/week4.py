#!/usr/bin/env python
# coding: utf-8

# Validate Input Range

# In[ ]:


def validate_input(num):
    return 0 <= num <= 100

# Test the function
user_input = int(input("Enter an integer: "))
print(validate_input(user_input))


# Count Uppercase and Lowercase Letters

# In[ ]:


def count_letters(input_string):
    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())
    return uppercase_count, lowercase_count

# Test the function
user_string = input("Enter a string: ")
result = count_letters(user_string)
print(f"Uppercase letters: {result[0]}, Lowercase letters: {result[1]}")


# Modified Greetings Program

# In[ ]:


def format_name(name):
    return name.capitalize()

# Test the function
user_name = input("Enter your name: ")
formatted_name = format_name(user_name)
print(f"Hello, {formatted_name}. Good to meet you!")


# Remove Last Character from String

# In[ ]:


def remove_last_char(input_string):
    return input_string[:-1]

# Test the function
user_input = input("Enter a string: ")
result = remove_last_char(user_input)
print(f"String with last character removed: {result}")


# Temperature Conversion Functions

# In[ ]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
celsius_temp = float(input("Enter temperature in Celsius: "))
print(f"{celsius_temp}°C is equivalent to {celsius_to_fahrenheit(celsius_temp)}°F")

fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
print(f"{fahrenheit_temp}°F is equivalent to {fahrenheit_to_celsius(fahrenheit_temp)}°C")


# Program for Temperature Conversion

# In[ ]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Test the program
user_input = input("Enter temperature in Celsius (e.g., 25C): ")
celsius_temp = float(user_input[:-1])
print(f"Equivalent temperature in Fahrenheit: {celsius_to_fahrenheit(celsius_temp)}°F")


# Program for Temperature Statistics

# In[ ]:


temperatures = []

for _ in range(6):
    user_input = input("Enter a temperature (e.g., 25C): ")
    celsius_temp = float(user_input[:-1])
    temperatures.append(celsius_temp)

print(f"Maximum temperature: {max(temperatures)}°C")
print(f"Minimum temperature: {min(temperatures)}°C")
print(f"Mean temperature: {sum(temperatures) / len(temperatures)}°C")


# Modified Temperature Statistics Program

# In[ ]:


temperatures = []

while True:
    user_input = input("Enter a temperature (press Enter to finish): ")
    
    if not user_input:
        break
    
    celsius_temp = float(user_input[:-1])
    temperatures.append(celsius_temp)

print(f"Maximum temperature: {max(temperatures)}°C")
print(f"Minimum temperature: {min(temperatures)}°C")
print(f"Mean temperature: {sum(temperatures) / len(temperatures)}°C")
