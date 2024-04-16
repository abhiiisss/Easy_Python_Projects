from random import randint

play_options = ["rock", "paper", "scissors"]


while True:

    computer_play = play_options[randint(0,2)] #play option for computer
    user_play = input("Chose one:Rock, Paper, Scissors? ").lower() #play option for user


    if computer_play == user_play:
        print("It's a tie")
    elif user_play == "rock":
        if computer_play == "Paper":
            print("You Lose! ", computer_play, "beats", user_play)
        else: #computer have played scissor
            print("You Won! ", user_play, "beats", computer_play)
    elif user_play == "paper":
        if computer_play == "Scissor":
            print("You Lose! ", computer_play, "beats", user_play)
        else: #computer have played rock
            ("You Won! ", user_play, "beats", computer_play)
    elif user_play == "scissor":
        if computer_play == "rock":
            print("You Lose! ", computer_play, "beats", user_play)
        else: #computer have played paper
            print("You Won! ", user_play, "beats", computer_play)    
    else:
        print("Not a valid option!, try again!!")