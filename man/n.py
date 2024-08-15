import random




#number guesser game
print("WELCOME TO MY GUESSER GAME IF YOU WOUULD LIKE TO PLAY, TYPE ANY NUMBER OF YOUR CHOICE")
print("BUT FIRSTLY")
IG=input("WHAT IS YOUR NAME")
FB=input("SEX")
print("YOU CAN START MY GAME NOW GOODLUCK!")

jackpot = input("guess a number from 0 to 12")
if jackpot. isdigit():
    jackpot = int(jackpot)    

    if jackpot <= 0:
        print("whatver you want to print")
        quit()
else:
    quit() 
bingo = input("try guessing another number ")
pk = input("try another guess")
sharingan =input("keep guessing")
randy = random.randint(0, 12)
num=0
while True:
    num += 1
    new = input("make a guess")
    if new.isdigit():
        new = int(new)
    else:
        print ("try typing a number next time")
        continue
    if new == randy:
        print("correct")
        break
    elif new > randy:
        print("you are close, dont give up ")
    else:
        print("you are getting there, try harder")
print("congratulation you had", num ,"guesses")                               
             
