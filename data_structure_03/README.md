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

Lists support various operations, such as indexing, slicing, appending, and more. For example:

```python
fruits = ['apple', 'orange', 'banana']

# Accessing an item by index
print(fruits[0])  # Output: 'apple'

# Slicing
print(fruits[1:3])  # Output: ['orange', 'banana']

# Appending an item
fruits.append('grape')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'grape']
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

```python
colors = ('red', 'green', 'blue')

# Accessing an item by index
print(colors[0])  # Output: 'red'

# Slicing
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

```python
# Accessing a value by key
print(my_dict['name'])  # Output: 'John'

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print(my_dict)
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

Sets support various operations like adding elements, removing elements, and set operations:

```python
fruits_set = {'apple', 'orange', 'banana'}

# Adding an element
fruits_set.add('grape')
print(fruits_set)

# Removing an element
fruits_set.remove('orange')
print(fruits_set)
```
