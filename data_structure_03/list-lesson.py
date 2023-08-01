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

print(my_list) # Output: [ 1, 2, 3, 4, 5, 'Aakash', 'Verma' ]

#=======================================================

# Access the items in different ways

zero_index_value = my_list[0] 
print(zero_index_value) # Zero index value
#Output: 1

last_index_value = my_list[-1] 
print(last_index_value) # Last index value
# Output: Verma

sliced_list_of_value = my_list[2:5] 
print(sliced_list_of_value) # Print value from index 2 to index 4
# Output: [3, 4, 5]

#===================================================================

# Remove the value by index and element

my_list.remove(4)
print(my_list) # Remove element by the element 4
# Output: [1, 2, 3, 5, 'Aakash', 'Verma']

my_list.pop(4)
print(my_list) # Remove element by the index 4
# Output: [1, 2, 3, 5, 'Verma']

#=============================================================

# Add the value at particular index

my_list.insert(3, 4)
print(my_list) # Add 4 as an element at index 3
# Output: [1, 2, 3, 4, 5, 'Verma']

my_list.insert(5, 'Aakash')
print(my_list) # Add Aakash as an element at index 5
# Output: [1, 2, 3, 4, 5, 'Aakash', 'Verma
#=============================================================

# Add a new list to extend the existing `my_list`

new_list = [ 6, 7, 8, 9, 10 ]
my_list.extend(new_list) 

print(my_list)
# Output: [1, 2, 3, 4, 5, 'Aakash', 'Verma', 6, 7, 8, 9, 10]

#=============================================================