#!/usr/bin/env python
# coding: utf-8

# Binary Representation

# In[ ]:


def to_binary_representation(number):
    if number <= 0:
        return "Invalid input. Please provide a positive integer."

    return bin(number)[2:]

# Test the function
number_to_convert = 15
binary_result = to_binary_representation(number_to_convert)
print(f"Binary representation of {number_to_convert}: {binary_result}")


# Factors of an Integer
# 

# In[ ]:


def find_factors(number):
    if number <= 0:
        return "Invalid input. Please provide a positive integer."

    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors

# Test the function
number_to_factorize = 12
factors_result = find_factors(number_to_factorize)
print(f"Factors of {number_to_factorize}: {factors_result}")


# Prime Number Checker
# 

# In[ ]:


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

# Test the function
number_to_check = 13
prime_result = is_prime(number_to_check)
print(f"{number_to_check} is prime: {prime_result}")


# Simple Encryption
# 

# In[ ]:


def simple_encrypt(message):
    reversed_message = message[::-1].replace(" ", "")
    return reversed_message

# Test the function
original_message = "Hello World"
encrypted_result = simple_encrypt(original_message)
print(f"Original Message: {original_message}")
print(f"Encrypted Message: {encrypted_result}")


# Randomized Encryption

# In[ ]:


import random
import string

def randomized_encrypt(message):
    interval = random.randint(2, 20)
    random_letters = ''.join(random.choices(string.ascii_lowercase, k=interval - 1))
    
    encrypted_message = ""
    for i, char in enumerate(message):
        if char.isalpha():
            encrypted_message += char + random_letters[i % (interval - 1)]
        else:
            encrypted_message += char

    return encrypted_message, interval

# Test the function
message_to_encrypt = "send cheese"
encrypted_result, interval_used = randomized_encrypt(message_to_encrypt)
print(f"Original Message: {message_to_encrypt}")
print(f"Encrypted Message: {encrypted_result}")
print(f"Interval Used: {interval_used}")


# Decrypt Randomized Message

# In[ ]:


def randomized_decrypt(encrypted_message, interval_used):
    decrypted_message = ""
    for i in range(0, len(encrypted_message), interval_used):
        decrypted_message += encrypted_message[i]

    return decrypted_message

# Test the function
decrypted_result = randomized_decrypt(encrypted_result, interval_used)
print(f"Decrypted Message: {decrypted_result}")
