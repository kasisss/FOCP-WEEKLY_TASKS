#!/usr/bin/env python
# coding: utf-8

# Modified Greeting Program

# In[ ]:


user_name = input("Enter your name: ")
if user_name:
    print(f"Hello, {user_name}!")
else:
    print("Hello, Stranger!")


# Password Simulation Program

# In[ ]:


password1 = input("Enter a new password: ")
password2 = input("Enter the password again: ")

if password1 == password2:
    print("Password Set")
else:
    print("Error: Passwords do not match.")


# Password Length Requirement

# In[ ]:


while True:
    password1 = input("Enter a new password: ")
    password2 = input("Enter the password again: ")

    if password1 == password2 and 8 <= len(password1) <= 12:
        print("Password Set")
        break
    else:
        print("Error: Passwords do not match or do not meet length requirements.")


# Avoid Common Passwords
# 
# 

# In[ ]:


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password: ")
    password2 = input("Enter the password again: ")

    if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        print("Password Set")
        break
    else:
        print("Error: Passwords do not match, do not meet length requirements, or are common passwords.")


# User-Persistent Password Selection

# In[ ]:


BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while True:
    password1 = input("Enter a new password: ")
    password2 = input("Enter the password again: ")

    if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        print("Password Set")
        break
    else:
        print("Error: Passwords do not match, do not meet length requirements, or are common passwords. Please try again.")


# Seven Times Table

# In[ ]:


for i in range(13):
    result = i * 7
    print(f"{i} x 7 = {result}")


# Modified Times Table with User Input

# In[ ]:


table_number = int(input("Enter the number for the times table (0 to 12): "))

for i in range(13):
    result = i * table_number
    print(f"{i} x {table_number} = {result}")


# Backward Times Table

# In[ ]:


table_number = int(input("Enter the number for the times table (-12 to 12): "))

if table_number >= 0:
    for i in range(13):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
else:
    for i in range(12, -1, -1):
        result = i * abs(table_number)
        print(f"{i} x {table_number} = {result}")