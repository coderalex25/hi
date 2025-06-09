from random import randint
player =input("what is your move(rock paper and scissors)? ")
computer = randint(1, 3)

if player == "rock" and computer == 1:
    print("its a tie!")
elif player == "paper" and computer == 2:
    print("its a tie!")
elif player == "scissors" and computer == 3:
    print("its a tie!")

elif player == "rock" and computer == 3:
    print("player wins! ")
elif player == 
