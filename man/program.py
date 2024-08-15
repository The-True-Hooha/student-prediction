print("hello")
name = input("what is your name")
name = str(name)
if name == str:
    print("welcome")
else:
    print("welcome")


age = input("how old are you")
if age.isdigit():
    age = int(age)
    
    if age > 3:
        print("you are old enough for this")
else:
    if age < 3:
        print("you can not use this")
    quit()

ready = input("are you ready")
true = "yes"
false = "no"
if true:
    print("let's start")
else:
    print("Bye")
    quit

import random


guess = input("guess the number I am thinking of")
if guess.isdigit():
    guess = int(guess)

    if guess <= 0:
        print("do not print a number less than 0 or  equals 0")
        quit()
else:
    quit()
      

randy = random.randint(0,20)
num=0
while True:
    num += 1
    new = input("guess again")
    if new.isdigit():
        new = int(new)
    else:
        print ("type a numner next time")
        continue
    if new == randy:
        print("you are right")
        break
    elif new > randy:
        print("tink harder you are close")
    else:
        print("try a higher number")
print("you had", num, "guesses")