
# import class date from module datetime

from datetime import date

# get the current year
current_year = date.today().year

def message(age):
  print(f"You are {age} years old!")

def yearlyTableOfAge(person_birth_year):
  for year in range(person_birth_year+1, current_year+1):
    if(year == current_year):
      print(f"In year {year}, you are {year - person_birth_year} years old !")
      break
    print(f"In year {year}, you were {year - person_birth_year} years old !")

def calculate_your_age(personBirthYear = 2000):
  message(current_year - personBirthYear)


calculate_your_age()
calculate_your_age(1995)
calculate_your_age(1990)
calculate_your_age(1985)

yearlyTableOfAge(1995)
