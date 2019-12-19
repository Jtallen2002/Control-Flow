"""

Programmer: Jake Allen
Date: 12-16-19
Program: Guess My Number

"""

myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess

guess = int(input("Enter a guess: "))

# Keep asking users to guess my number until it is equal to myNumber

while guess != myNumber:
    guess = int(input("\nWrong, enter a new guess: "))

print("\nCongratulations, you found my number!")
