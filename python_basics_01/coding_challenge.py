'''
1. Calculate the area of a rectangle with a width of 5 and a height of 10.
2. Check if a given number is even or odd.
3. Write a program to print the first 10 numbers in the Fibonacci sequence.
'''


# Calculate the area of a rectangle with a width of 5 and a height of 10

width = 5
height = 10

rectangle_formula = 2 * (width + height)

print(rectangle_formula)

# Check if a given number is even or odd

number_1 = 5
number_2 = 6

resultant_1 = number_1 % 2 != 0
resultant_2 = number_2 % 2 == 0
print(f"Number {number_1} is Odd")
print(f"Number {number_2} is Even")

# Write a program to print the first 10 numbers in the Fibonacci sequence
last_number = 0
next_number = 1
count = 0

while count < 10:
    print(last_number)
    new_number = last_number + next_number
    last_number = next_number
    next_number = new_number
    count += 1
