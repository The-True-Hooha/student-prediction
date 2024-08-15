import random

print ("hello welcome to my random guessing game")
game = input ("guess the decimal number")
if game.isdecimal():
    game = float(game)
    
    if game >= 0:
        print("help me")
        quit()

else:
    quit()
    
randy = random.randint(0.1,0.9)
num = 0
while True:
    num += 0.1
    good = input("make a guess")
    if good.isdecimal():
        good = float(good)
    else:
        print ("you are not doing well")
        continue
    if good == randy:
        print ("welldone")  
        break
    elif good > randy:
        print ("so close")
    
    
        
    


    