from random import randint
score=0
alex = True
while(alex):

    player =input("what is your move(rock paper and scissors)? ")
    computer = randint(1, 3)

    if computer == 1:
        print("computer played rock")
    if computer == 2:
        print("computer played paper")
    if computer == 3:
        print("computer played scissors")

    if player == "rock" and computer == 1:
        print("its a tie!")
    elif player == "paper" and computer == 2:
        print("its a tie!")
    elif player == "scissors" and computer == 3:
        print("its a tie!")

    elif player == "rock" and computer == 3:
        print("player wins! ")
        score=score+1
    elif player == "paper" and computer == 1:
        print("player wins")
        score=score+1
    elif player == "scissors" and computer == 2:
        print("player wins")
        score=score+1
            
    elif player == "rock" and computer == 2:
        print("computer wins! ")
    elif player == "paper" and computer == 3:
        print("computer wins")
    elif player == "scissors" and computer == 1:
        print("computer wins")
    
    print("your score is ")
    print (score)

    bob =input ("do you whent to continue ")
    if bob =="no":
        alex = False
    