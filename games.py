import random


def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None
    # !=

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < number_to_guess:
            print("Too low, try again!")
        elif guess > number_to_guess:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed it!")


# guess_the_number()


def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    player_choice = input("Enter rock, paper, or scissors: ").lower()

    if player_choice == computer_choice:
        print(f"It's a tie! Both chose {computer_choice}.")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print(f"You win! {player_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {player_choice}.")


# rock_paper_scissors()


def quiz_game():
    questions = {
        "What is the capital of France?": "a) Paris\nb) London\nc) Berlin\nd) Madrid",
        "What is 5 + 7?": "a) 10\nb) 11\nc) 12\nd) 13",
        "Which planet is known as the Red Planet?": "a) Earth\nb) Mars\nc) Jupiter\nd) Saturn",
    }

    answers = {
        "What is the capital of France?": "a",
        "What is 5 + 7?": "c",
        "Which planet is known as the Red Planet?": "b",
    }

    score = 0

    for question, options in questions.items():
        print(question)
        print(options)
        answer = input("Your answer: ").lower()

        if answer == answers[question]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"You got {score} out of {len(questions)} correct!")


quiz_game()



bridget = {
    "height": "6cm"
}

def boil_water():
    pass

def measure_garri():
    pass

def pour_hotwater():
    pass

def mix_both():
    pass


def make_eba():
    boil_water()
    measure_garri()
    pour_hotwater()
    mix_both()
    
    
    
def insert_card():
    pass


def input_pin():
    pass

def select_amount():
    pass

def withdraw_cash():
    pass


def atm_main():
    insert_card()
    input_pin()
    select_amount() #10k 
    withdraw_cash()



