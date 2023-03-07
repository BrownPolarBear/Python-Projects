#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for letter in text.lower():   
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if letter.isalpha(): 
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if letter not in dictionary:
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
           dictionary[letter] = 0 
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      dictionary[letter] +=1 
       # Increment the letter counter. 
  return dictionary

print(count_letters("AaBbCc"))

print(count_letters("Math is fun! 2+2=4"))

print(count_letters("This is a sentence."))


# In[3]:


print(count_letters("How many letters and occurrences are in this sentence?"))


# In[ ]:




