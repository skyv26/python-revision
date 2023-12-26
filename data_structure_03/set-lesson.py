#======================================

# Create a empty set

empty_set = {}
print(empty_set)
# Output: {}

# Create a set of number

number_set = { 1, 2, 3, 4, 5}
print(number_set)
# Output: { 1, 2, 3, 4, 5 }

# But now if you try to add duplicate then it will always
# return the unique value, which means a set always
# exist of unique values, remove the duplicate behind the
# scenes.

number_set = { 1, 2, 3, 4, 4, 5, 5}
print(number_set)
# Output: { 1, 2, 3, 4, 5 }

#==============================================

my_set = {1}

# Add the value to set

my_set.add('Aakash')
my_set.add(2)
my_set.add(3)
my_set.add('Verma')
print(my_set)
# Output: {1, 2, 3, 'Aakash', 'Verma'}

#==============================================

my_set.remove('Aakash')
my_set.remove(2)
my_set.remove(3)
my_set.remove('Verma')
my_set.remove(1)
print(my_set)
# Output: set()

#=============================================

# Edge case

'''
If you want to create an empty set and later add the values
then below is not possible

variable = {}

variable.add('Aakash')

because behind the scene after definition `variable = {}`,
python consider variable of type dictionary not `Set`. So in
order to solve this problem. We need to explicitely tell
the interpreter we need an empty Set for later use.

'''

variable = set()

variable.add('Aakash')
print(variable)
# Output: { 'Aakash' }
