# Python Input-Output In-Depth Tutorial 🚀

## Introduction
Welcome to an in-depth exploration of Python's input and output features! In this lesson, we'll cover a variety of topics, from taking user input to advanced printing techniques. Buckle up for an exciting journey into the world of Python!

## 1. Taking User Input 🎤

To capture user input, Python provides the `input()` function. Let's see how it works:

```python
user_input = input("Enter something: ")
print("You entered:", user_input)
```

**Note:** The `input()` function always returns a string.

## 2. Type Conversion 🔄

### a. String to Integer and Vice Versa 🧮
Converting between string and integer is common. Pay attention to potential errors:

```python
# String to Integer
number_str = "42"
number_int = int(number_str)

# Integer to String
number_int = 42
number_str = str(number_int)
```

### b. String to Boolean 🤔
Convert a string to a boolean value:

```python
bool_str = "True"
bool_value = bool(bool_str)
```

### c. String to Binary and Hexadecimal 🤖
```python
# String to Binary
binary_str = bin(42)

# String to Hexadecimal
hex_str = hex(255)
```

## 3. Formatting Strings 💅

### a. String Interpolation 🎭
Create dynamic strings with f-strings:

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

## 4. Advanced Printing 🚀

### a. Printing with Symbols ✨
Enhance your output with Unicode symbols:

```python
print("This is a star symbol: \u2605")
```

### b. Newline and End Parameters 📝
Control your output formatting:

```python
print("First line\nSecond line")
print("This will not end with a newline", end=" ")
print("This will be on the same line.")
```

### c. Printing Online 🌐
Print immediately using `flush=True`:

```python
print("This will be printed", flush=True)
```

## Challenges 🏆

### Challenge 1
Write a program that takes two numbers as input, adds them, and prints the result with appropriate formatting.

### Challenge 2
Create a program that converts a given binary string to an integer.

### Challenge 3
Implement a function that takes a sentence as input, capitalizes the first letter of each word, and prints the modified sentence.
