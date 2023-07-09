# Lesson 3: Data Structures

## Introduction

Welcome to Lesson 3 on Data Structures! In this lesson, we will revise essential data structures in Python, including lists, tuples, dictionaries, and sets. We will explore how to work with these data structures to manipulate and organize data efficiently.

## Section 1: Lists

### What is a List?

A list is a versatile and mutable data structure in Python that can store a collection of items. Items in a list are ordered and can be of different data types.

### Creating Lists

You can create a list by enclosing items in square brackets `[]`. For example:

```python
my_list = [1, 2, 3, 'apple', 'orange']
```

### Basic Operations on Lists

Lists support various operations:

#### Indexing

Accessing an item by index:

```python
fruits = ['apple', 'orange', 'banana']
print(fruits[0])  # Output: 'apple'
```

#### Slicing

Slicing to get a subset of the list:

```python
print(fruits[1:3])  # Output: ['orange', 'banana']
```

#### Appending

Appending an item to the end of the list:

```python
fruits.append('grape')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'grape']
```

#### Extending

Extending a list with another list:

```python
vegetables = ['carrot', 'broccoli']
fruits.extend(vegetables)
print(fruits)  # Output: ['apple', 'orange', 'banana', 'grape', 'carrot', 'broccoli']
```

#### Inserting

Inserting an item at a specific index:

```python
fruits.insert(2, 'kiwi')
print(fruits)  # Output: ['apple', 'orange', 'kiwi', 'banana', 'grape', 'carrot', 'broccoli']
```

#### Removing

Removing an item by value:

```python
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'kiwi', 'grape', 'carrot', 'broccoli']
```

#### Popping

Popping an item by index:

```python
popped_item = fruits.pop(1)
print(popped_item)  # Output: 'orange'
print(fruits)       # Output: ['apple', 'kiwi', 'grape', 'carrot', 'broccoli']
```

#### Reversing

Reversing the order of items in the list:

```python
fruits.reverse()
print(fruits)  # Output: ['broccoli', 'carrot', 'grape', 'kiwi', 'apple']
```

#### Sorting

Sorting the list:

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 9]
```

## Section 2: Tuples

### What is a Tuple?

A tuple is an immutable and ordered collection of items in Python. Once created, the elements of a tuple cannot be changed.

### Creating Tuples

You can create a tuple by enclosing items in parentheses `()`. For example:

```python
my_tuple = (1, 2, 'apple', 'orange')
```

### Basic Operations on Tuples

While tuples are immutable, they support operations like indexing and slicing:

#### Indexing

Accessing an item by index:

```python
colors = ('red', 'green', 'blue')
print(colors[0])  # Output: 'red'
```

#### Slicing

Slicing to get a subset of the tuple:

```python
print(colors[1:3])  # Output: ('green', 'blue')
```

## Section 3: Dictionaries

### What is a Dictionary?

A dictionary is an unordered collection of key-value pairs. It allows you to store and retrieve data efficiently based on unique keys.

### Creating Dictionaries

You can create a dictionary by enclosing key-value pairs in curly braces `{}`. For example:

```python
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
```

### Basic Operations on Dictionaries

Dictionaries support operations like accessing values, adding new key-value pairs, and more:

#### Accessing a Value

Accessing a value by key:

```python
print(my_dict['name'])  # Output: 'John'
```

#### Adding a New Key-Value Pair

Adding a new key-value pair:

```python
my_dict['occupation'] = 'Engineer'
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'occupation': 'Engineer'}
```

#### Removing a Key-Value Pair

Removing a key-value pair by key:

```python
del my_dict['age']
print(my_dict)  # Output: {'name': 'John', 'city': 'New York', 'occupation': 'Engineer'}
```

#### Checking if a Key Exists

Checking if a key exists in the dictionary:

```python
if 'age' in my_dict:
    print("Age exists in the dictionary.")
else:
    print("Age does not exist in the dictionary.")
```

#### Getting Keys and Values

Getting all keys and values in the dictionary:

```python
keys = my_dict.keys()
values = my_dict.values()
print(keys)    # Output: dict_keys(['name', 'city', 'occupation'])
print(values)  # Output: dict_values(['John', 'New York', 'Engineer'])
```

#### Items

Getting key-value pairs as items:

```python
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('city', 'New York'), ('occupation', 'Engineer')])
```

## Section 4: Sets

### What is a Set?

A set is an unordered collection of unique elements in Python. Sets are useful for operations like intersection, union, and difference.

### Creating Sets

You can create a set by enclosing elements in curly braces `{}`. For example:

```python
my_set = {1, 2, 3, 'apple', 'orange'}
```

### Basic Operations on Sets

Sets support various operations:

#### Adding an Element

Adding an element to the set:

```python
fruits_set = {'apple', 'orange', 'banana'}
fruits_set.add('grape')
print(fruits_set)  # Output: {'apple', 'orange', 'banana', 'grape'}
```

#### Removing an Element

Removing an element from the set:

```python
fruits_set.remove('orange')
print(fruits_set)  # Output: {'apple', 'banana', 'grape'}
```

#### Set Operations

Performing set operations:

```python
favorite_colors = {'blue', 'green', 'red'}
rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'}

# Intersection
common_colors = favorite

_colors.intersection(rainbow_colors)
print(common_colors)  # Output: {'green', 'blue', 'red'}

# Union
all_colors = favorite_colors.union(rainbow_colors)
print(all_colors)  # Output: {'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'red'}

# Difference
unique_favorite_colors = favorite_colors.difference(rainbow_colors)
print(unique_favorite_colors)  # Output: set()

# Symmetric Difference
symmetric_diff = favorite_colors.symmetric_difference(rainbow_colors)
print(symmetric_diff)  # Output: {'orange', 'yellow', 'indigo', 'violet'}
```