# Day 1 - Final project: Ausbildung eligibility checker
age = input("How old are you? ")
age = int(age)
name = input("What is your name? ")
country = input("What is your country? ")
years_left = 18 - age

if age >= 18:
    print(name + " from " + country + ", you are eligible to apply for Ausbildung in Germany!")
else:
    print(name + " from " + country + ", you need " + str(years_left) + " more years before you can apply.")
