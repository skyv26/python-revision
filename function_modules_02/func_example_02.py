
# function with no parameter and no return value

def message(start, end):
  print(f"Counting from {start} to {end} :")

# function with default parameter no return value

def counting(start=1, end=10):
  message(start, end)
  while(start <= end):
    print(start)
    start+=1

counting()
counting(20, 50)
counting(-20)
