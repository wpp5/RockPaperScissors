import random
import time
delay = 1.5
#Making a list for computer options
ComputerOptions = ["rock","paper","scissors"]
#Collecting users name
UserName = input("What is your name?")
#This delay is to simulate the computer thinking
time.sleep(delay)
print("Welcome", UserName, "to my Rock-Paper-Scissors game")
time.sleep(delay)
x = "yes"
#This while loop will keep the programing running for the user to keep playing
while x == "yes":
    #This variables takes the user input
    UserChoice = input("Please choose from the following. Rock, paper, scissors").lower()
    #This statement will catch any user inpits outside of rock paper scissors
    if UserChoice in ComputerOptions:
        #This will generate a random computer choice
        ComputerChoice = random.choice(ComputerOptions)
        time.sleep(delay)
        print("You chose:",UserChoice)
        time.sleep(delay)
        print("Computer chose:",ComputerChoice)
        time.sleep(delay)
        #This series of if statements will tell the user whether user won or loss
        if UserChoice == ComputerChoice:
            print("It's tie!")
        elif UserChoice == "paper" and ComputerChoice == "rock":
            print("You win! Congrats")
        elif UserChoice == "paper" and ComputerChoice == "scissors":
            print("Oh! The computer won, that's ok!")
        elif UserChoice == "rock" and ComputerChoice == "paper":
            print("Oh! The computer won, that's ok!")
        elif UserChoice == "rock" and ComputerChoice == "scissors":
            print("You win! Congrats")
        elif UserChoice == "scissors" and ComputerChoice == "paper":
            print("You win! Congrats")
        elif UserChoice == "scissors" and ComputerChoice == "rock":
            print("Oh! The computer won, that's ok!")
        time.sleep(delay)
        print("Play again")
    else:
        print("Invalid input! Try again")




    


