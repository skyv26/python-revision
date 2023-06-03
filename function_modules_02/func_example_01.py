
# Function with no parameter and no return value

def checking():
  print("Checking...")

# Function with parameter and return value

def does_number_is_odd(number):
  return number % 2 != 0

# Function with parameter without return value

def printMessage(number):
  checking()
  if(does_number_is_odd(number)):
   print(f"Number {number} is Odd")
  else:
   print(f"Number {number} is Even")


number_1 = 5
number_2 = 10
number_3 = 15

printMessage(number_1)
printMessage(number_2)
printMessage(number_3)
