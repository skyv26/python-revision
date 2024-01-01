"""

A dictionary in python is basically a hash-maps,
which exists in the key-value pair format. You can
create a dictionary using {} braces and make sure that
your keys should always be in a string but the values 
can be of any type, even in list Or tuple or set or 
a nested dictionary

"""

#===========================================

my_dictionary = {
    'name': 'Aakash',
    'age': 30,
    'height': 2.0,
    'favourite_colors': ('black', 'white'),
    'guessed_numbers': [1, 2, 3, 4, 5]
}

print(my_dictionary)
'''
  Output: {
    'name': 'Aakash',
    'age': 30, 
    'height': 2.0, 
    'favourite_colors': ('black', 'white'), 
    'guessed_numbers': [1, 2, 3, 4, 5]
}

'''

#===================================================

# But below is not acceptable

# my_dictionary = {
#     'name': 'Aakash',
#      age: 30,
#     'height': 2.0,
#     'favourite_colors': ('black', 'white'),
#     'guessed_numbers': [1, 2, 3, 4, 5]
# }

# print(my_dictionary)
# Output: Result in Error

#===================================================

# Access the value by key
print(my_dictionary['favourite_colors'])
# Output: ('black', 'white')

# Change the value at certain place
my_dictionary['age'] = 40
print(my_dictionary)

'''
  Output: {
    'name': 'Aakash',
    'age': 40, 
    'height': 2.0, 
    'favourite_colors': ('black', 'white'), 
    'guessed_numbers': [1, 2, 3, 4, 5]
}

'''

#===================================================

# Create a new key-value pair in existing dictionary

my_dictionary['key'] = 'value'

print(my_dictionary)

'''
  Output: {
    'name': 'Aakash',
    'age': 40, 
    'height': 2.0, 
    'favourite_colors': ('black', 'white'), 
    'guessed_numbers': [1, 2, 3, 4, 5],
    'key': 'value'
}

'''

#===================================================

# Access all the keys of dictionary
all_keys = my_dictionary.keys()
print(all_keys)
# Output: dict_keys(['name', 'age', 'height', 'favourite_colors', 'guessed_numbers', 'key'])


# If you want to convert obj to plain list then cast it using list method
all_keys = list(all_keys)
print(all_keys)
# Output: ['name', 'age', 'height', 'favourite_colors', 'guessed_numbers', 'key']

#===================================================

# Access all the values of dictionary
all_values = my_dictionary.values()
print(all_values)
# Output: dict_values(['Aakash', 40, 2.0, ('black', 'white'), [1, 2, 3, 4, 5], 'value'])


# If you want to convert obj to plain list then cast it using list method
all_values = list(all_values)
print(all_values)
# Output: ['Aakash', 40, 2.0, ('black', 'white'), [1, 2, 3, 4, 5], 'value']

#===================================================

# Remove a specific key-value pair of dictionary

del my_dictionary['key']
print(my_dictionary)

'''
  Output: {
    'name': 'Aakash',
    'age': 40, 
    'height': 2.0, 
    'favourite_colors': ('black', 'white'), 
    'guessed_numbers': [1, 2, 3, 4, 5],
}

'''