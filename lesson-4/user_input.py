'''
    In this code exercise, we will learn about how to take 
    input from the user and print those input OR perform some
    action based on the input
''' 

## In order to take input, we use `input` method, which takes
## one parameter and that's a string of our own choice.

## Take an input and print output, when you will run this program, you 
## will notice that in your terminal or command line window, cursor will still at
## place OR continously blink, which actually implies waiting for some input, just
## something random and get the result, in my case I enter 5 and i will get 5 as result

first_input = input()
print(first_input)

'''
    Output: 5
            5

'''

## In above example, you noticed that, it is very annoying to see that blank
## cursor, which do nothing, and how we can even expect that a user will add
## something and get the ouput. So that's why we now add a input message.

second_input = input('Please enter something random and hit enter : ')
print(f'Can you see ? It is looking cool and informative and this is your input : {second_input}')

## Practice 1 : Take an input and based on input print even odd.

third_input = int(input('Please enter a number : '))
if(third_input % 2 == 0):
    print('Even')
else:
    print('Odd')

## You noticed that we got the result based on our input, but just before the input method
## We used another method `int`, which actually type-cast the input from string to integer
## By default, input method provided `string` value and then after we need to type-cast
## as per our requirement, like we did above. Otherwise, you will get an error while performing.
## mathematics computation over string value. That's it for input.