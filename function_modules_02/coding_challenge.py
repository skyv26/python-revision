# Write a function that calculates the area of a circle given its radius.
def areaOfCircle(r):
  from math import pi
  print(f"Area of circle with radius {r} : {pi*r*r}")

areaOfCircle(10)

# Create a module that contains a function to check if a number is prime.
from number_is_prime import number_is_prime

print(f"Number 0 is {'prime' if number_is_prime(0) else 'not prime'}")
print(f"Number 1 is {'prime' if number_is_prime(1) else 'not prime'}")
print(f"Number 2 is {'prime' if number_is_prime(2) else 'not prime'}")
print(f"Number 3 is {'prime' if number_is_prime(3) else 'not prime'}")
print(f"Number 9 is {'prime' if number_is_prime(9) else 'not prime'}")
print(f"Number 17 is {'prime' if number_is_prime(17) else 'not prime'}")
print(f"Number 27 is {'prime' if number_is_prime(27) else 'not prime'}")

# Import the math module and use it to calculate the factorial of a number.
import math

print(math.factorial(10))
