import random
def Pizza():
     print("Welcome to Tech-Camp 4.0")      
Pizza() 
def Divine():
     print("Tech-Camp 4.0 help people to Build, Code and Design")      
Divine() 
def Lattef():
     print("Some of tech camp courses include:"
           " Robotics"     
           " Data_Science"     
           " Abacus_counting"
           " Microbit"
           " Scratch"
           " Ballet"
           " Design"
           " Web Development")
Lattef()
def Who_I_Am():
     print("I'm your host Omokhuale Divine and my clients are",
           "Afoegba Elijah"
           "Rockerfella"
           "Egburedi Divine"
           "Obiora Uzoma"
           )      
def Name():
     print("Here are some names of some tech camp student and their course")      
Who_I_Am() 
Name()
def Miracle(zname):
      print(zname + " with" +" Data Science")
Miracle("Jaiye")
Miracle("Pere")
Miracle("Elijah")
def Phone(rname):
      print(rname + " with " +" Web development")
Phone("Tejiri")
Phone("Kelvin")
Phone("Efe")
def Brand(rname):
      print(rname + " with " +" Robotics")
Brand("Alexa")
Brand("Mine")
Brand("Mikel")
def bag(zip, pig):
      print(zip + " says" + pig)
bag("\nSkysenx", " welcome to our game")
def Hello(**hi):
      print("and " + hi["House"])
Hello(fname = "Tobias", House = "Have a nice time")
print("First is the guessing game")
import random
#number guesser game
print("hello and welcome to my questionare and age guessing game")
name = input ("What is your firstname:")
name30 = input("what is ur surname:")
name1 = input ("What is your favourite color:")
name2 = input ("What is ur faviorute gaming platform:")
name3 = input ("Are u my friend:")
def my_function(**kid):
  print("Pls begin the game " + kid["lname"], kid["fname"]) 
my_function(fname= name, lname = name30)
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
        print("you are close , try a bit harder")
    else:
        print("you are getting there, try harder")
print("you had ", num , "guesses")
print("Do you wish to continue(Yes / No)")
print("ohk")
GG1= print("🏆U won🏆")
GG= print("Proceeding to game-2........")
print("Game 2")
def my_fun(**kid):
  print("Pls begin the game Two " + kid["lname"], kid["fname"]) 
my_fun(fname= name, lname = name30)

print("You are welcome to game two , You have to guess the name in my mind")
color = input("wwhat is your complexion")
age = input("how old are u")
nationality = input("what country are u from ?")
print("i guess", color, "people are good")
print("if u are", age, "then i guess u are able to play this game")
print("Good Luck ! ", name)
print("You won't pass this level !!!")
words = ['Uzoma',' Divine', ' Elijah', ' Macaroni', ' Rockerfella']
word = random.choice(words)
print("Guess the word: ")
guesses = ''
turns = 4
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("what ?")
            failed += 1
    if failed == 0:
        print("🥇Congratulations🏆")
        print("The word is: ", word)
        break
    # print()
    guess = input("guess a name between:", 'Uzoma','Divine', 'Elijah', 'Macaroni', 'Rockerfella')
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")      
def my_Wo(**kid):
  print("Your smarter that I thought " + kid["lname"], kid["fname"]) 
my_Wo(fname= name, lname = name30)
def my_function(a, b):
  sum = a + b
  print("You are full of wisdom", name, "You have cashed out", sum)
my_function(100000, 200000)
print("math quiz is next")
print("My mood after the game")
def angel (mood):
    if mood == "happy":
        print ('sweet')
    else:
        print ('terrible')
angel ('Happy')   
num = 0 
  #1
print("NO.1")
print("addition")
print("a" ,"+", "b" , "=", 95)
y = input("")
n = int(y)
o = input("")
m = int(o)
if  m + n == 95:
        num += 1
        print("correct.👍👌🏅🥇🏆")
if  m + n != 95:
          num -= 1
          print("Loser👎👎")
      #2
print("NO.2")
print("addition")
print("a", "b" , 73)
y = input("")
n = int(y)
o = input("")
m = int(o)
if  m + n == 73:
        num += 1
        print("correct.👍👌🏅🥇🏆")
if  m + n != 73:
        num -= 1
        print("Loser👎👎")
      #3
print("NO.3")
print("addition")
print("a", "b" , 85)
y = input("")
n = int(y)
o = input("")
m = int(o)
if  m + n == 85:
        num += 1
        print("correct.👍👌🏅🥇🏆")
if  m + n != 85:
        num -= 1
        print("Loser👎👎")
      #4
print("NO.4")
print("multiplication")
print("a", "b" , 36)
y = input("")
n = int(y)
o = input("")
m = int(o)
if  m * n == 36:
        num += 1
        print("correct.👍👌🏅🥇🏆")
if  m * n != 36:
        num -= 1
        print("Loser👎👎")
      #5
print("NO.5")
print("Division")
print("a", "b" , 90)
y = input("")
n = int(y)
o = input("")
m = int(o)
if  n / m == 90:
        num += 1
        print("correct.👍👌🏅🥇🏆")
if  n / m != 90:
        num -= 1
        print("Loser👎👎")
      #6
print("NO.6")
print("Substraction")
print("a", "b" , 5)
y = input("")
n = int(y)
o = input("")
m = int(o)
if  n - m == 5:
          num += 1
          print("correct.👍👌🏅🥇🏆")
if  n - m != 5:
          num -= 1
          print("Loser👎👎")
print("you got",num,"out of 6")