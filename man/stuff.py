import random

# number guesser game
print("hello, welcome to my random guessing game..")
name = input("what is your name")
print(name)
game = input("guess the number")
if game.isdigit():
    game = int(game)

    if game <= 0:
        print("whatever you want to print")
        quit()
else:
    quit()


randy = random.randint(0, 10)
print(randy)
num = 0
while True:
    num += 1
    new = input("make a guess")
    if new.isdigit():
        new = int(new)
    else:
        print("type a number next time")
        continue
    if new == randy:
        print("correct")
        break
    elif new > randy:
        print("you are close boiiii, you can try harder")
    else:
        print("you are getting there, try harder")
print("you had ", num, "guesses")
