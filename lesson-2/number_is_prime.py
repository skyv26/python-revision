def number_is_prime(number):
  if(number == 0 or number == 1 or number == 2):
    return True
  else:
    count = 0
    for i in range(2, number+1):
      if(number % i == 0):
        count+=1
    return count <= 1
