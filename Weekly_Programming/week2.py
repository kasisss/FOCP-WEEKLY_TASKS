#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Task 1
user_name = input("Hello, what is your name? ")
print(f"Hello, {user_name}. Good to meet you!")


# In[8]:


# Task 2
celsius_temp = float(input("Enter a temperature in Celsius: "))
fahrenheit_temp = (celsius_temp * 9/5) + 32
print(f"{celsius_temp}C is equivalent to {fahrenheit_temp}F.")


# In[6]:


# Task 3
num_students = int(input("How many students? "))
group_size = int(input("Required group size? "))

num_groups = num_students // group_size
students_left_over = num_students % group_size

if num_groups == 1:
    print(f"There will be 1 group with {students_left_over} student{'s' if students_left_over != 1 else ''} left over.")
else:
    print(f"There will be {num_groups} groups with {students_left_over} student{'s' if students_left_over != 1 else ''} left over.")


# In[4]:


# Task 4
total_sweets = int(input("Enter the total number of sweets: "))
num_pupils = int(input("Enter the number of pupils: "))

sweets_per_pupil = total_sweets // num_pupils
sweets_left_over = total_sweets % num_pupils

print(f"Each pupil will receive {sweets_per_pupil} sweet{'s' if sweets_per_pupil != 1 else ''}, and there will be {sweets_left_over} sweet{'s' if sweets_left_over != 1 else ''} left over.")


# In[ ]:
