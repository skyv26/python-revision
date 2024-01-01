'''

In this lesson we will learn, how to use `print` method
to print anything, in all possible way and we will see
how print method is easy and comes handy in terms of 
printing the data in a specific format.

'''

## Let's take a variable and print "Hello, World" message.
message = 'Hello, World!'
print(message)
# Output: Hello, World!

## But now let's remove the World from the string and print value of two variable at the same time.
message = 'Hello, '
name = 'Tom!'
print(message, name)
# Output: Hello,  Tom!

## Did you notice that, there was an extra space after "Hello, " ?
## That space comes because whenever we print the variables comma
## separate, we will get a space automatically. But how do we can 
## fix this issue ? We can consider using the string formatter method-I. Like below

print(f"{message}{name}")
# Output: Hello, Tom!

## OR

print(f"{message}{name} How are you ?")
# Output: Hello, Tom! How are you ?

## Now let's practice, what we learnt so far ?


## Practice 1: Print the number from 1 to 10 (Simple)

for each in range(1, 11):
    print(each)

# Output: 1
#         2
#         3
#         .
#         .
#         .
#         10

## Practice 2: Greet all person in the list (Simple)

person_list = ['Tom', 'Aakash', 'Mary', 'Harry', 'Catherine']

for each in person_list:
    print(f"Hello, {each}")

# Output: Hello, Tom
#         Hello, Aakash
#         .
#         .
#         Hello, Catherine

## Practice 3: Print the table of "any_number"
any_number = 5 # Put your desired value and check the output

for num in range(1, 11):
    print(f"{any_number} x {num} = {any_number * num}")

## Practice 4: Print the list of message in correct format

message = ['Hi!', ' Aakash', ' How ', 'are ', 'you ?']

for each in message:
    print(each)

# Output: Hi!
#          Aakash
#          How 
#         are
#         you ?

## Oops!!!!!
## Do you know how the print is working behind the scene ?
## As you can understand that like any other python function or method
## `print` is also a function or method in python, which takes `n` number of arguments as parameter
## but the last parameter of print is optional or default parameter and the name of that
## parameter is `end` By default it is something like end='\n' to print everything on new line
#. So now if I try it now using `end`

for each in message:
    print(each, end='')

# Output: Hi! Aakash How are you ?

## But now if you try to print something else without end, then you will see something strange
## your result will print right next after the previous output, because the cursor of the terminal
## was previously ended at the previous text.

print('something strange!')

# Output: Hi! Aakash How are you ?something strange!

## From now if your print something, everything will be normal again.

print('Now it is normal')

# Output: Now it is normal

### Conclusion: By default python print a message and leave a blank space after the message that
##              we print, because of the default parameter behavior, which you can alter in your way
#               You can end the line even with any character of your choice, but don't forget that, 
#               based on your action, the next output will work accordingly.

## Last but not least

## String format method-II (Interpolation)

message = "Welcome to {lang} and it is a {lesson} lesson".format(lang='Python', lesson=4)
print(message)

## String format methond-III (Interplolation using the placeholders, old school way)

message = "Welcome to %s and it is a %d lesson" % ('Python', 4)
print(message)

## Above method you need to know and remember where and when to use the placeholder correctly.
## But first 2 methods are most widely used by the people all around the world.