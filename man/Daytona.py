import random

#number guesser game
print("hello and welcome to my questionare and age guessing game")
name = input ("What is your name")
name1 = input ("What is your favourite color")
name2 = input ("How about ur faviorute food")
name3 = input ("Are u my friend")
name4 = input ("what is your gmail")
name5 = input ("What is your account number")
name6 = input ("Which bank holds thhis account number")
print("Your info is not safe wi me, HEHEHE!")

print(name)
Hi =  input("guess my age it is between numbers 0 to 9")
if Hi.isdigit():
    game = int(Hi)
    
    if game <= 0:
        print("whatever you want to print")
        quit()
else:
    quit()
    
    
randy = random.randint(0, 9)
num=0
while True:
    num += 1
    new = input("make a guess")
    if new.isdigit():
        new = int(new)
    else:
        print ( "type a number next time and don't add space before u start typing")
        continue
    if new == randy:
        print("correct")
        break
    elif new > randy:
        print("you are close nigga, try a bit harder")
    else:
        print("you are getting there, try harder")
print("you had ", num , "guesses")
GG1= print("U won ^_^")
print("This account number", name5, "under", name6, "Has now lost $30,000")
GG = print("GOODBYE! and thanks for playing")
