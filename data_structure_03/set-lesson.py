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
