import random

# random_number = random.randint(1,20);

# entry = "y"
# while entry == "y":
#     user_input = int(input("Enter a number guess: "))
#     if user_input == random_number:
#         print(f"You guessed correctly! The number is indeed {user_input}")
#         break;
#     else:
#         print("That was a wrong guess.")
#         entry = input("Do you want to guess a new number? y/n: ")
# print("Goodbye!");
random_number = random.randint(1,20);

while True:
    guess = int(input("Choose a number from 1 to 20: "));
    if guess < random_number:
        print("Guess is too low.")
    elif guess > random_number:
        print("Guess is too high")
    else:
        print("YOU WON!")
        print(random_number)
        play_again = input("Do you want to play again? y/n: ")
        if play_again == "y":
            random_number = random.randint(1,20);
            guess = None
        else:
            print("Thank you for playing the game.")
            break

