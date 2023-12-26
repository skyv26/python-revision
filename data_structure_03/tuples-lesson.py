#=================================================

"""
Create a tuple and access the elements of the tuples
because we can't modify the tuple once created because
immutability behaviour.
"""

# Create a empty tuple
my_tuple = ()
print(my_tuple)
# Output: ()

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
# Output: (1, 2, 3, 4, 5)

my_tuple = (1, '2', 3.0, 'four')
print(my_tuple)
# Output: (1, '2', 3.0, 'four')

sliced_tuple = my_tuple[1:3]
print(sliced_tuple)
# Output: ('2', 3.0)

#=======================================================

# We can convert a list to tuple and vice versa

my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple) 
# Output: (1, 2, 3, 4)

my_list = list(my_tuple)
my_list.insert(1, 'Aakash')
my_list.insert(2, 'Verma')
my_tuple = tuple(my_list)
print(my_tuple)
# Output: (1, 'Aakash', 'Verma', 2, 3, 4)

#=====================================================