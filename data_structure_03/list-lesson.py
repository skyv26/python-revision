"""
    Let's create an empty list, homogeneous, heterogeneous list and gradually add the things first 
    and then after perform the rest of the operation to understand
    the python list in a better way.
"""

# Normal Empty List
my_list = []
print(my_list)

# List of items of same type
my_list = [ 1, 3, 2, 6, 5, 4 ]
print(my_list)

# List of items of different types
my_list = [ 1, 2.0, '3', 'four' ]
print(my_list)

# Let's define an empty list again
my_list = []
print(my_list)

# Append the items into the list (Stack Behaviour)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print(my_list) # [ 1, 2, 3, 4, 5 ]

my_list.append('Aakash')
my_list.append('Verma')

print(my_list) # [ 1, 2, 3, 4, 5, 'Aakash', 'Verma' ]

# Access the items in different ways

zero_index_value = my_list[0] 
print(zero_index_value) # Zero index value

last_index_value = my_list[-1] 

print(last_index_value) # Last index value

sliced_list_of_value = my_list[2:5] 

print(sliced_list_of_value) # Print value from index 2 to index 4

#===================================================================

# Remove the value by index and element

my_list.remove(4)
print(my_list) # Remove element by the element 4

my_list.pop(4)
print(my_list) # Remove element by the index 4

#=============================================================

# Add the value at particular index

my_list.insert(3, 4)
print(my_list) # Add 4 as an element at index 3

my_list.insert(5, 'Aakash')
print(my_list) # Add Aakash as an element at index 5

#=============================================================

