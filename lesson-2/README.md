# Lesson 2: Functions and Modules

## Introduction

Welcome to Lesson 2 on Functions and Modules! In this lesson, we will delve into the concept of functions, how to create your own functions, and then move on to understanding modules and how to import them. We will also practice by writing and using your own functions and modules.

## Section 1: Functions

### What is a Function?

A function is a reusable block of code that performs a specific task or set of tasks. Functions are essential for breaking down complex programs into smaller, manageable parts, making your code more organized and easier to maintain.

### Creating Functions

To create a function in Python, you use the `def` keyword followed by the function name and a pair of parentheses. For example:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice") # Output: Hello, Alice!
```

In this example, we defined a function named `greet` that takes one parameter (`name`) and prints a greeting.

### Function Parameters and Return Values

**Functions** can take parameters (`inputs`) and can also return values (`outputs`). For example:

```python
def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8
```

In this example, the `add` function takes two `parameters`, *x* and *y*, and returns their **sum**.

## Modules and Libraries

## Section 2: Modules

Python `modules` are files containing Python code. They can define **functions**, `variables`, and *classes*, which can be used in other Python programs. Modules help organize code and make it more `reusable`.

### Importing Modules

To use functions and variables defined in a `module`, you need to import that module. Python provides the **import** statement for this purpose. For example:

```python
import math

result = math.sqrt(25)
print(result)  # Output: 5.0
```

In this example, we import the `math` module and use its `sqrt` function to calculate the square root of 25.

### Creating Your Own Modules

You can create your own modules by defining functions and variables in a separate **.py** file. For example, if you create a file named `my_module.py` with the following content:

```python

# my_module.py

def say_hello(name):
    print(f"Hello, {name}!")

greeting = "Welcome to my module!"

```

You can then import and use this module in another Python script:

```python

# your_main.py

import my_module

my_module.say_hello("Bob") # Output: Hello, Bob!
print(my_module.greeting) # Output: Welcome to my module!

```

## Section 3: Coding Exercises

Now, let's practice what we've learned with some coding exercises:

1. Write a function that calculates the area of a circle given its radius.
2. Create a module that contains a function to check if a number is prime.
3. Import the math module and use it to calculate the factorial of a number.

Feel free to experiment and create your own functions and modules for additional practice.

That's it for Lesson 2 on Functions and Modules! Functions and modules are fundamental building blocks in Python, and mastering them will greatly enhance your programming skills.

Keep coding, and feel free to ask if you have any questions!
