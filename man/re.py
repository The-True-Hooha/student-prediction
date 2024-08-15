import random

print("Hello! My name is Hanna. Welcome! You are expected to choose a name at random.")
name = input("What is your name? ")
age = input("How old are you? ")
nationality = input("What country are you from? ")

print(f"If you're {age} years old, then you can play.")
print("Good luck,", name)

words = ['uwa', 'shine', 'divine', 'octivia', 'rodney', 'praise', 'daniel']
word = random.choice(words)

print(word)
print("Guess the word, ", name)

guesses = ''
turns = 9

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nVictory! The word is:", word)
        break

    guess = input("\nGuess a letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", turns, 'more guesses')

        if turns == 0:
            print("You lose!")
