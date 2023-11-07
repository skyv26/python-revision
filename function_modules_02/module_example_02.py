# Import custom module function and variable

from customlibrary import check_num_is_positive, printTable

def checker(resultant):
   return 'positive' if resultant else 'negative'

resultant = check_num_is_positive(10)
print(f"Number 10 is {checker(resultant)}")
resultant = check_num_is_positive(-10)
print(f"Number -10 is {checker(resultant)}")

printTable(10)
