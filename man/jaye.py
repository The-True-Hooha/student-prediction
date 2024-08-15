import random

#this code is to prove that something has been learnt from the previous class
print("Prepare to unlock a new level of frustration *,*")
name1 = input("Welcome.Input guess")
name = input ("What is your name")

print(name, "are sure you can handle this?Well if you say so.")
Hi = input("guess the number in my mind which is between 0 to 30")
if Hi.isdigit():
    hi = int(Hi)
    
    if hi <=0:
        print("Come back CHILD!!!")
        quit()
else:
    quit()
    

randy = random.randint(0, 30)            
num =0
while True:
    num += 1
    new = input("make a guess")
    if new.isdigit():
        new = int(new)
    else:
        print ("Wrong input")
        continue
    if new == randy:
        print("correct")
        break
    elif new > randy:
        print("You are close nigga, try again (:")
    else:
        print("Close but not close enough.Try HARDER!!!")
print("you had", num, "guesses")
bye = print("This is the end off my game")
bye2 = print("GOOD JOB ^_^")