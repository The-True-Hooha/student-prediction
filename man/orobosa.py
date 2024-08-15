import random
# print("u are welcome. you are to choose a random name from mr.david's row")
# color = ("what is your complexion")
# age = input("how old are u")
# nationality = input("what country are u from ?")
# name = input("What is your name ?")
# print("i guess", color, "people are good")
# print("if u are", age, "then i guess u are able to play this game")
# print("Good Luck ! ", name)
# print("i guess we have other", nationality, "here")
words = ['orobosa', 
         'sheyi', 
         'divine', 
         'jaye', 
         'rokerfella', 
         'pere', 
         'kenneth', 
         'elijah', 
         'macaroni', 
         'ike', 
         'solomon', 
         'david'
        ]
word = random.choice(words)
print(word)

print("Guess the word", name)
guesses = ''
turns = 7
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("what ?")
            failed += 1
    if failed == 0:
        print("🥇victory🏆")
        print("The word is: ", word)
        break
    print()
    guess = input("guess a name:")
    mike 
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")