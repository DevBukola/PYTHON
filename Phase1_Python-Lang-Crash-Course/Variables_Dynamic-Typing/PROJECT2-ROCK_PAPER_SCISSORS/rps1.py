print("...Rock");
print("...Paper");
print("...Scissors");

player1 = input("Player 1, make your choice: ");
print("***NO CHEATING!\n\n" * 20);
player2 = input("Player 2, make your choice: ");

if player1 == player2:
    print("It is a tie!");
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!");
    elif player2 == "paper":
        print("Player 2 wins!");
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!");
    elif player2 == "scissors":
        print("Player 2 wins!");
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 wins!");
    elif player2 == "paper":
        print("Player 1 wins!");
else:
    print("Something went wrong.");

        


# if player1 == "rock" and player2 == "scissors":
#     print("Player 1 wins!");
# elif player1 == "rock" and player2 == "paper":
#     print("Player 2 wins!");
# elif player1 == "paper" and player2 == "rock":
#     print("Player 1 wins!");
# elif player1 == "paper" and player2 == "scissors":
#     print("Player 2 wins!");
# elif player1 == "scissors" and player2 == "rock":
#     print("Player 2 wins!");
# elif player1 == "scissors" and player2 == "paper":
#     print("Player 1 wins!");
# elif player1 == player2:
#     print("It is a tie!");
# else:
#     print("Something went wrong.");