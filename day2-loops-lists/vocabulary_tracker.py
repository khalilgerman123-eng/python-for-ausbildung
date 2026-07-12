# Day 2 - Exercise: German vocabulary tracker using loops and lists
how_many = input("How many words do you want to enter today? ")
how_many = int(how_many)
words = []

for i in range(how_many):
    word = input("Enter a German word you learned today: ")
    words.append(word)

print("Today you learned: ", words)
print(len(words))

if len(words) >= 5:
    print("Great job! You're building a strong vocabulary")
else:
    print("Good start! Try to learn more words tomorrow")
