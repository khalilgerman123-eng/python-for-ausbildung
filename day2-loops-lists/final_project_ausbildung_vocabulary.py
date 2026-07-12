# Day 2 - Final project: Combining everything from Day 1 and Day 2
name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)

if age >= 18:
    print(name + ", you are eligible to apply for Ausbildung!")
else:
    print(name + ", you need a few more years before applying.")

how_many = int(input("How many words do you want to learn today? "))

while how_many < 1:
    how_many = int(input("Please enter a number of 1 or more: "))

words = []

for i in range(how_many):
    word = input("Enter a german word you learned: ")
    words.append(word)

print("\nHere is your vocabulary list:")

for i in range(len(words)):
    print(i + 1, "-", words[i])
