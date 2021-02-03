import random
import time
delay = 1.5
#Making a list for computer options
ComputerOptions = ["rock","paper","scissors"]
#Collecting users name
UserName = input("What is your name?")
time.sleep(delay)
print("Welcome", UserName, "to my Rock-Paper-Scissors game")
time.sleep(delay)
x = "yes"
while x == "yes":
    UserChoice = input("Please choose from the following. Rock, paper, scissors").lower()
    ComputerChoice = random.choice(ComputerOptions)
    time.sleep(delay)
    print("You chose:",UserChoice)
    time.sleep(delay)
    print("Computer chose:",ComputerChoice)
    time.sleep(delay)
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
    print("Play again!")




    


