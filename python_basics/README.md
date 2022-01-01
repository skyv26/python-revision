# Lesson 1: Python Basics

## Introduction

Welcome to the first lesson on Python Basics! In this lesson, we will cover the foundational concepts that every Python programmer should know. We will start with the basics, including variables, data types, and basic operations. After that, we will review control structures like if statements and loops (for and while). To reinforce your learning, we will also work on small coding exercises.

## Section 1: Variables and Data Types

### Variables

A variable is a name that can store data. In Python, you can create a variable by assigning a value to it. For example:

```python
my_variable = 42
```

Here, my_variable is a variable that stores the integer value 42.

### Data Types

Python has several built-in data types, including:

- Integers (int)
- Floats (float)
- Strings (str)
- Booleans (bool)

You can use the `type()` function to check the data type of a variable:

```python
my_integer = 42
my_float = 3.14
my_string = "Hello, Python!"
my_boolean = True

print(type(my_integer))  # Output: <class 'int'>
print(type(my_float))    # Output: <class 'float'>
print(type(my_string))   # Output: <class 'str'>
print(type(my_boolean))  # Output: <class 'bool'>
```

### Basic Operations

Python supports basic arithmetic operations like addition, subtraction, multiplication, and division. For example:

```python
x = 10
y = 5

addition = x + y       # 10 + 5 = 15
subtraction = x - y    # 10 - 5 = 5
multiplication = x * y # 10 * 5 = 50
division = x / y       # 10 / 5 = 2.0 (always returns a float)

print(addition, subtraction, multiplication, division)

```

## Section 2: Control Structures

### If Statements

An `if` statement is used for conditional execution. It allows you to run a block of code only if a specified condition is `True`. For example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

```

### Loops

Python supports two primary types of loops: for and while loops.

#### For Loop

A `for` loop is used to iterate over a sequence (e.g., a `list`, `tuple`, or `string`). For example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

#### While Loop

A `while` loop is used to execute a block of code repeatedly as long as a specified condition is `True`. For example:

```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1

```

## Section 3: Coding Exercises

Let's practice what we've learned with some `coding` exercises. Try to write Python code to solve the following tasks:

1. Calculate the area of a rectangle with a width of 5 and a height of 10.
2. Check if a given number is even or odd.
3. Write a program to print the first 10 numbers in the Fibonacci sequence.

Feel free to reach out if you have any questions or need help with the exercises.

That's it for Lesson 1 on Python Basics! Make sure to practice these concepts and complete the coding exercises. In the next lesson, we'll dive deeper into Python's data structures and functions.
