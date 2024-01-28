#!/usr/bin/env python
# coding: utf-8

# Sorted List of Unique Letters

# In[ ]:


def unique_letters_sorted(input_string):
    return sorted(set(char.lower() for char in input_string if char.isalpha()))

# Test the function
input_str = "cheese"
result = unique_letters_sorted(input_str)
print(f"Unique Letters Sorted: {result}")


# Functions for Word Comparison

# In[ ]:


def letters_in_either(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower()))

def letters_in_both(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower()))

def letters_in_either_not_both(word1, word2):
    return sorted(set(word1.lower()) ^ set(word2.lower()))

# Test the functions
word1 = "hello"
word2 = "world"
result_either = letters_in_either(word1, word2)
result_both = letters_in_both(word1, word2)
result_either_not_both = letters_in_either_not_both(word1, word2)
print(f"Letters in Either Word: {result_either}")
print(f"Letters in Both Words: {result_both}")
print(f"Letters in Either, Not in Both: {result_either_not_both}")


# Country and Capital Management Program

# In[ ]:


country_capital_dict = {}

while True:
    country = input("Enter the name of a country (or 'exit' to terminate): ").capitalize()
    if country == 'Exit':
        break

    if country in country_capital_dict:
        print(f"The capital city of {country} is {country_capital_dict[country]}")
    else:
        capital = input(f"Enter the capital city of {country}: ").capitalize()
        country_capital_dict[country] = capital


# Frequency Analysis Program

# In[ ]:


def frequency_analysis(message):
    letter_counts = {}
    for char in message:
        if char.isalpha():
            char_lower = char.lower()
            letter_counts[char_lower] = letter_counts.get(char_lower, 0) + 1

    sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts[:6]

# Test the function
encrypted_message = "This is a sample encrypted message."
result_frequency_analysis = frequency_analysis(encrypted_message)
print(f"Six Most Common Letters: {result_frequency_analysis}")