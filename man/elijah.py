import random

#def number_of_guesses ():#
 #   number = random.randint(1, 10)


player_f_name = input("Hello what is your first name:  ")
player_l_name = input("Hello what is your last name:  ")
# player_age = input ("Hello please how old are you: ")
player_sex = input ("Hello please what is your gender: ")
player_class = input ("Hello which class are you in: ")
number_of_guesses = 0
print ("okay, " + player_f_name + "_" + player_l_name +  "  i will like to play a guessing game with you,") 
okay, mike
print ("now guess")

number = random.randint(1, 20)

while  number_of_guesses < 8:
    guess = int(input())
    number_of_guesses +=1

    if guess < number:
        print("Your guess is low")
    elif guess > number:
            print ("your guess is high")
    else:
       break

if guess == number:                                     
        print ("Congratulations you get it")
else:
     print ("sorry, try again")
     
print("you had",  number_of_guesses, "guesses")