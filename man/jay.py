import random

print("Welcome to our game ")
print("Hello there")
lucky = input("Enter your user-name")
print("Ohk")
lucky = input("Enter your age")
print("Ohk")
lucky = input("Choose your gender")
print("Ohk")
lucky = input("guess the number")

if lucky .isdigit():
    lucky =   int(lucky)
    
    if lucky <= 0:
        print("whatever you want to print")
        
        quit()
        
randy = random.randint(1, 15)
num=0

while True:
   num +=1

   new = input("make a guess")
   if new.isdigit():
       new = int(new)
   else:
       print ( "Type a new number next time")
       continue
   if new == randy:
       print("correct")
       break
   elif new > randy:
       print("you are close boiiiii,try harder")

   else:
       print("you are getting there, try harder")
print("you had", num , "guesses")

lucky = input("Please enter feedback")
print("Thank you")